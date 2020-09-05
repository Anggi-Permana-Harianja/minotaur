'''
import modules
'''
import os
import datetime as dt
import pandas as pd
import pandas_datareader as pdr
from matplotlib import pyplot as plt
from matplotlib import style


'''
getting historical stock price data
'''
class Simple_chart():
    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.ma = None
        self.df = None

    def ingest(self):
        style.use('ggplot')
        start = dt.datetime(2000, 1, 1)
        today = dt.date.today()
        end = dt.datetime(today.year,
                        today.month,
                        today.day)
        #getting stock price data from Yahoo Finance
        df = pdr.DataReader(self.stock_code,
                            'yahoo',
                            start,
                            end)
        #saving ingested dataset into ./dataset
        filename = self.stock_code.replace('.', '_')
        current_dir = os.getcwd()
        try:
            os.mkdir(current_dir + '/dataset')
        except FileExistsError:
            pass
        df.to_csv(current_dir + '/' + 'dataset' + '/' + filename)
        print('Ingesting stock data from code: {}'.format(self.stock_code))
        print('The ingested data saved into minotaur_trading dataset...')
        print('You can access {} dataset by importing minotaur_trading.dataset.{}'.format(self.stock_code, filename))


        self.df = df
        return df

    def set_ma(self, ma):
        self.df['ma'] = self.df['Adj Close'].rolling(window = ma).mean()
        self.df.dropna(inplace = True)
        self.ma = ma
        self.df = self.df

        return self.df

    def visualize(self, options):
        #manage subplots
        ax1 = plt.subplot2grid((6,1),
                               (0,0),
                               rowspan = 5,
                               colspan = 1)
        ax2 = plt.subplot2grid((6,1),
                               (5,0),
                               rowspan = 1,
                               colspan = 1,
                               sharex = ax1)
        
        if self.ma is None:
            plt.title('Stock code: {}'.format(self.stock_code),
                  y = 7)
        else:    
            plt.title('Stock code: {} with moving average: {}'.format(self.stock_code, self.ma),
                  y = 7)
        
        for item in options:
            if options != 'Volume':
                ax1.plot(self.df.index, 
                        self.df[item])
        ax1.legend(options)
        ax2.bar(self.df.index,
                self.df['Volume'])
        ax2.legend(['Volume'])

        plt.show()    
    


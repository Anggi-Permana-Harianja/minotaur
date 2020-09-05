import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='minotaur-trading',  
     version='1.0',
     scripts=['minotaur-trading'] ,
     author="Anggi Permana Harianja",
     author_email="permanaharianja@gmail.com",
     description="Machine Learning Platform for Trading",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Anggi-Permana-Harianja/minotaur-trading",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
     ],
 )
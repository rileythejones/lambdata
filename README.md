# lambdata_rileythejones

a collection of data science helper functions, for playing with data 
https://test.pypi.org/project/lambdata-rileythejones/0.1.7/

# documentation 

- in google colab:

```
pip install -i https://test.pypi.org/simple/ lambdata-rileythejones==0.1.7
```

- import the Class and the sample dataframes 
```
from lambdata_rileythejones import CleanData
from lambdata_rileythejones.df_utils import df_null, df_random, df_random_column
```

- CleanData(df).check_nulls() 
  - takes a dataframe and returns the total null values in the dataframe 
- CleanData(df).outlier_filter() 
  - takes a dataframe and returns the dataframe with the outlier rows filtered out , default = 2 STD
- CleanData(df).bag_tag(column) 
  - takes a column and returns a column where all the values are integer categories based on their proportional binning , default number of bins = 10


```
clean_data = CleanData(df_random)
clean_data.check_nulls()
=> 0
dirty_data = CleanData(df_null)
dirty_data.check_nulls()
=> 1

df_random.shape
=> (100, 3)

clean_data.outlier_filter().shape()
=> (86, 3)

df_category = clean_data.bag_tag(df_random_column, 7)
df_category.unique()
=> 7
```

# UNIT 3 - Sprint 1- Module 1 
_Python Modules, Packages, and Environments_

## __How to make a package__

# verify installations :
- where python
- where git
- where pip
- where conda 
- where pipenv , (pip install pipenv)

# create a new github repo:
-  git ignore : add python 
-  include README.md
-  add MIT license 
-  git clone 

# create a pipfile and pipfile lock: 
- pipenv install numpy pandas 
  - pipenv shell command should work 

# open editor from command line:  
+ code  . 
  + the pipfile and pipfile lock should be there 

# push to your repository 
- git add . 
- git commit -m "made pipfiles"  
- git push origin master 
  * git config --global user.name "GITHUBUSERNAME" (set this up once)
  * git config --global user.email "YOUREMAIL@gmail.com"

# Make a folder that will be the package name and the `__init__.py` file 
- mkdir lambdata_rileythejones
- in the folder create a new file  `__init__.py`

# now from the command line open up the python terminal 
- python
- >>> import lambdata_rileythejones
- >>> dir(lambdata_rileythejones)
- there will be contents even if it's blank 
```
['ONES', 'ZEROS', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'increment', 'np', 'pd'] 
```

# Put stuff in the `__init__.py` file 

At the top put a doc string , it automatically creates a help message
```
"""lambdata - collection of data science helper functions """

import pandas as pd 
import numpy as np 

# sample code 

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

# sample functions 

def increment(x)
    return (x + 1)
```

# import it in the python terminal 

- test out the function we just made 
```
>>>import lambdata_rileythejones 
>>>lambdata_rileythejones.increment(4)
5  
```
- test out the dataset we just made 
```
>>>lambdata_rileythejones.ONES
0
0  1.0
1  1.0
2  1.0
3  1.0
4  1.0
5  1.0
6  1.0
7  1.0
8  1.0
9  1.0
```
- make a file called df_utils.py in the lambdata_rileythejones folder 
```
"""
utility functions for working with DataFrames
"""
import pandas 
TEST_DF = pandas.DataFrame([1, 2, 3, 4, 5])
```
- sidenote to always test packages in pipenv shell terminal (go into pipenv shell where you see the pipfile)
- run the terminal with $ python 
```
>>> from lambdata_DS9 import df_utils 
>>> df_utils.TEST_DF
   0
0  1
1  2
2  3
3  4
4  5
```

-__the folder that you do pipenv stuff in is one where you can see the pipfile, pipfile.lock, readme.md, LICENSE etc..__
# install twine 
- pipenv install -d twine 

# make the setup file 
- call it setup.py 
```
"""
lambdata - a collection of data science helper functions for lambda school
"""
import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="lambdata-DS9",
    version = "0.1.1",
    author = "alekslovesdata",
    description = "a collection of data science helper functions",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://lambdaschool.com/courses/data-science",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires = REQUIRED,
    classifiers=["Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
    )
```

# building the package 
-  python setup.py sdist bdist_wheel 
- to remove it : rm /dist*
- change version number and name if needed. 



- twine upload --repository-url https://test.pypi.org/legacy/ dist/*

- now you can pip install your package wherever you want 





-when you type pipenv make sure when you type ls you see the license
pipenv install -d twine 
this will change the pipfile  



-make sure to change the name in the setup file and the version number if changes are made 

-you must delete the dist folder if you make changes to the package. 


-if you do "git status" 
it will not add certain files because of the gitignore file  


you need to create a test pipy account to upload the package 

it's a great way to share functions with people

goal for tonight reproduce everything we did in class and put some actual useful functions in it 



pypi 
pip install ....
dir()

import lambdata 
# you can put datasets and function into it 




# UNIT 3 - Sprint 1- Module 2 

_Object-Oriented Programming, Code Style and Reviews_

- Windows version of Lecture
[![Windows version of Lecture](http://img.youtube.com/vi/v2uOwVpyAD4/0.jpg)](https://www.youtube.com/watch?v=v2uOwVpyAD4&feature=youtu.be)


### random prenotes 
- launching pipenv in the right environment is important 
- grouping functions in init, and dataframes is df_utils is smart
- although we could put all the majors functions in a file called df_functions

- in a lot of jobs code is written much more often than it's written. 
- DON'T REPEAT YOURSELF
- create minimal technical debt" for others to deal with 

- functional is a series of steps do this do that 
- object oriented is more of a prepackaged containers 
- subclasses inherited from the parent class 
- for a subclass you put the parent class in the parentheses
-------

- use dir(Class) to show its attributes 
- game instance , Game class
- instance is an object 
- self represents an instance of the class, so you can change attributes
- the reason to use inheritance is to use less code, to not repeat yourself
- DRYourselfs
-  to use inheritance 
- a field is a variable declared inside a class 
- the constructor is the init 
- >>>`from oop_example import Game`
- adding the init line lets you change the methods 
-  super is the way to override init 
```   
 def __init__(self, rounds=3, player1='Superman', player2='Stephanie'):
        super().__init__(rounds, player1, player2)
```

- pip install pycodestyle 
-  pycodestyle oop_example.py
- pip install autopep8==0.8
- autopep8 --in-place NAME_OF_FILE.py
- https://avilpage.com/2015/05/automatically-pep8-your-python-code.html
- pep8online.com 
- you can install a linter into your text editor that highlights grammtical errors as you are typing 

- zoom call with jarret grande tonight, give two positive comments for each negative, talk about style and flow, 



# UNIT 3 - Sprint 1- Module 3 

_Containers and Reproducible Builds_



- images are the templates of docker technology
- containers are the instances of the template 
-  docker command prompt from https://training.play-with-docker.com/ops-s1-images/
- $ docker 
- $ docker run hello-world
- $ docker container ls -a 
- $ docker image ls 
-  container is an shipping container
-  image is the template 
-  to clean up the containers
-  $ docker container prune 
- which apk
- apk add nano
- which nano 
- nano
- opens up nano, make a file and save it 
-  docker run -it debian /bin/bash
-  now we are in a different working directory 
-  pwd 
-----
- mkdir container mkdir lambdata cd cd 
- nano dockerfile 

# putting lambdata on docker 
- typical dockerfile has environmental variables and packages 
- docker build . -t lambdata 
- you need to be in the directory with the dockerfile 
- docker run -it lambdata /bin/bash
- python3
- >>>import lambdata_rileythejones as lambdata
- >>>from lambdata_rileythejones import df_utils
- >>> df_utils.df_random


- nano Dockerfile 


- https://github.com/Zebfred/DS-OOP-Review/tree/master/football
- docker is import for deploying to scale 
- put dockerfile inside the host not the container 




- or windows follow along mostly with this tutorial:    https://docs.docker.com/toolbox/toolbox_install_windows/
- First check if you machine has virtualization running.
- Go into task manager, and under 'performance' look at your cpu, then look for virtualization. 
- If that's 'Enabled' you're fine, if not:
Restart and enter your BIOS. Under Advanced search for options with your CPU for 'virtualization'. If you're having trouble, google for what your motherboard manufacture calls it because every one of them does it differently.
Save settings and exit. When you're back in windows, check your task manager as before to confirm.
- Next, download the latest release:    https://github.com/docker/toolbox/releases
Once it's installed, open CMD, NOT WHAT THE TUTORIAL SAYS.
You need to type in this command:
`docker-machine create default --virtualbox-no-vtx-check`

From here docker is now installed on your computer much like python. (edited) 
https://github.com/docker/machine/issues/4271







-docker is used to create reproducible builds, it's a small size, scales well to deploy to many people, 










- Windows version of Lecture
[![Windows version of Lecture](http://img.youtube.com/vi/Q4EoR2mUQtc/0.jpg)](https://www.youtube.com/watch?v=Q4EoR2mUQtc&feature=youtu.be)

# useful links today:
- https://training.play-with-docker.com/ops-s1-hello/
- https://github.com/ageron/handson-ml/blob/master/docker/Dockerfile
- docker for windows: https://docs.docker.com/toolbox/toolbox_install_windows/
- docker for linux: https://runnable.com/docker/install-docker-on-linux
# code for today about DOCKER!!
```
docker
docker COMMAND --help #opens help files about commands
docker create --help
docker run hello-world #runs a sample container with some text
docker container ls -a #gives all containers
docker image ls #shows all images
docker container prune #deletes all containers
which apk #checks for having access to apk
apk add nano #adds nano text editor
nano
docker run -it debian /bin/bash
nano Dockerfile
```
# make Dockerfile
```
docker build . -t lambdata #this builds the image for lambdata
docker run -it lambdata /bin/bash #this uses the image to create a container
```
# ONCE YOU'RE IN THE PYTHON SHELL (which you access with the command python3)
```
import lambdata_soycode as lambdata
```
dir(lambdata)
lambdata.TEST

~~~
Dockerfile:
FROM debian
### *Minimal* Python container
### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### Basic Python dev dependencies
RUN apt-get update && \
 apt-get upgrade -y && \
 apt-get install python3-pip curl nano -y && \
 pip3 install pandas && \
 pip3 install -i https://test.pypi.org/simple/ lambdata-soycode && \
 python3 -c "import lambdata_soycode; print('Success!')"
 ~~~


 # UNIT 3 - Sprint 1- Module 4 

_Software Testing, Documentation, and Licensing_


- write basic unit tests
- make documentation 
- work with licenses 
- contributing to open source projects can help get you a job 
- writing unit tests can be dull but important contribution 
- scikit learn, pandas 
---------------
- sqrt.py
```
def newton_sqrt1(x):
    """Return the square root of x using Newton's Method."""
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

def newton_sqrt2(x, guess=2):
    """Danger! Something's not quite right..."""
    from numpy.testing import assert_almost_equal as eq
    if eq(newton_sqrt2(x, guess)**2, x):
        return guess
    else:
        guess = 0.5*(guess+x)
        return newton_sqrt2(x, guess)

def lazy_sqrt(x):
    return x**0.5

def builtin_sqrt(x):
    from math import sqrt
    return sqrt(x)
```
- sqrt_test.py
```
#import the unit test package and functions we want to test out
import unittest
from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt

class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square root functions!"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(lazy_sqrt(2), 1.41421356)

if __name__ == '__main__':
    unittest.main()
```
- b.py
```
print("Hello World from %s!" % __name__)

if __name__ == '__main__':
    print("Hello World again from %s!" % __name__)


#now in terminal run:
#python a.py
#python b.py
```
- a.py
```
import b 
```


- pip install pytest
-  $ pytest
-  this will run every test it can find in that folder
- pytest -v
-  verbose setting 
- pytest --collect-only 

- there's a package called hypothesis that will automatically test for edgecases 
- pip install hypothesis
-  there's another package for pandas dataframes called onguard 
-  use the docstrings at the top of the file and top of the methods 
-  for yourself and others 
- how to clear terminal in windows????

# Licenses 
- https://exygy.com/which-license-should-i-use-mit-vs-apache-vs-gpl/
- why use them
-  they protect your from liability in case of a HIPPA violation etc...

- Spruce up lambdata!

Add at least one basic unittest to lambdata
Make sure there are docstrings wherever PEP 8 demands
Write a high-quality README.md that is both skimmable and has appropriate examples/details/links for someone who wants to understand your code
Pick a license for your package, and add it in a LICENSE file.
















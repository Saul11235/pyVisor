#  script for local install

from os import system

system("pip install setuptools")
system("pip install wheel")
system("pip install twine")

system("python setup.py sdist bdist_wheel")

system("twine upload dist/*")




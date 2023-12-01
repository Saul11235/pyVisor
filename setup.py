from setuptools import setup, find_packages

f=open("README.md","r")
readme_file=f.read()
f.close()

setup(
    name='pyVisor',         
    version='1.0.0', 
    description='package for simple exploring of python objects',
    author='Edwin Saul',
    author_email='edwinsaulpm@gmail.com',
    url="https://edwinsaul.com"
    packages=find_packages(),  # Automatically discover and include all packages
    keywords='DEV debug flask',
    install_requires=[
        "flask"
    ],
    long_description=readme_file,
    long_description_content_type="text/markdown",

)

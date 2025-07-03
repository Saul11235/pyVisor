from setuptools import setup, find_packages

f=open("README.md","r")
readme_file=f.read()
f.close()

setup(
    name='pyVisor',         
    version='1.1.0', 
    description='package for simple exploring of python objects',
    author='Edwin Saul',
    author_email='edwinsaul@proton.me',
    url="https://edwinsaul.com/index.html?p=pyVisor",
    packages=find_packages(),  # Automatically discover and include all packages
    keywords='DEV debug flask',
    install_requires=[
        "flask"
    ],
    long_description=readme_file,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'pyVisor= pyVisor.pyVisorCLI:main',
        ],
    },

)

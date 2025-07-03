# pyVisor

![LogoPyVisor](https://raw.githubusercontent.com/Saul11235/pyVisor/refs/heads/master/logo.svg)

[![view on github](https://img.shields.io/badge/-view_on_github-blue)](https://github.com/Saul11235/pyVisor)
[![test examples](https://img.shields.io/badge/-test_examples-green)](https://github.com/Saul11235/pyVisor/tree/master/test)
[![view on PyPI](https://img.shields.io/badge/-view_on_PyPI-red)](https://pypi.org/project/pyVisor/)


pyVisor is a package - webAplication writed in flask to
view the content of a python object

## How to install 

- *recomended:* : <code>pip install pyVisor</code>


## How does it work?

Detects a Python object and launches a web application 
to browse and view its contents, pyVisor requires Flask

## How to use

in python scripting:
<pre>
from pyVisor import visor
import tkinter

v=visor(tkinter,"tkinter")
v.run()
</pre>

pyVisor as an CLI application:
<pre>
pyVisor tkinter
</pre>
<pre>
pyVisor from os.path import readme
</pre>

use Ctrl+C to end.

## Credits

[![Edwin Saul](https://img.shields.io/badge/-Writed_by_Edwin_Saul-black)](https://edwinsaul.com)


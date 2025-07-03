try   :  from .__init__ import visor
except:  from __init__  import visor

from sys       import  argv
from importlib import  import_module

def get_sys_args():
    # sys.argv[1:] excluye el nombre del script (argv[0])
    return [arg.strip() for arg in argv[1:] if arg.strip()]

#---------------------------

def print_message():
    print("""
 pyVisor by EdwinSaul (https://edwinsaul.com)
 View the content of a python object or module in a web app.
 +---------------------------------------+
 | pyVisor myModule                      |
 | pyVisor from myModule import myObject |
 +---------------------------------------+
 example: pyVisor tkinter
          pyvisor from os.path import listdir
 Use ctrl+C to end.
""")
    quit()

#---------------------------

def print_not_found():
    print(f"""
 Error, module not found  :(
          """)
    quit()

#---------------------------

def print_error_syntax():
    print(f"""
 Error, invalid syntax, valid examples

 pyVisor tkinter
 pyVisor os.path
 pyVisor tkinter as tk
 pyVisor import math
 pyVisor import tkinter as tk
 pyvisor from math import sin
 pyvisor from math import sin as ss
 pyVisor from os.path import listdir
 pyVisor from os.path import listdir as ls
          """)
    quit()

#---------------------------


def sort_args(args):
    response=[]
    if   len(args)==0:  # nothing
        pass
    elif len(args)==1:  # nameModule
        for x in args[0].split("."): response.append(x)
    elif len(args)==2:  # import nameModule
        if args[0]=="import":
            for x in args[1].split("."): response.append(x)
    elif len(args)==3:  # object as alias
        if args[1]=="as":
            for x in args[0].split("."): response.append(x)
    elif len(args)==4:  # from module import object / import module as alias
        if args[0]=="from" and args[2]=="import":
            for x in args[1].split("."): response.append(x)
            for x in args[3].split("."): response.append(x)
        if args[0]=="import" and args[2]=="as":
            for x in args[1].split("."): response.append(x)
    elif len(args)==6:  # from module import object as alias
        if args[0]=="from" and args[2]=="import" and args[4]=="as":
            for x in args[1].split("."): response.append(x)
            for x in args[3].split("."): response.append(x)
    return response
 
#---------------------------

def get_alias(args):
    response=""
    if "as" in args and len(args)==3:  # object as alias
        if args[1]=="as" : response=args[2]
    if "as" in args and len(args)==4:  # import module as alias
        if args[0]=="import" and args[2]=="as": response=args[3]
    if "as" in args and len(args)==6:  # from module import object as alias
        if args[0]=="from" and args[2]=="import" and args[4]=="as": response=args[5]
    if response=="": return ".".join(sort_args(args))
    else:            return response

#---------------------------

def get_object(args):
    "return a list [object,bool] True if ok, False if not"
    sorted_args=sort_args(args)
    # if sorted args     -----------
    if   len(sorted_args)==0:
        print_error_syntax()
    # if a single module -----------
    elif len(sorted_args)==1:
        try:
            # importacion 
            module = import_module(sorted_args[0])
            return [module, True]
        except:
            try:
                module = eval(sorted_args[0])
                return [module, True]
            except:
                return [None,   False]
    else: # an object in an package
        try:
            # get name package
            module_name=".".join(list(sorted_args[:-1]))
            object_name=sorted_args[-1]
            # get obj 
            module = import_module(module_name)
            return [getattr(module,object_name),True]
        except: return [None,  False]

#---------------------------
def main():
    "CLI command for use pyVisor"
    args=get_sys_args()
    # no arguments
    if len(args)==0        : print_message()
    # sorting args
    sorted_args = sort_args(args)
    if len(sorted_args)==0 : print_error_syntax()
    # get objects
    alias_obj   = get_alias  (args)
    python_obj  = get_object (args)
    # run pyvisor  web app
    if python_obj[1]:
        v=visor(python_obj[0],alias_obj)
        v.run()
    else:
        print_not_found()


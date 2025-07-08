try   :  from .__init__ import visor
except:  from __init__  import visor

from sys            import  argv
from shlex          import  split
from importlib      import  import_module

from os.path        import  isfile,isdir,join,basename

from importlib.util import  spec_from_file_location,module_from_spec


def get_sys_args():
    # sys.argv[1:] excluye el nombre del script (argv[0])
    full_string  = ' '.join(argv[1:])
    response     = []
    counter_str  = ""
    in_str       = False
    type_str     = 1     # 1 -> ""  2-> ''
    # ---------------
    def add_to_response():
        nonlocal response, in_str, counter_str
        if in_str:
            response.append(counter_str[:])
            counter_str="" 
        else:
            for x in counter_str.split(" "):
                if len(x) and x!=" ": response.append(x)
            counter_str=""
    # ---------------
    for x in full_string:
        if in_str:
            if   x=='"' and type_str==1:
                add_to_response()
                in_str = False
            elif x=='"' and type_str==2:
                add_to_response()
                in_str = False
            else:
                counter_str+=x
        else:
            if   x=='"':   # begin str
                add_to_response()
                in_str   = True
                type_str = 1
            elif x=="'":   # begin str
                add_to_response()
                in_str   = True
                type_str = 2
            else:
                counter_str+=x
    # ---------------
    add_to_response()
    return response

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

 pyVisor ./my_sript.py
 pyVisor ./my_package

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

def is_local_content(args):
    "Return True or False if is an script.py or package"
    if len(args)!=1:
        return False
    elif isfile(str(args[0])) and (str(args[0]).endswith(".py") or str(args[0]).endswith(".pyw") ):
        return True
    elif isdir(str(args[0])):
        if isfile(join(str(args[0]),"__init__.py")):
              return True
        else: return False
    else:     return False

#---------------------------

def sort_args(args):
    if is_local_content(args): return args
    # ---------------
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
    "return an string with the literal name of the obj"
    # ---------------
    if is_local_content(args):
        try     : 
            alias = basename(args[0]).split(".")
            if len(alias)==0: alias.append("")
            alias = alias[:-1]
            alias = "".join(alias)
            if alias == "": return "module"
            else          : return alias
        except  : return str(args[0]).replace("/","").replace("\\","")
    # ---------------
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
    # ---------------
    if is_local_content(args):
        try:
            path=args[0]
            if isdir(path):path=join(path,"__init__.py")
            spec   = spec_from_file_location(get_alias(args), path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return [module,True]
        except:
            return [None,False]
    # ---------------
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
    # test Mode  
    testMode = False# <--- to enable test mode
    # run TestMode
    args=get_sys_args()
    # test Mode args
    if testMode:print('----------------------------')
    if testMode:print('args       : ',args)
    # no arguments
    if len(args)==0        : print_message()
    # sorting args
    sorted_args = sort_args(args)
    # test Mode sorted_args
    if testMode:print('----------------------------')
    if testMode:print('sort_args  : ',sorted_args)
    if len(sorted_args)==0 : print_error_syntax()
    # get objects
    alias_obj   = get_alias  (args)
    python_obj  = get_object (args)
    # test Mode sorted_args
    if testMode:print('----------------------------')
    if testMode:print('alias_obj  : ',alias_obj)
    if testMode:print('----------------------------')
    if testMode:print('python_obj : ',python_obj)
    if testMode:print('----------------------------')
    # run pyvisor  web app
    if python_obj[1] and not(testMode):
        v=visor(python_obj[0],alias_obj)
        v.run()
    else:
        print_not_found()

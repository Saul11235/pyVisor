# geto obj by Edwin saul

class getObj:

    def __init__(self,obj,name):
        """this class explore and determine the subobjects in
        an python obj, known the array for the subobj
        for example:

        import tkinter

        obj->tkinter,  name->"tkinter"

        from tkinter.Tk import Label
        array = ["tkinter","Tk","Label"]
        """
        self.obj=obj
        self.name=name

    #----------------------------------------------

    def inipath(self): 
        """return initial path ["initial"]"""
        return [self.name]

    #----------------------------------------------

    def get(self,array):
        """self.get(array)
        returns {bool,obj}

        bool   True    if the object exists
        bool   False   if the objext does not exists

        obj is the object
        array is an list: array=["first","second","third"...]"""
        if len(array)==0: return self.get(self.inipath())
        elif len(array)==1 and array==[self.name]: return [True,self.obj]
        elif len(array)==1 and array!=[self.name]: return [False,None]
        elif array[0]!=self.name:  return [False,self.obj]
        elif array[0]==self.name: 
            #------------------
            array=array[1:]
            subobj=self.obj
            exists=True
            #-------------------
            for element in array:
                if exists:
                    exists=False
                    try: 
                        subobj=getattr(subobj,element)
                        exists=True
                    except: pass
            # return object
            if not(exists): subobj=None
            return [exists,subobj]
        
    #----------------------------------------------

    def down(self,array):
        """elements contained in the array object defined
        format dict {nameObject, array} """
        data=self.get(array)
        if data[0]:
            dic={}
            for element in dir(data[1]):dic[element]=array+[element]
            return dic
        else: return {}

    #----------------------------------------------

    def up(self,array):
        """elements in the parent conatiner array in
        format dict {nameObject, array} """
        if len(array)>1:
            array.pop()
            data=self.get(array)
            #--------
            if data[0]:
                dic={}
                for element in dir(data[1]):dic[element]=array+[element]
                return dic
            else: return {}
            #--------
        else: return {}
 
    #----------------------------------------------


if __name__=="__main__":

    import tkinter
    a=getObj(tkinter,"tkinter")

    print("----------------")
    print(a.get([]))
    print(a.get(["tkinter"]))
    print(a.get(["tkinter","Tk"]))
    print(a.get(["tkinter","Tk","config"]))
    print(a.get(["lolo"]))
    print(a.get(["tkinter","lolo"]))
    print(a.get(["tkinter","Tk","lolo"]))

    print("----------------")
    print(a.down(["tkinter","Tk","config"]))
    print(a.down(["tkinter","Tk","lolo"]))

    print("----------------")
    print(a.up(["tkinter"]))
    print(a.up(["tkinter","Tk","config"]))
    print(a.up(["tkinter","Tk","lolo"]))

    print("----------------")
    print("test finished...")


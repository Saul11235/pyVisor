# getObj by Edwin saul

#-----------------------
def is_private(name):
    if len(name)==0:return False
    elif name[0]=="_": return True
    else: return False

#-----------------------
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
            narray=array[::]
            narray.pop()
            data=self.get(narray)
            #--------
            if data[0]:
                dic={}
                for element in dir(data[1]):dic[element]=narray+[element]
                return dic
            else: return {}
            #--------
        else: return {}
 
    #----------------------------------------------
    def getStrContent(self,array):
        "return string content known array"
        data=self.get(array)
        try: return str(data[1])
        except: return ""

    #----------------------------------------------
    def getStrType(self,array):
        "return string type known array"
        data=self.get(array)
        try: return str(type(data[1])).replace("'>","").replace("<class '","")
        except: return ""

    #----------------------------------------------
    def getStrDoc(self,array):
        "return string doc known array"
        data=self.get(array)
        try: return str(data[1].__doc__)
        except: return ""

    #----------------------------------------------
    def getStrCount(self,array):
        "return string count number of public and private subobjects"
        data=self.down(array).keys()
        public=0;private=0
        for elem in data:
            if is_private(elem): private+=1
            else: public+=1
        return str(public+private)+" (pub:"+str(public)+" priv:"+str(private)+")"





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


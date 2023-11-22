# pyVisor by Edwin Saul Pareja

from flask import Flask
import webbrowser 

try:    from .getObj import getObj
except: from getObj  import getObj

try:    from .viewContent  import viewContent
except: from viewContent   import viewContent

try:    from .viewVoid     import viewVoid
except: from viewVoid      import viewVoid

class visor:

    def __init__(self,obj,name):
        """creating class visor
        obj   - object
        name  - "name of object" string
        example:
        import tkinter
        obj - tkinter,  name="tkiner" """
        self.obj=getObj(obj,name)
        self.app=Flask(__name__)
        #--------config path-------------
        @self.app.route("/")
        def blank():
            array=self.obj.inipath()
            data=self.obj.get(array)
            up=self.obj.up(array)
            down=self.obj.down(array)
            #---return
            return viewContent(data[1],array,up,down)

        #--------customg path-------------
        @self.app.route("/<path:custom_path>")
        def path(custom_path):
            array=custom_path.split("/")
            data=self.obj.get(array)
            #-----------------------------
            if data[0]==True:
                up=self.obj.up(array)
                down=self.obj.down(array)
                # content
                return viewContent(data[1],array,up,down)
            #-------------------------
            else:
                return viewVoid()

    #----------------------------------------------

    def run(self,port=8000,debug=False):
        """open webbrowser and open flask server
        port=8000 default
        debug=False (default)"""
        webbrowser.open("http://localhost:"+str(port))
        self.app.run(host="0.0.0.0",port=str(int(port)),debug=bool(debug))
        exit()

    #----------------------------------------------

if __name__=="__main__":

    import tkinter
    v=visor(tkinter,"tkinter")
    v.run()
    print("----------------")
    print("test finished...")


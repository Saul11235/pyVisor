# viewContent


try   :  from .render import render
except:  from render  import render



class viewVoid:

    def __init__(self):
        "create an 404 error page"
        self.page=render()
        self.__make()


    def __make(self):
        w=self.page.set #
        #--------------------
        w("<div id='container'>")
        w("<h1> info not found </h1>")
        w("<a href='/'>back to home</a>")
        w("</div>")  #end container

    def get(self):
        "get html code of view page"
        return self.page.get()



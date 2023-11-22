# viewContent

try   :  from .render import render
except:  from render  import render

def get_url(array):
    "get /url/format from ['url','format']"
    text=""
    for element in array: text=text+"/"+str(element)
    return text



class viewContent:

    def __init__(self,obj,array,up,down,getObj):
        "create an html page to view an object"
        self.obj=obj
        self.array=array
        self.up=up
        self.down=down
        self.getObj=getObj
        #---------------
        self.page=render() #creating render page
        self.__make()


    def __make(self):
        w=self.page.set # for  easy config
        #---------------

        w("<div id='container'>")
        w("<h1>"+str(self.array)+"</h1>")
        if len(self.array)>1: w("<a href='/'>back to home</a>")
        w("<p>")
        w("<ul>")
        for elem in self.down.keys():
            w("<li>")
            w("<a href='"+get_url(self.down[elem])+"'>"+elem+"</a>")
            w("</li>")

        w("</ul>")
        w("</p>")

        w("</div>")  #end container


    def get(self):
        "get html code of view page"
        return self.page.get()



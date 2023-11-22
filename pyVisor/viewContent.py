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

        pass

    def __make(self):
        w=self.page.set # for  easy config
        #---------------

        w("<div id='container'>")

        self.__navigatorArray()
        # back to home--------
        if len(self.array)>1: w("<a href='/'>back to home</a>")
        #---------------------

        # content -----------
        w("<p>")

        content=""
        try: content=str(self.obj).replace("<","&lt").replace(">","&gt").replace("\n","<br>")
        except: pass
        if content!="":
            w("<h2>Content</h2>")
            w(content)

        typ=""
        try: typ=str(type(self.obj)).replace("<","&lt").replace(">","&gt")
        except:pass
        if typ!="":
            w("<h2>Type</h2>")
            w(typ)

        doc=""
        try: doc=str(self.obj.__doc__).replace("<","&lt").replace(">","&gt").replace("\n","<br>")
        except: pass
        if doc!="":
            w("<h2>Doc</h2>")
            w(doc)

        w("</p>") #End content



        w("<p>")
        w("<ul>")
        for elem in self.down.keys():
            w("<li>")
            w("<a href='"+get_url(self.down[elem])+"'>"+elem+"</a>")
            w("</li>")

        w("</ul>")
        w("</p>")

        w("</div>")  #end container


    def __navigatorArray(self):
        # define navigation header
        buttons=[]
        acumulator=[]
        for element in self.array:
            acumulator.append(element)
            buttons.append("<a href='"+get_url(acumulator)+"'>"+element+"</a>")
        self.page.set("<h1 id='navigation'>"+str(".".join(buttons))+"</h1>")


    def get(self):
        "get html code of view page"
        return self.page.get()



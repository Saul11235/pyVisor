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
        self.page.title(array[len(array)-1]) #title
        self.__make()
        #---------------

    def __make(self):
        w=self.page.set        # for  easy config
        ww=self.page.setFormat
        #---------------
        w("<div id='container'>") # begin container --------------------------
        #-------
        self.__navigatorArray()
        self.__typeNavigation()
        self.__contenObj() #table of contents

        w("<p>") # begin SubObjects
        w("<h3>SubObjects</h3>")
        w("<ul>")
        for elem in self.down.keys():
            w("<li>")
            w("<a href='"+get_url(self.down[elem])+"'>"+elem+"</a>")
            w("</li>")

        w("</ul>")
        w("</p>") # ende SubObjects

        w("</div>")  #end container #---------------------------------------


    def __navigatorArray(self):
        # define navigation header
        buttons=[]
        acumulator=[]
        for element in self.array:
            acumulator.append(element)
            buttons.append("<a href='"+get_url(acumulator)+"'>"+element+"</a>")
        self.page.set("<h1 id='navigation'>"+str(".".join(buttons))+"</h1>")

    def __typeNavigation(self):
        # define type navigation barr
        print(self.array)
        if len(self.array)>1: 
            self.page.set("<p>  <table id='navtype'> <tr>  <td> <a href='/'>home</a> </td> <td>")
            self.page.set(self.array)
            self.page.set("</td> ")
            self.page.set("</tr> </table>  <p>")
        #---------------------------------

    def __contenObj(self):
        # define table showing content
        self.page.set("<table id='tcontent'> <tbody>") # begin  table -----------
        content=""
        try: content=str(self.obj)
        except: pass
        if content!="":
            self.page.set("<tr> <td class='graybg'>Content</td> <td class='whitebg'>")
            self.page.setFormat(content)
            self.page.set("</td> </tr>")
        typ=""
        try: typ=str(type(self.obj))
        except:pass
        if typ!="":
            self.page.set("<tr> <td class='graybg'>Type</td>  <td class='whitebg'>")
            self.page.setFormat(typ)
            self.page.set("</td> </tr>")
        doc=""
        try: doc=str(self.obj.__doc__)
        except: pass
        if doc!="":
            self.page.set("<tr> <td class='graybg'>Doc</td> <td class='whitebg'>")
            self.page.setFormat(doc)
            self.page.set("</td> </tr>")
        self.page.set("</tbody></table>") # end table ----------------





    def get(self):
        "get html code of view page"
        return self.page.get()



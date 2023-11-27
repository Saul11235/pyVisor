# viewContent

try   :  from .render import render
except:  from render  import render

#-------------------------------------
def get_url(array):
    "get /url/format from ['url','format']"
    text=""
    for element in array: text=text+"/"+str(element)
    return text

#-------------------------------------
def cut(num,element):
    if len(element)<=num: return element
    else: return element[0:num-3]+"..."

#-------------------------------------
def is_private(name):
    if len(name)==0:return False
    elif name[0]=="_": return True
    else: return False

#-------------------------------------
class viewContent:

    def __init__(self,obj,array,up,down,getObj):
        "create an html page to view an object"
        self.obj=obj
        self.array=array
        self.up=up
        self.down=down
        self.getObj=getObj
        self.basicTypes=["int","float","dict","list","tuple","str","bool"]
        self.__initVarExists=False
        try:down["__init__"]; self.__initVarExists=True
        except:pass
        #---------------
        self.page=render() #creating render page
        self.page.title(array[len(array)-1]) #title
        self.__make()
        #---------------

    #------------------------------------------------------
    def __make(self):
        w=self.page.set        # for  easy config
        ww=self.page.setFormat
        #---------------
        w("<div id='container'>") # begin container --------------------------
        #-------
        self.__navigatorArray()  # Header
        self.__typeNavigation()  # navigator by type
        self.__contenObj()       # table of contents
        self.__subobjects()      # table of subchilds

        w("</div>")  #end container #---------------------------------------


    #------------------------------------------------------
    def __navigatorArray(self):
        # define navigation header
        buttons=[]
        acumulator=[]
        for element in self.array:
            acumulator.append(element)
            buttons.append("<a href='"+get_url(acumulator)+"'>"+element+"</a>")
        self.page.set("<h1 id='navigation'>"+str(".".join(buttons))+"</h1>")

    #------------------------------------------------------
    def __typeNavigation(self):
        # define type navigation barr
        print(self.array)
        if len(self.array)>1: 
            self.page.set("<p id='navtypecontent'>")
            npath=[]
            for element in self.array:
                npath.append(element)
                #creating new button on type nav bar -------
                self.page.set("<a class='navtype' href='"+get_url(npath)+"'>")
                self.page.setFormat(self.getObj.getStrType(npath))
                self.page.set("</a>")
                #------------------------------------------
            self.page.set("</p>")
        #---------------------------------

    #------------------------------------------------------
    def __contenObj(self):
        # define table showing content
        self.page.set("<table id='tcontent'> <tbody>") # begin  table -----------
        #--content---
        self.page.set("<tr> <td class='graybg'>Content</td> <td class='whitebg'>")
        self.page.setFormat(self.getObj.getStrContent(self.array))
        self.page.set("</td> </tr>")
        #-type--------
        self.page.set("<tr> <td class='graybg'>Type</td>  <td class='whitebg'>")
        self.page.setFormat(self.getObj.getStrType(self.array))
        self.page.set("</td> </tr>")
        #-doc---------
        self.page.set("<tr> <td class='graybg'>Doc</td> <td class='whitebg'>")
        self.page.setFormat(self.getObj.getStrDoc(self.array)) 
        self.page.set("</td> </tr>")
        #-count--------
        self.page.set("<tr> <td class='graybg'>Count</td> <td class='whitebg'>")
        self.page.setFormat(self.getObj.getStrCount(self.array)) 
        self.page.set("</td> </tr>")
        #-__init__-----
        if self.__initVarExists:
            self.page.set("<tr> <td class='graybg'>__init__</td> <td class='whitebg'>")
            self.page.setFormat(self.getObj.getStrDoc(self.array+["__init__"])) 
            self.page.set("</td> </tr>")
        #-signature-----
        signature=self.getObj.getStrSignature(self.array)
        if signature!="":
            self.page.set("<tr> <td class='graybg'>signature</td> <td class='whitebg'>")
            self.page.setFormat(signature)
            self.page.set("</td> </tr>")
        #-----------------
        self.page.set("</tbody></table>") # end table ----------------


    def __get_sort_child_list(self):
        initialList= list(self.down.keys())
        public=[];private=[]
        for element in initialList:
            if is_private(element): private.append(element)
            else: public.append(element)
        return self.__sort_by_type(public)+self.__sort_by_type(private)


    def __sort_by_type(self,array):
        complex_vars=[]; basic_vars=[]
        for element in array:
            fullArray=self.array+[element]
            typeOnArray=self.getObj.getStrType(fullArray)
            if typeOnArray in self.basicTypes: basic_vars.append(element)
            else:complex_vars.append(element)
        return complex_vars+basic_vars


    def __subobjects(self):
        w=self.page.set
        ww=self.page.setFormat
        w("<h3>SubObjects</h3>")
        w("<table class='tableContent'>  <thead> <tr>")
        w("<th> SubObject </th>")
        w("<th> type      </th>")
        w("<th> Content   </th>")
        w("<th> Doc       </th>")
        w("<th> Count     </th>")
        w("</tr> </thead>")
        w("<tbody>")
        for elem in self.__get_sort_child_list():
            w("<tr>") #-inicio-------------------------
            subArray=self.down[elem]

            w("<td>")
            w("<a href='"+get_url(subArray)+"'>")
            ww(elem)
            w("</a>")
            w("</td>")

            w("<td>")
            ww(cut(10,self.getObj.getStrType(subArray)))
            w("</td>")

            w("<td>")
            ww(cut(30,self.getObj.getStrContent(subArray)))
            w("</td>")

            w("<td>")
            ww(cut(30,self.getObj.getStrDoc(subArray)))
            w("</td>")


            w("<td>")
            ww(cut(20,self.getObj.getStrCount(subArray)))
            w("</td>")



            w("</tr>") # fin item ----------------------

        w("</tbody> </table>") #------------------------







    def get(self):
        "get html code of view page"
        return self.page.get()



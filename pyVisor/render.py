# render by Edwin Saul

try:    from .getHtmlObjects  import getjs,getcss
except: from getHtmlObjects   import getjs,getcss

#-----------------------------------------------------    
header="<!doctype html>\n<html>\n<head>\n<meta charset=\"utf-8\"/>\n<title>"
body="</title>\n</head>\n<body>"
endbody="\n</body>\n</html>"
#-----------------------------------------------------    

class render:

    def __init__(self):
        "create object to render an html page"
        self.__name="title"
        self.__content=""
        self.set("<script>"+getjs()+"</script>")
        self.set("<style>"+getcss()+"</style>")
        
    def title(self,title):
        "add an title to the html page"
        self.__name=str(title)

    def set(self,string):
        "add an line to the html page"
        self.__content=self.__content+"\n"+str(string)

    def setFormat(self,string):
        "add line an add an format text to read in html"
        self.set(string.replace("<","&lt").replace(">","&gt").replace("\n","<br>").replace("\t","&nbsp;"))

    def get(self):
        "get all html code"
        text=header+self.__name+body+self.__content+endbody
        return text

#-------------------------------------------------
if __name__=="__main__":
    a=render()
    a.title("example")
    a.set("<h1>hello world</h1>")
    a.set("<p>lorem ipsum</p>")
    print(a.get())


# script make getHtmlObjects.py  

print("html obj")

css=open("pyVisor/custom.css","r")
js =open("pyVisor/custom.js","r")
py =open("pyVisor/getHtmlObjects.py","w")

py.write("#this file is autogenerated no write manually\n")
py.write('def getcss(): return """')
py.write(css.read()+ '"""\n')
py.write('def getjs(): return """')
py.write(js.read())
py.write('"""')


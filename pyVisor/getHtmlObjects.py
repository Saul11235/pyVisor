#this file is autogenerated no write manually
def getcss(): return """/*style css ----------------------------------------*/
body {
  background-color: darkblue;
  font-family: Arial, Helvetica, sans-serif;
  font-size:  3.1ex;
}
#container {
  background-color: lightblue;
  border-radius: 20px;
  padding: 20px;
  margin: 20px;
}
/*Nagigation header -------------------------------- */
#navigation {
  color: black;
  font-weight: bold;
  text-decoration: none;
  overflow-wrap: break-word;
  word-wrap: break-word;
}
#navigation :visited {
  color: black;
}
#navigation a { 
  text-decoration: none;
}
/*type navigation bar------------------------------- */
#navtypecontent {
  line-height: 1.8;
} 
.navtype {
  font-size: 1em;
  color: white;
  text-decoration: none;
  font-weight: bold;
  background-color: black;
  margin: 4px;
  padding: 4px;
  border-radius: 4px;
}
.navtype :visited {
  color:white;
}
/*Table obj content---------------------------------- */
table {
  border-collapse: collapse;
}
#tcontent td {
  border: 2px solid black;
  border-collapse: collapse;
  font-family: monospace;
  padding: 4px;
}
#tcontent .graybg {
  background-color: lightgray;
  font-weight: bold;
}
#tcontent .whitebg {
  background-color: white ;
}
#navtype tr td {
  padding: 10px;
  margin:  10px;
  color: red;
}
/*--------------------------------------------------- */
.tableContent {
  border-collapse: collapse;
  border: 2px solid black;
}
.tableContent thead tr th {
  border: 2px solid black;
  border-collapse: collapse;
  padding: 4px;
  color: black;
  background-color: lightgray;
}
.tableContent tbody tr td {
  border: 2px solid black;
  border-collapse: collapse;
  padding: 4px;
  background-color: white ;
}
/*--------------------------------------------------- */
/*subobjext navigation slide*/
#navBarSUBOBJ1 a {
  text-decoration: none;
  font-size: 0.8em;
  font-weight: bold;
  background-color: darkblue;
  color: white;
  margin: 2px;
  padding: 2px;
}
#navBarSUBOBJ1 a:visited {
  color: white;
}
/*----------------------------------------------*/
#navBarSUBOBJ2 a {
  text-decoration: none;
  font-size: 0.8em;
  color: black;
  font-weight: bold;
}
#navBarSUBOBJ2 a:visited {
  color: black;
}

/*--------------------------------------------------- */



"""
def getjs(): return """/*script javascript*/
console.log("hello world")
"""
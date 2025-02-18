from . import quickfile
import os
import shutil
from . import postmarkup

def BBCode(inp):
    return postmarkup.render_bbcode(inp)

if os.path.exists("build"):
    shutil.rmtree("build")
os.makedirs("build/bbcode")
os.makedirs("build/html/cipher")
cipherlist=quickfile.read(open("ciphers.txt",encoding="utf-8").read())
leaderboard={}
ciphers=[]
solved=open("build/bbcode/solved.bb","w",encoding="utf-8")
current=open("build/bbcode/current.bb","w",encoding="utf-8")
index=open("build/html/cipher/index.html","w",encoding="utf-8")
index.write("<ul>")
for row,i in enumerate(cipherlist):
    out=open("build/html/cipher/"+str(row)+".html","w",encoding="utf-8")
    out.write(f"""<!DOCTYPE HTML>
<html><head><title>Can You Decode This - 50_scratch_tabs</title><link rel="stylesheet" href="../styles.css"></head>
<body>
<nav class="navbar"><h1>50_scratch_tabs</h1></nav>
<div class="main-container">
<h2>Can You Decode This?</h2><div class="container">
<h3>Cipher #{row}</h3>
  """)
    out.write('<link rel="stylesheet" href="../styles.css">Ciphertext:<div class="box">')
    out.write(BBCode(i["ciphertext"]))
    out.write("</div>")
    out.write('Creator\'s note: <div class="box">')
    out.write(BBCode(i["description"]))
    out.write("</div>")
    ciphertexttype="code"
    currententry=f'[quote][url={i["creation-link"]}]#{row}[/url] by [url=https://scratch.mit.edu/users/{i["creator"]}]@{i["creator"]}[/url][{ciphertexttype}]{i["ciphertext"]}[/{ciphertexttype}][/quote]'
    if i["solver"]=="":
        current.write(currententry)
    else:
        solved.write(currententry)
        out.write("Solved by: "+i["solver"])
        out.write('<br>Solution:<div class="box">')
        out.write(BBCode(i["solution"]))
        out.write("</div>")
        out.write('<a href="')
        out.write(i["solve-link"])
        out.write('">View Solution Post</a>')
    out.write(f"""
</div>
</div>
  <center><div style="font-style: italic;color: gray;"><a href="{i["creation-link"]}">View Cipher Source</a></div></center>
<script>
// Script here
</script>
</body>
</html>
""")
    out.close()
    index.write('<li><a href="'+str(row)+'.html">#'+str(row)+" by "+i["creator"]+"</a></li>")
index.write("</ul>")
index.close()
open("build/html/styles.css","wb").write(open("styles.css","rb").read())
solved.close()
current.close()
open("build/html/solved.html","w").write('<link rel="stylesheet" href="styles.css">'+BBCode(open("build/bbcode/solved.bb").read()))
open("build/html/current.html","w").write('<link rel="stylesheet" href="styles.css">'+BBCode(open("build/bbcode/current.bb").read()))
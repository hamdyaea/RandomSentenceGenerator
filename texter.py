#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from flask import Flask, render_template
import random
import sys

path = '/home/hamdyaea/mysite'
if path not in sys.path:
   sys.path.insert(0, path)


app = Flask(__name__)

@app.route('/')
def index():
    file = open('/home/hamdyaea/mysite/fortunes.txt').read()
    text = file.split('%')
    start = 0
    end = 434
    value = random.randint(start,end)
    msg = str(text[value])
    #return msg+str("<br><br>This is a random text generator for tests<br><br>Developer : Hamdy Abou El Anein<br>hamdy.aea@protonmail.com")
    return render_template("index.html",msg=msg)

if __name__ == '__main__':
    app.run()

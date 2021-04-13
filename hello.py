import os
import requests
from flask import Flask, render_template
app = Flask(__name__)

BE_URL=os.environ.get("SPRINGBOOT_DEMO_URL","http://mk8s.info/backend")

@app.route('/')
def hello():
    print("SPRINGBOOT_DEMO_URL:",BE_URL)
    response = requests.get(BE_URL+"/properties")
    return render_template('index.html',data=response.json())

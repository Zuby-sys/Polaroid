
from flask import Flask, render_template, request
from database import Database
import json
from pprint import pprint


upload_folder = "C:\\Users\\student\\Documents\\палоройд\\uplode_image"

app = Flask(__name__)


@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/upload", methods = ["POST"])
def get_img():
    print(request.headers)
    pprint(json.loads(request.data))
    
    return render_template (
        "upload.html",        
    )

@app.route("/postimg", methods = ["POST"])
def add_dbs():
    db=Database()
    JSON=json.loads(request.data)
    name = JSON["name"]
    url = JSON["url"]
    print(url)
    db.add_db(name,url)
    return ""



@app.route("/get",methods=['GET'])
def get_tasks():
    missy="подключение есть"
    return missy

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
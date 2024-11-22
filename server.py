from flask import Flask, render_template, request
from img_gr import get_img_from_gr
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/upload", methods = ["POST"])
def get_img():
    print(request.json)
    return render_template (
        "upload.html",        
    )

@app.route("/get",methods=['GET'])
def get_tasks():
    missy="подключение есть"
    return missy

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
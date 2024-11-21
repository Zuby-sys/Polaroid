from flask import Flask, request, render_template
from img_gr import get_img_from_gr

app = Flask(__name__)

missy="подключение есть"
@app.route("/index.html")
def index():
    return render_template("index.html") 
@app.route("/upload")
def get_img():
    img = get_img_from_gr()
    return render_template (
        "upload.html",
        title = "хз потом придумаю",
        json = img["url"]         
    )
@app.route("/get",methods=['GET'])
def get_tasks():
    return missy
if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
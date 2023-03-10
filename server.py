from flask import Flask,render_template,session
import os
import data_manager

app = Flask(__name__)
app.secret_key = "bhafiow vnkahbdsejr/"


UPLOAD_FOLDER = (
    os.getenv("UPLOAD_FOLDER") if "UPLOAD_FOLSER" in os.environ else "images" 
)
app.config["UPLOAD_FOLDER"] =UPLOAD_FOLDER

@app.route("/")
def main():
    getBooks = data_manager.get_books()
    return render_template("home.html",books=getBooks)


if __name__ == "__main__":
    app.run(debug=True)
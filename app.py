from flask import Flask
from flask import render_template
app=Flask(__name__)


users={"id":1, "name":"세인"},{"id":2, "name":"동수"},{"id":3,"name":"박형석"}

app.route("/")
def user_list():
    return render_template("index.html",users=users)


if __name__ == "__main__":
    app.run(debug=True)
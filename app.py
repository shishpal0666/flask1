from flask import Flask

app=Flask(__name__) #object of the class Flask.

@app.route("/")
def hellow_world():
    return "hellow World!" 


if __name__== "__main__":
    app.run(host="127.0.0.1",debug=True)
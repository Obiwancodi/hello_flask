from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/jedi/<firstname>/<lastname>")
def hello_person(firstname,lastname):
    return render_template('hellotemplate.html', jedi = lastname[0:3] + firstname[0:2])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World. It's really nice to meet you."

if __name__ == "__main__":
    app.run(debug=True)
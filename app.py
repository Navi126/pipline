from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello naveen Jenkins CI/CD!"

if __name__ == '__main__':
    app.run(host='192.168.224.103', port=5000)

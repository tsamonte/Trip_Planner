from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/getData', methods=['POST'])
def sendHello():
    return "Hello"

if __name__ == "__main__":
    app.run()
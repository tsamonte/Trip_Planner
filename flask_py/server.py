from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/getData', methods = ['GET'])
def sendMessage():
    arr = ['Irvine', 'West Covina', 'Los Angeles']
    print(arr)
    return json.dumps(arr)

@app.route('/testData')
def test():
    return "Hello World"

if __name__ == "__main__":
    app.run()
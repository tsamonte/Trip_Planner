from flask import Flask, render_template, jsonify
import main
import json

app = Flask(__name__)

@app.route('/getData', methods = ['GET'])
def sendMessage():
    data = main.main()
    print(data)
    return json.dumps(data)

@app.route('/testData')
def test():
    return "Hello World"

if __name__ == "__main__":
    app.run()
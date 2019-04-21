from flask import Flask, render_template, jsonify
import generatePlan
import json

app = Flask(__name__)

@app.route('/getData', methods = ['GET'])
def sendMessage():
    data = generatePlan.generatePlan("Irvine, CA 92697")
    return json.dumps(data)

@app.route('/testData')
def test():
    return "Hello World"

if __name__ == "__main__":
    app.run()
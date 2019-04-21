from flask import Flask, render_template, jsonify
import generatePlan
import json

f = open("firstaddy.txt", 'r')
firstaddy = f.readlines()
f.close()

app = Flask(__name__)


@app.route('/getData', methods = ['GET'])
def sendMessage():
    data = generatePlan.generatePlan(firstaddy)
    return json.dumps(data)

@app.route('/testData')
def test():
    return "Hello World"

if __name__ == "__main__":
    app.run()
from flask import Flask, request, jsonify
from store import Store

app = Flask(__name__)
store = Store()

@app.route("/", methods=["GET"])
def home() : 
    res = {
        "status" : "success",
        "message" : "API working"
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run()
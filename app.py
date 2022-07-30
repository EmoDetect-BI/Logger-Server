from flask import Flask, request, jsonify
from store import Store
import uuid

app = Flask(__name__)
store = Store()

@app.route("/", methods=["GET"])
def home() : 
    res = {
        "status" : "success",
        "message" : "API working"
    }
    return jsonify(res)

@app.route("/createOrg", methods=["POST"])
def createOrg() :
    body = None
    try : 
        body = request.get_json()
    except :
        return jsonify({
            "status" : "error", 
            "message" : "Invalid request"
            })
    if not body :
        return jsonify({
            "status" : "error",
            "message" : "No body"
        })
    if not "name" in body :
        return jsonify({
            "status" : "error",
            "message" : "No name"
        })
    nm = body["name"]
    if store.isOrg(nm) :
        return jsonify({
            "status" : "error",
            "message" : "Org already exists"
        })
    
    store.addOrg(nm)
    return jsonify({
        "status" : "success",
        "message" : "Org created"
    })

if __name__ == '__main__':
    app.run()
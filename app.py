from flask import Flask, request, jsonify
from store import Store
import uuid
from utils import *

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
    err, body = checkJsonAndBody(request, ["name"])
    if err : 
        return err
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
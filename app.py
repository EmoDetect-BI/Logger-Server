from flask import Flask, request, jsonify
from store import Store
import uuid
from utils import *
from controllers import org

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
    return org.createOrg(store, body)

if __name__ == '__main__':
    app.run()
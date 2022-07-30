from flask import Flask, request, jsonify
from store import Store
import uuid
from utils import *
from controllers import org

app = Flask(__name__)
store = Store("store.pkl")

@app.route("/", methods=["GET"])
def home() : 
    return DUMMY_RES()

@app.route("/createOrg", methods=["POST"])
def createOrg() :
    err, body = checkJsonAndBody(request, ["name"])
    if err : 
        return err
    return org.createOrg(store, body)

@app.route("/addUser", methods=["POST"])
def addUser() :
    err, body = checkJsonAndBody(request, ["name", "org"])
    if err : 
        return err
    return DUMMY_RES()

if __name__ == '__main__':
    app.run()
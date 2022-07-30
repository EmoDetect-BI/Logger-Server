from flask import Flask, request
from store import Store
from utils import *
from controllers import logControllers, orgControllers

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
    return orgControllers.createOrg(store, body)

@app.route("/addUser", methods=["POST"])
def addUser() :
    err, body = checkJsonAndBody(request, ["name", "org"])
    if err : 
        return err
    return orgControllers.addUser(store, body)

@app.route("/saveDatabase", methods=["GET"])
def saveDatabase() :
    store.save()
    return DUMMY_RES()

@app.route("/createSession", methods=["POST"])
def createSession() : 
    err, body = checkJsonAndBody(request, ["name", "org", "session"])
    if err : 
        return err
    return logControllers.createSession(store, body)

@app.route("/log", methods=["POST"])
def log() : 
    err, body = checkJsonAndBody(request, ["session", "log"])
    if err : 
        return err
    logControllers.saveLog(store, body)
    return DUMMY_RES()

@app.route("/getDB", methods=["GET"])
def getDB() : 
    return jsonify(store.getDB())

@app.route("/getLogs/<uuid:session>", methods=["GET"])
def getLogs(session) : 
    return jsonify(store.getLogs(str(session)))

if __name__ == '__main__':
    app.run()
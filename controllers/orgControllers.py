from flask import jsonify

def createOrg(store, body) :
    nm = body["name"]
    if store.isOrg(nm) :
        return jsonify({
            "status" : "error",
            "message" : "Org already exists"
        })
    
    store.addOrg(nm)
    store.save()
    return jsonify({
        "status" : "success",
        "message" : "Org created"
    })

def addUser(store, body) :
    nm = body["name"]
    org = body["org"]
    if not store.isOrg(org) :
        return jsonify({
            "status" : "error",
            "message" : "Org does not exist"
        })
    if store.isUser(org, nm) :
        return jsonify({
            "status" : "error",
            "message" : "User already exists"
        })
    store.addUser(org, nm)
    store.save()
    return jsonify({
        "status" : "success",
        "message" : "User added"
    })
from flask import jsonify

def createSession(store, body) :
    org = body["org"] 
    nm = body["name"]
    sess = body["session"]
    
    if not store.isOrg(org) :
        return jsonify({
            "status" : "error",
            "message" : "Org does not exist"
        })
    if not store.isUser(org, nm) :
        return jsonify({
            "status" : "error",
            "message" : "User does not exist"
        })
    if sess in store.sessions[(org, nm)] :
        return jsonify({
            "status" : "error",
            "message" : "Session already exists"
        })
    store.addSession(org, nm, sess)
    store.save()
    return jsonify({
        "status" : "success",
        "message" : "Session created"
    })
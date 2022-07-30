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
from flask import jsonify

def DUMMY_RES() :
    return jsonify({
        "status" : "success",
    })

def DUMMY_ERR() :
    return jsonify({
        "status" : "failed",
    })

def checkJsonAndBody(req, fields) :
    body = None
    try : 
        body = req.get_json()
    except :
        return jsonify({
            "status" : "error", 
            "message" : "Invalid request"
        }), None
    if not body :
        return jsonify({
            "status" : "error",
            "message" : "No body"
        }), None
    
    missing = []
    flag = False
    for field in fields : 
        if not field in body :
            flag = True
            missing.append(field)
            
    if flag : 
        return jsonify({
            "status" : "error",
            "message" : "Fileds missing",
            "meta" : {
                "missing" : missing
            }
        }), None
    return None, body
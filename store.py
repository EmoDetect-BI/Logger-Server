import os
import pickle

class Store : 
    def __init__(self, save_pth) :
        self.save_pth = save_pth
        self.orgStructure = {}
        self.sessions = {}
        self.logs = {}
        if os.path.exists(save_pth) :
            print("Loading Database...")
            with open(save_pth, "rb") as f :
                sv = pickle.load(f)
                self.orgStructure = sv.orgStructure
                self.logs = sv.logs
                self.sessions = sv.sessions
            print("Database Loaded from local")
        
    def isOrg(self, orgName) :
        return orgName in self.orgStructure
    
    def addOrg(self, orgName) :
        self.orgStructure[orgName] = set({})
    
    def isUser(self, orgName, userName) :
        return userName in self.orgStructure[orgName]
    
    def addUser(self, orgName, userName) :
        self.orgStructure[orgName].add(userName) 
        self.sessions[(orgName, userName)] = set({})   
    
    def addSession(self, orgName, userName, session) : 
        self.sessions[(orgName, userName)].add(session)
    
    def save(self) :
        with open(self.save_pth, "wb") as f :
            pickle.dump(self, f)
        print("Database saved to local")
    
    def __repr__(self) : 
        return str(self.orgStructure)

    def getDB(self) :
        org = {}
        for i in self.orgStructure : 
            org[i] = list(self.orgStructure[i])
        sess = []
        for i in self.sessions : 
            sess.append({
                "org" : i[0],
                "name" : i[1],
                "sess" : list(self.sessions[i])
            })
        return {
            "orgStructure" :org,
            "sessions" : sess,
        }
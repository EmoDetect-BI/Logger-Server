import os
import pickle

class Store : 
    def __init__(self, save_pth) :
        self.save_pth = save_pth
        self.orgStructure = {}
        self.logs = {}
        if os.path.exists(save_pth) :
            print("Loading database...")
            with open(save_pth, "rb") as f :
                sv = pickle.load(f)
                self.orgStructure = sv.orgStructure
                self.logs = sv.logs
        
    def isOrg(self, orgName) :
        return orgName in self.orgStructure
    
    def addOrg(self, orgName) :
        self.orgStructure[orgName] = set({})    
    
    def save(self) :
        with open(self.save_pth, "wb") as f :
            pickle.dump(self, f)
    
    def __repr__(self) : 
        return str(self.orgStructure)
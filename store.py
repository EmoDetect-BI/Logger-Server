class Store : 
    def __init__(self) :
        self.orgStructure = {}
        self.logs = {}
        
    def isOrg(self, orgName) :
        return orgName in self.orgStructure
    
    def addOrg(self, orgName) :
        self.orgStructure[orgName] = set({})    
    
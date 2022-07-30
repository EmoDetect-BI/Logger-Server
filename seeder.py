STRUCTURE = [
    {
        "organization": "org1",
        "users" : [
            "User1",
            "User2",
            "User3"
        ]
    },
    {
        "organization" : "org2",
        "users" : [
            "User4",
            "User5",
            "User6",
            "User7",
            "User8",
            "User9",
            "User10",
            "User11"
        ]
    }
]

from store import Store

s = Store("store.pkl", False)
for org in STRUCTURE : 
    s.addOrg(org["organization"])
    for user in org["users"] :
        s.addUser(org["organization"], user)
s.save()
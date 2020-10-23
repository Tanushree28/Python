import json

data ='''
{
    "name" : "Tanushree",
    "phone" :{
        "type" : "intl",
        "number" : "98499010"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:',info["email"]["hide"])

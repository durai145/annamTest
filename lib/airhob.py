import requests
import yaml
conf=yaml.load(open("/root/annamTest/conf/annam.yml", "r").read())
data={
    "TripType": "O",
    "NoOfAdults": 1,
    "NoOfChilds": 0,
    "NoOfInfants": 0,
    "ClassType": "Economy",
    "OriginDestination": [
        {
            "Origin": "SFO",
            "Destination": "LAX",
            "TravelDate": "04/23/2018"
        }
    ],
    "Currency": "USD"
}
host=conf[0]['host']
port=conf[0]['port']
prot = None
host='dev-sandbox-api.airhob.com'

def search(searchReq):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json', 'mode': 'sandbox',  'apikey' : 'f6b7abfd-4650-4'}
    if None != port:
        r=requests.post("https://" + host + ":" + port + "/sandboxapi/flights/v1.3/search", headers=headers, json=searchReq, verify=False)
    else:
        r=requests.post("https://" + host + "/sandboxapi/flights/v1.3/search", headers=headers, json=searchReq, verify=False)
    return r

r=search(data)
print(r.text)
#getUser()


import requests
import yaml
conf=yaml.load(open("/home/ubuntu/annamTest//conf/annam.yml", "r").read())
data={}
data['product_name'] = 'HOME'
data['product_version'] = '001'
data['username'] = 'duraimurugan.govindaraj.002'
data['emp_id'] = 'H00020002'
data['first_name'] = 'duraimurugan'
data['last_name'] = 'govindaraj'
data['dob'] = '10-oct-1983'
data['password'] = '1qaz2wsx'
data['user_type'] = 'EMPLOYEE'
data['user_role'] = 'SECURITY_ADMIN'

host=conf[0]['host']
port=conf[0]['port']

def createUser(createUserReq):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    r=requests.put("https://" + host + ":" + port + "/user/create", headers=headers, json=createUserReq, verify=False)
    return r

#createUser(data);

def getUser():
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    r=requests.get("https://" + host + ":" + port + "/user/", headers=headers, verify=False)
    return r

#getUser()

def getUserDetails(empId):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    r=requests.get("https://" + host + ":" + port + "/user/" + empId + "/details", headers=headers, verify=False)
    return r
#getUserDetails(empId)


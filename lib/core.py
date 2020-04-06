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

errorCount=0
successCount=0

host=conf[0]['host']
port=conf[0]['port']
protocal='http'
if 'protocal' in conf[0]:
    protocal=conf[0]['protocal']

def createUser(createUserReq):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url = protocal + "://" + host + ":" + port + "/user/create"; 
    print(  url)
    print ( createUserReq)
    r=requests.put(url, headers=headers, json=createUserReq, verify=False)
    return r

def createV1User(createUserReq):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url = protocal + "://" + host + ":" + port + "/v1/user/create" 
    print( url)
    print (createUserReq)
    r=requests.put(url, headers=headers, json=createUserReq, verify=False)
    return r
#createUser(data);
def createRole(createUserReq):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url=protocal + "://" + host + ":" + port + "/role/create"
    print(url)
    print(createUserReq)
    r=requests.put(url, headers=headers, json=createUserReq, verify=False)
    return r

def getUser():
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url=protocal  + "://" + host + ":" + port + "/user/"
    print(url)
    print(createUserReq)
    r=requests.get(url, headers=headers, verify=False)
    return r

#getUser()

def getUserDetails(empId):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url = protocal + "://" + host + ":" + port + "/user/" + empId + "/details"
    print(url)
    print(empId)
    r=requests.get(url, headers=headers, verify=False)
    return r
#getUserDetails(empId)

def getPortal():
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url = protocal + "://" + host + ":" + port + "/portal/"
    print(url)
    r=requests.get(url, headers=headers, verify=False)
    return r

def createPortal(data):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url = protocal + "://" + host + ":" + port + "/portal/create"
    print(url)
    print(data)
    r=requests.put(url, json=data,  headers=headers, verify=False)
    return r

def createProduct(data):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url = protocal + "://" + host + ":" + port + "/product/create"
    print(url)
    print(data)
    r=requests.put(url, json=data,  headers=headers, verify=False)
    return r

def getProducts():
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url =protocal + "://" + host + ":" + port + "/product/" 
    print(url)
    r=requests.get(url, json=data,  headers=headers, verify=False)
    return r

def getRoles():
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url =protocal + "://" + host + ":" + port + "/role/"
    print(url)
    r=requests.get(url, json=data,  headers=headers, verify=False)
    return r

def getPortalDetails(prtlId):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url =protocal + "://" + host + ":" + port + "/portal/" + prtlId + "/details"
    print(url)
    r=requests.get(url, json=data,  headers=headers, verify=False)
    return r

def doLogin(data):
    headers = {'user-agent': 'annam/0.0.1', 'content-type': 'application/json'}
    url =protocal + "://" + host + ":" + port + "/service/loginDetails/doLogin"
    print(url)
    r=requests.post(url, json=data,  headers=headers, verify=False)
    return r


def verify(**args):
    global errorCount, successCount
    if str(args['expected']) != str(args['actual']):
        errorCount=errorCount + 1
        print(args)
        print(errorCount)
        print(successCount)
    else:
        successCount=successCount + 1

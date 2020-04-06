import sys
sys.path.append('/home/ubuntu/annamTest/lib');
from  core import *
import json

data={}
data['prtl_name'] = 'GPASSO'
data['prtl_version'] = '001'
data['username'] = 'duraimurugan.govindaraj.002'
data['emp_id'] = 'H00020002'
data['first_name'] = 'duraimurugan'
data['last_name'] = 'govindaraj'
#data['dob'] = '10-oct-1983'
data['password'] = '1qaz2wsx'
data['user_type'] = 'Employee'
data['user_role'] = 'SECADMIN'
data['role_name'] = 'ADMIN'

print(json.dumps(data, indent=4, sort_keys=True))
r=createV1User(data)
print(r.text)
createResp=json.loads(r.text)
#  "error": "Not Found", 
#  "message": "Portal is not exists", 
#  "path": "/v1/user/create", 
#  "status": 404, 
#  "timestamp": "2020-02-29T01:28:12.715+0000"
verify(expected='404', actual=createResp['status'],field='status', path=createResp['path'])
verify(expected='Portal is not exists', actual=createResp['message'],field='message',path=createResp['path'])

#r=getUserDetails(data['emp_id'])
#parsedJson=json.loads(r.text)
#print json.dumps(parsedJson, indent=4, sort_keys=True)

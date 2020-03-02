import sys
sys.path.append('/home/ubuntu/annamTest/lib');
from  core import *
import json

data={}
data['prtl_name'] = 'GPASSOSP'
data['prtl_version'] = '002'
data['username'] = 'duraimurugan.govindaraj.002'
data['emp_id'] = 'H00020002'
data['first_name'] = 'duraimurugan'
data['last_name'] = 'govindaraj'
#data['dob'] = '10-oct-1983'
data['password'] = '1qaz2wsx'
data['user_type'] = 'Employee'
data['user_role'] = 'SECADMIN'

print json.dumps(data, indent=4, sort_keys=True)
r=createV1User(data)
print r.text
r=getUserDetails(data['emp_id'])
parsedJson=json.loads(r.text)
#print json.dumps(parsedJson, indent=4, sort_keys=True)

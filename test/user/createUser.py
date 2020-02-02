import sys
sys.path.append('/home/ubuntu/annamTest/lib');
from  core import *
import json

data={}
data['product_name'] = 'HOME'
data['product_version'] = '001'
data['username'] = 'duraimurugan.govindaraj.001'
data['emp_id'] = 'H00020001'
data['first_name'] = 'duraimurugan'
data['last_name'] = 'govindaraj'
data['dob'] = '10-oct-1983'
data['password'] = '1qaz2wsx'
data['user_type'] = 'Employee'
data['user_role'] = 'Security_Admin'
r=createUser(data)
r=getUserDetails(data['emp_id'])
parsedJson=json.loads(r.text)
print json.dumps(parsedJson, indent=4, sort_keys=True)

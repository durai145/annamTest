
import sys
sys.path.append('/home/ubuntu/annamTest/lib');
from  core import *
import json

data={}

#{prtlName='null', prtlVersion='null', basePath='null', prodName='null', prodVersion='null'


#     String prtlName;
#     String prtlVersion;
#     String basePath;
#     String prodName;
#     String prodVersion;

#     String roleName;
#     String status;
#     int roleValue;
#     String prtlName;
#     String prtlVersion;

data['prtl_name'] = 'GPASSOSP'
data['prtl_version'] = '001'
data['role_name'] = 'ADMIN'
data['status'] = '001'
data['role_value'] = 0xFF
r=createRole(data)
print(r.text)

r=getRoles()
print(r.text)
parsedJson=json.loads(r.text)
print(json.dumps(parsedJson, indent=4, sort_keys=True))

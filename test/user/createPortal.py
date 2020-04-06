
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


data['prtl_name'] = 'GPASSOSP'
data['prtl_version'] = '001'
data['prod_name'] = 'HOME'
data['prod_version'] = '001'
data['base_path'] = 'prtl'
r=createPortal(data)
print(r.text)

r=getPortal()
print(r.text)
parsedJson=json.loads(r.text)
print(json.dumps(parsedJson, indent=4, sort_keys=True))
for prtl in parsedJson:
    if 'id' in prtl:
        r=getPortalDetails(prtl['id'])
        print(r.text)
        jsonObj = json.loads(r.text)
        print(json.dumps(jsonObj, indent=4, sort_keys=True))

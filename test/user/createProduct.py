
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


data['prod_name'] = 'HOME'
data['prod_version'] = '001'
r=createProduct(data)
print r.text

r=getProducts()
print r.text
parsedJson=json.loads(r.text)
print json.dumps(parsedJson, indent=4, sort_keys=True)
for prod in parsedJson:
    print prod
            

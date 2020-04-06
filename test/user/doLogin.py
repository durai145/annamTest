import sys
import json
sys.path.append('/home/ubuntu/annamTest/lib');
from  core import *

LoginDetailsRequest={}
UserDetails={}
UserDetails['username'] = "H00020002"
UserDetails['password'] = "1qaz2wsx"
PortalDetails={}
PortalDetails['portal_key'] = 'GPASSOSP'
LoginDetailsRequest['user_details']=UserDetails;
LoginDetailsRequest['portal_details']=PortalDetails;

print(json.dumps(LoginDetailsRequest, indent=4, sort_keys=True))
r=doLogin(LoginDetailsRequest)
print(r.text)

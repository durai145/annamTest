import requests

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
r=requests.put("https://192.168.1.42/user/create", json=data, verify=False)

print(r.text)

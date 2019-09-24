#%%
import requests
from requests.auth import HTTPBasicAuth

#%%
r = requests.get('http://127.0.0.1:8000/apis/orders', auth=HTTPBasicAuth('admin', 'admin'))
print(r.content)

#%%
data = {
    "order_desc": "test entry 2",
    "order_date": "2019-09-25",
    "order_qty": 1,
    "order_amount": 200.0,
    "order_notes": "Good",
    "order_item": 1,
    "order_payment_type": 1
}
r = requests.post('http://127.0.0.1:8000/apis/orders', data = data, auth=HTTPBasicAuth('admin', 'admin'))
print(r.content)

#%%

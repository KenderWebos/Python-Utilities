import time
import requests

def AddCustomer(id, email, name, active):
    customer = {'id': id, 'email':email, 'name':name, 'active': active}
    r = requests.post('http://192.168.0.2:3000/customers', json=customer)

    print(r.json())

def GetAllCustomers():
    r = requests.get('http://192.168.0.2:3000/customers')
    data = r.json()

    for element in data:
        print(element)

AddCustomer(0,"awebo@ucsc.cl","chang",1)
GetAllCustomers()
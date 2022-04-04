import time
import requests

def agregarCustomer(id, email, name, active):

    customer = {'id': id, 'email':email, 'name':name, 'active': active}
    r = requests.post('http://192.168.0.2:3000/customers', json=customer)

    print(r.json())

def conseguirTodosLosCustomers():

    r = requests.get('http://192.168.0.2:3000/customers')
    data = r.json()

    for element in data:
        print(element)

agregarCustomer(0,"awebo@ucsc.cl","chang",1)
conseguirTodosLosCustomers()
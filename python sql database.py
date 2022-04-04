import time
import requests

def agregarCustomer():

    customer = {'id': 2, 'email':"something@gmail.com", 'name':"Matias", 'active': 1}
    r = requests.post('http://localhost:3000/customers', json=customer)

    print(r.json())

def conseguirTodosLosCustomers():

    r = requests.get('http://localhost:3000/customers')
    data = r.json()

    for element in data:
        print(element)

conseguirTodosLosCustomers()
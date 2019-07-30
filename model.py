import json
import os

PATH = os.path.dirname(__file__)
DATA = "other_data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)

def save(data):
    with open(DATAPATH, 'w') as file_object:
        json.dump(data, file_object, indent=2)

def create_account(NewFirstname,NewLastName,newpin):
        import random
        newaccountnumber = random.randint(1,1000)
        client= NewFirstname + NewLastName
        data={client:{'Account_number':newaccountnumber,'Pin':int(newpin),'Balance':0}}
        data.update()
        return data



def login(clientcheck,accountcheck,pin):
        if clientcheck in data:
                if data[clientcheck]['Account_number']== accountcheck & data[clientcheck]['Pin']== pin:
                        return True
        
def get_balance(clientname):
    return data[clientname]['Balance']


def client_exists(client):
    if client in data:
        return True
    return False

def withdraw(client,money):
    if data[client]["Balance"]> int(money):
           data[client]["Balance"]=data[client]["Balance"]-int(money)
           save(data)
    else:
        print("Inssuficient fund")
     
        
        
def add_fund(client,money): 
    data[client]['Balance']=data[client]['Balance']+int(money)
    save(data)





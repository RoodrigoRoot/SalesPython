import sys



clients = ["Pablo", "Ricardo"]

def createClient(client_name):
    global clients

    
    if clientName not in clients:
        clients.append(client_name)
        
        listClients()
    else:
        Message(0)


def listClients():
   for id, client in enumerate(clients):
       print("{}: {}".format(id,client))


def updateClient(clientName,updateClientName):
    global clients

    if clientName in clients:
        index = clients.index(clientName)
        clients[index] = updateClientName
        print(clientName)
        listClients()
    else:
        Message(1)


def deletedClient(clientName):
    global clients

    if clientName in clients:
        clients.remove(clientName)
        listClients()
    else:
        Message(0)
      

def Message(code):

    if code == 1:
        print("The client already is in the client\'s list")#Cliente encontrado
        
    elif code == 2:
        print("Client Found")
    else:
        print("The client is not include en Clients List")

def searchClient(clientName):
    global clients
    for client in clients:
        if client != clientName:
            continue
        else:
            return True    


def _printWelcome():
    print('*' * 80)
    print("Bienvenido a Platzi Ventas")
    print('*' * 80)
    print("what would you lije to do today?")
    print("[C]Create Client")
    print("[L]List Client")
    print("[U]Update Client")
    print("[D]Delete Client")
    print("[S]Search Client")


def _getClientName():
    clientName = None
    
    while not  clientName:
        clientName = input("what is the client name? ")
        
        if clientName == "exit":
            clientName = None
            break
    if not clientName:
        sys.exit()
  
    return clientName


    
if __name__ == '__main__':
    _printWelcome()

    command = input()
    command = command.upper()
    if command == "C":
        clientName = _getClientName()
        createClient(clientName)
        
    elif command == "L":
        listClients()
    elif command == "D":
         clientName = _getClientName()
         deletedClient(clientName)
         
         
    elif command =='U':
        clientName = _getClientName()
        updateClientName = input("what is the new name?")
        updateClient(clientName,updateClientName)
    
    elif  command == "S":
        clientName = _getClientName()
        found = searchClient(clientName)

        if found:
            Message(2)
            listClients()
        else:
            print("Bad {}".format(clientName))
            listClients()


    else:
        print("Comando Invalido")
        listClients()
    

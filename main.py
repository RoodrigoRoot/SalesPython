clients = "Pablo, Ricardo"

def createClient(client_name):
    global clients
    _addComa()
    if clientName not in clients:
        clients += client_name
        _addComa()
    else:
        print('The client already is in the client\'s list')




def listClients():
    global clients
    print(clients)


def _addComa():
    global clients
    clients +=  ", "


def _printWelcome():
    print('*' * 50)
    print("Bienvenido a Platzi Ventas")
    print('*' * 50)
    print("what would you lije to do today?")
    print("[C]Create Client")
    print("[D]Delete Client")


if __name__ == '__main__':
    _printWelcome()

    command = input("")
    if command == "C":
        clientName = input("what is the client name?")
        createClient(clientName)
        listClients()
    elif command == "D":
        pass
    else:
        print("Comando Invalido")
    

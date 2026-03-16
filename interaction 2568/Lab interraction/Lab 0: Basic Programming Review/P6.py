"""
priyakorn pichitmarn
683040494-9
P6 
"""
def main():
    
    clients = {}

    
    while True:
        client_id = input("Client ID: ")
        
      
        if client_id == "done":
            break
            
       
        saving = float(input("Enter saving: "))
        
     
        clients[client_id] = saving


    print("Current clients:")
    for c_id, c_saving in clients.items():
        print(f"{c_id} : {c_saving:.2f}")

    search_id = input("Search for ID: ")
    if search_id in clients:
        print(f"{search_id} has {clients[search_id]:.2f}")
    else:
        print(f"{search_id} not found")

    new_client_id = input("Client ID: ")
    
    total_savings = sum(clients.values())

    clients[new_client_id] = total_savings

    print("Current clients:")
    for c_id, c_saving in clients.items():
        print(f"{c_id} : {c_saving:.2f}")

if __name__ == "__main__":
    main()
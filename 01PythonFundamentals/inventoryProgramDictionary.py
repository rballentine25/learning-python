
def launchInventory():
    inventory = {}
    while True:        
        selInput = input(f"""Inventory Management
    1. Add Item
    2. Remove item
    3. Display inventory
    4. Quit
Choose one: """)
        
        if selInput =='1':
            addItem()
        elif selInput == '2':
            removeItem()
        elif selInput == '3':
            dispInventory()
        else:
            break

def addItem():
    return 

def removeItem():
    return 

def dispInventory():
    return 


launchInventory()


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inventory = dict(sorted(inv.items()))

def display_inventory(inventory):
    print('\n-------------------------------------------- ')
    print("Inventory:")
    for k,v in inventory.items():
        print(v,k)
    print("Total items: ", sum(inventory.values()))
    print('\n-------------------------------------------- ')


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, added_items):
    for item in dragon_loot:
        if item in inventory:
            inventory[item] +=1
        else: 
            inventory[item] = 1



def print_table(inventory, order=None):
    k_list=[]
    for k,v in inventory.items(): 
        k=str(k)
        v=str(v)
        k_list.append(k)
    max_key_len=int(len(max(k_list, key=len)))
    max_value_len=int(len('count'))
    print('\n-------------------------------------------- ')
    print("Inventory:")
    print("count".rjust(max_value_len," "),"item name".rjust(max_key_len+max_value_len," "))
    print('-'*(max_key_len+2*max_value_len+1))
    if order=='count,asc':
        for k,v in sorted(inventory.items(),key=lambda v:v[1]):
            v=str(v)   
            k=str(k)
            print(v.rjust(max_value_len," "), k.rjust(max_key_len+max_value_len," "))
    elif order=='count,desc':
        for k,v in sorted(inventory.items(),key=lambda v:v[1], reverse=True):
            v=str(v)   
            k=str(k)
            print(v.rjust(max_value_len," "), k.rjust(max_key_len+max_value_len," "))
    else:
        for k,v in inventory.items():
            v=str(v)   
            k=str(k)
            print(v.rjust(max_value_len," "), k.rjust(max_key_len+max_value_len," "))
    print('-'*(max_key_len+2*max_value_len+1))
    print("Total number of items:",sum(inventory.values()))
    print('\n-------------------------------------------- ')

def import_inventory(inventory, filename="import_inventory.csv"):
        file = open(filename, 'r')
        data = file.readline().split(',')
        for item in data:
            item = item.strip()
            if item in inventory:
                inventory.update({item: inventory[item]+1})
            else:
                inventory.update({item: 1})
        return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    if filename == None:
        with open('export_inventory.csv', 'w') as export_inv:
            for key, value in inventory.items():
                export_inv.write('%s:%s, ' % (key, value))
    else:
        with open(filename, 'w') as export_inv:
            for key, value in inventory.items():
                export_inv.write('%s:%s, ' % (key, value))
    export_inv.close()

add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
print_table(inventory, 'count,None')
export_inventory(inventory, filename=None)

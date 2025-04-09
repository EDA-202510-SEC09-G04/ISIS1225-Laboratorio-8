
import bst_node as bst



def new_map():
    
    map = {'root': None}
    
    return map




def put (my_bst, key,value):
    
   my_bst['root'] =  insert_node(my_bst['root'],key,value)
   
   

def insert_node(root,key,value):
    
    if root == None:
        
        return bst.new_node(key,value)


    if key < root['key']:
        
       root['left'] = insert_node(root['left'],key,value)
        
    elif key > root['key']:
        
        root['right'] = insert_node(root['right'],key,value)
        
        
    else:
        
        root['value'] = value
        
        
    return root





def get(my_bst,key):
    
    
    node = get_node(my_bst['root', key])
    if node is not None:
        
        return node['value']
    
    else:
        
        return None


def get_node (root,key):
    
    if root == None:
        
        return None
    
    if root['key'] == key:
        
        return root
    
    elif root['key'] < key :
        
        return get_node(root['left'],key)
    
    elif root['key'] > key:
        
        return get_node(root['right'],key)
        



def encontrar_minimo(nodo):
    
    actual = nodo
    
    while actual['left']:
        
        actual = actual['left']
        
    return actual




def remove(my_bst,key):
    
    my_bst['root'] = remove_node(my_bst['root'],key)


def remove_node(root,key):
    
    if root == None:
        
        return root
    
    
    if  root['key'] > key:
        
        root['left'] = remove_node(root['left'],key)
        
    elif root['key'] < key:
        
        root['right'] = remove_node(root['right'],key)
        
    
    else:
        
        # Caso 1: El nodo no tiene hijos
        
        if root['left'] is None and root['right'] is None:
            
            return None
        
        # Caso 2: El nodo solo tiene un hijo
        
        if  root['left'] is None:
            
            return root['right']
        
        elif root['right'] is None:
            
            return root['left']
        
        #Caso 3: El nodo tiene dos hijos
        
        sucesor = encontrar_minimo(root['right'])
        root['key'] = sucesor['key']
        root['value'] = sucesor['value']
        root['right'] = remove_node(root['right'], sucesor['key'])
    
    
    return root
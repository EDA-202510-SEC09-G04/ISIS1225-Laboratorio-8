
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
        
       
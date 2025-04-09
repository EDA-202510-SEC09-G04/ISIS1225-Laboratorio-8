
from pprint import pprint
import DataStructures.Tree.bst_node as bst


def new_map():
    
    map = {'root': None}
    
    return map



def put (my_bst, key,value):
    
   my_bst['root'] =  insert_node(my_bst['root'],key,value)
   
   return my_bst
   

def insert_node(root,key,value):
    if root is None:
        return bst.new_node(key, value)

    if key < root['key']:
        root['left'] = insert_node(root.get('left'), key, value)
    elif key > root['key']:
        root['right'] = insert_node(root.get('right'), key, value)
    else:
        root['value'] = value
        return root  

    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size

    return root


# Crea un arbol vacío
map = new_map()
print(map)
# Salida esperada: { "root": None }

# Agrega un nuevo nodo al árbol
map = put(map, 2, "dos")

# Agrega otro nodo al árbol
map = put(map, 1, "uno")

# Agrega otro nodo al árbol con una llave ya existente
map = put(map, 1, "uno modificado")

pprint(map)


def get(my_bst,key):

    
    node = get_node(my_bst['root'],key)
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




def contains(my_bst,key):
    
   nodo =  get(my_bst,key)
   
   
   if nodo is not None:
       
       return True
   
   else:
       
       return False
   
   
   
   
def size(my_bst):
    
    return size_tree(my_bst['root'])
   
def size_tree(root):
    
    if root is None:
        
        return 0
    
    return 1 + size_tree(root['right']) + size_tree(root['left'])



def is_empty(my_bst):
    
    if my_bst['root'] is None:
        
        return True
    
    else:
        
        return False
    
    
    
def key_set(my_bst):
    
    
    return key_set_tree(my_bst['root'],None)
    
    
def key_set_tree(root, resultado = None):
    
    if resultado is None:
        
        resultado = []
        
        
    if root is not None:
        
        
        key_set_tree(root['left'],resultado)
        resultado.append(root['key'])
        key_set_tree(root['right'], resultado)
        
    return resultado


#COMIENZO FUNCIONES POR DESARROLLAR

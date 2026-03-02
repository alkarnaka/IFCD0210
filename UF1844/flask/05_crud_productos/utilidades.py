import json

def cargar_productos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_datos(archivo, datos):
    with open(archivo,'w', encoding='utf-8') as f:
        json.dump(datos, f, indent= 4, ensure_ascii=False)

def nuevo_id(archivo_prod):
    datos = cargar_productos(archivo_prod)
    prods = datos['productos']
    
    if not prods:
        return 1
    
    lista_ids = [p['id'] for p in prods]
    return max(lista_ids) + 1
import json

def cargar_productos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_datos(archivo, datos):
    with open(archivo,'w', encoding='utf-8') as f:
        json.dump(datos, f, indent= 4, ensure_ascii=False)

def nuevo_id(archivo_prod):
    lista_ids = []
    datos = cargar_productos(archivo_prod)
    prods = datos['productos']
    for p in prods:
        lista_ids.append(p['id'])
    
    return max (lista_ids) + 1
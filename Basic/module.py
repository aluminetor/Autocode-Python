

def full_name(name: str, lastname: str) -> str:
    print(name, lastname)




import random
import string
 

def random_user_id() -> str:
    caracteres = string.ascii_lowercase + string.digits
    return "".join(random.choices(caracteres, k=6))



def user_id_gen_by_user() -> str:
    caracteres = string.ascii_letters + string.digits
    
    # Lectura de las dos entradas
    num_caracteres = int(input("Número de caracteres: "))
    num_ids = int(input("Número de IDs a generar: "))
    
    # Generar la lista de identificadores
    ids = [
        "".join(random.choices(caracteres, k=num_caracteres))
        for _ in range(num_ids)
    ]
    
    # Retornar los IDs separados por salto de línea
    return "\n".join(ids)


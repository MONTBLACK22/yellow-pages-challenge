# Tu código aquí




# Listar todos los usuarios
# Agregar un nuevo usuario. Para ello deberás solicitar el nombre y el número al usuario
# Modificar un usuario existente. Para ello deberás solicitar el nombre del cliente, buscarlo, y en caso de encontrarlo, solicitar el nuevo número. En caso de no encontrarlo, hazle saber al usuario que el nombre del cliente no existe.
# Eliminar un usuario existente.
# Salir

people = {
  "Ana": "+4-651-928088",
  "Juan": "+23-698-536640",
  "Pedro": "+40-659-506848",
  "Luis": "+20-615-184747",
  "Maria": "+78-671-257932",
  "Sofia": "+30-611-770853",
  "Jose": "+27-669-616952",
  "Lucia": "+38-642-779107",
  "Carlos": "+19-665-202837",
  "Marta": "+38-691-898782",
  "Miguel": "+32-636-538868",
  "Laura": "+80-670-553129",
  "David": "+80-650-777691",
  "Paula": "+9-645-756359",
  "Andres": "+31-650-896836",
  "Elena": "+65-658-231873",
  "Jorge": "+35-638-631914",
  "Raul": "+54-631-199248",
  "Clara": "+94-642-663803",
  "Sara": "+48-657-677260"
}



while  True:
    print('Menú: ')
    print('Presiona 1. Listar todos los usuarios')
    print('Presiona 2. Agregar un nuevo usuario')
    print('Presiona 3. Modificar un usuario existente')
    print('Presiona 4. Eliminar un usuario existente')
    print('Presiona 5. Salir')
    user_input = int(input())
    if user_input == 1:
        for key,value in people.items():
            print(f'{key}---------->{value}')
    elif user_input == 2:
        nuevo = input('Ingrese el nombre del usuario: ')
        phone = input('Ingrese el número de teléfono del usuario: ')
        people[nuevo] =  phone
    elif  user_input == 3:
        name = input('Ingrese el nombre del usuario a modificar: ')
        if name in people:
            new_phone = input('Ingrese el nuevo número de teléfono del usuario: ')
            people[name] = new_phone
        else:
                print('El nombre del usuario no existe')
    elif user_input == 4:
        name = input('Ingrese el nombre del usuario a eliminar: ')
        if name in people:
            del  people[name]
            print('El usuario ha sido eliminado')
        else:
            print('El nombre del usuario no existe')
    elif  user_input == 5:
        break
    else:
        print('Valor Incorrecto!')
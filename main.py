# Estructura de una Tarea
# tarea = {
#    "text": "la tarea", 
#    "done": False,
# }

task_list = []


def run():

    running = True

    while(running == True):

        print("LISTA DE TAREAS")
        print("1. Agregar nueva tarea")
        print("2. Ver la lista de  tarea (no disponible)")
        print("3. Quitar una tarea (no disponible)")
        print("4. Editar una tarea (no disponible)")
        print("5. marcar una tarea como terminada (no disponible)")
        print("6. salir")
        print
        option = int(input("escoja la accion a ejecutar y dar enter: "))
        print(f"escogio la opcion {option} ")                                       

        if option == 1:
            user_text = input("escriba la nueva tarea: ")

            new_task= {
                "text": user_text,
                "done": False,
            }

            task_list.append(new_task)

            print(task_list) # TODO: Eliminar esto cuando ya podamos listar las tareas correctamente
        elif option == 6:
            running = False
                     
        else:
            print("opcion no valido")






if __name__=="__main__":
    run()

tarea = {
    "text": "la tarea",
    "done": True,
}

tarea2 = {
    "text": "otra tarea",
    "done": False
}

tarea3 = {
    "text": "otra tarea",
    "done": False
}

tarea3["text"] = "tarea 3"
tarea3["done"] = True

task_list = [tarea, tarea2, tarea3]

tarea_temp = task_list[2] # tarea3

print(tarea_temp["text"]) # tarea 3

tarea4 = {
    "text": "tarea ultima",
    "done": False
}

task_list.append(tarea4) # [tarea, tarea2, tarea3, tarea4]
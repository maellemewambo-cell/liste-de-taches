
todo_list = []

def display_menu():
    print("\n===== TO-DO LIST MANAGER =====")  
    print("1. Add a new task")                   
    print("2. View all tasks")                   
    print("3. Mark task as complete")            
    print("4. Delete a task")
    print("5. Exit")                             
    print("="*30)      

def add_task():
    description = input("Enter task description: ")  
    name = input("Enter the name of the task")
    choice = int(input("Enter task Priority: \n 1.High\n 2.Medium\n 3.Low"))
    category = ""
    while description.strip() == "":                  # strip() removes extra spaces
        print("Task description cannot be empty.")    
        description = input("Enter task description: ")  

    while name.strip() == "":                  
        print("Task name cannot be empty.")    
        name = input("Enter task name: ")
    while choice == "":
        print("Please enter Task priority level")
        choice = input("Enter task Priority: \n 1.High\n 2.Medium\n 3.Low")
    while 1>choice>4:
        print("Enter a valid priority level number")
        choice = input("Enter task Priority: \n 1.High\n 2.Medium\n 3.Low")
    if choice== 1:
        category = "high"
    elif choice == 2:
        category = "medium"
    else:
        category = "low"
    
    task = {
        "name" : name,
        "description": description,  
        "priority": category,
        "status": "Pending"           
    }

    todo_list.append(task)           
    
    print(f"Task: '{name}' : '{description}', Priority: '{category}' added successfully!") 

def view_tasks():
    
    if len(todo_list) == 0:           
        print("No tasks available.") 
        return   # return so as to break the program quickly                     

    sorted_task = sorted(todo_list, key = lambda task: task["priority"])
    print("\n--- YOUR TASKS ---")     
    
    for index, task in enumerate(sorted_task,1):
        print(f"{index}. {task['name']}: {task['description']},status: {task['status']},priority: {task['priority']}")

def mark_complete():
    view_tasks()  
    if len(todo_list) == 0:
        return

    try: #try tells python that "attempt to run this code"
        task_num = int(input("Enter task number to mark as complete: "))

        if 1 <= task_num <= len(todo_list):               
            todo_list[task_num - 1]["status"] = "Complete" 
            print("Task marked as complete!")              
        else:
            print("Invalid task number.")  
    except ValueError: # Ici cest pour que genre si le user enter un letter ou quelquechose qui nest pas int vu que tas dit quon convert task_num
        # to be an integer ca va fait lerreur donc valueError est la pour avoid ca. 
        # try and except ValueError always work together si cest pas except ValueError cest soit "else" ou "finally"
        
        print("Please enter a valid number.")

def delete_task():
    
    view_tasks()  
    
    
    if len(todo_list) == 0:
        return

    try:
        
        task_num = int(input("Enter task number to delete: "))

        
        if 1 <= task_num <= len(todo_list):
            
            removed = todo_list.pop(task_num - 1) # pop cest un built in function qui retire un element dun list et ca return le element
            # Donc removed va stored le pop element. tu pouvais aussi use "del" mais ca delete unefois et ca delete une fois ca return rien
            print(f"Task '{removed['name']}' deleted.") 
            print(view_task)
        else:
            print("Invalid task number.")  
    except ValueError:
        
        print("Please enter a valid number.")

def check_if_list_has_5_tasks():
    return len(todo_list) == 5

def check_if_list_is_full():
    return len(todo_list) == 10


while True:
    display_menu()  
    choice = input("Enter your choice (1-5): ").strip()  

    
    if choice == "1":
        if check_if_list_has_5_tasks():
            print("List already has 5 tasks. Your list is half full.")
            add_task()
        elif check_if_list_is_full():
            print("list is full. Delete one before adding another task")
        else:
            add_task()

    elif choice == "2":
        view_tasks()           

    elif choice == "3":
        mark_complete()         
        
    elif choice == "4":
        delete_task()           

    elif choice == "5":
        print("Exiting program. Adios Mi Amigos!")  
        break                               

    else:
        print("Invalid option. Please enter a number between 1 and 5.")
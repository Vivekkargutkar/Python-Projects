# define function to task
def task() : 
    tasks = []

    print("\n--------WELCOME TO THE TASK MANAGEMENT SYSTEM--------\n")

    total_task = int(input("Enter how many task you want complete in day : "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"\nToday's tasks are \n{tasks}")
    
    while True:
        print("\nEnter number to using this operations")

        operation = int(input("\n1 - Add task\n2 - Update task\n3 - Delete task\n4 - View all tasks\n5 - Exit/stop\n"))

        if operation == 1:
            add_val = input("Enter task you want to add : ")
            tasks.append(add_val)
            print(f"\nTask {add_val} has been added successfully...")

        elif operation == 2 :
            update_val = input("Enter the task name you want to update : ")
            if update_val in tasks :
                up = input("Enter new task : ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"\nTask {up} has been updated...")

            else : 
                print(f"{update_val} has not found in tasks")

        elif operation == 3 :
            del_val = input("Which task you want to delete : ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"\nTask {del_val} has been deleted successfully")

            else : 
                print(f"{del_val} has not found in tasks")

        elif operation == 4 : 
            print(f"\nTotal Tasks : {tasks} ")

        elif operation == 5 : 
            print("\nThanks for using...closing this program!!")
            break

        else :
            print("\nInvalid operation choose valid operation..!")

    
task()


        




    

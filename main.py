class TaskManager:

    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n====================================")
        print("        Tasc-Man-Ager v1.0")
        print("====================================")

        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")    

    def add_task(self):
        task = input("Enter Task: ")
        self.tasks.append(task)

        print("Task Added Successfully")    


    def view_tasks(self):
        if(self.tasks) == 0:
            print("I Can't see anything ")
            return
        
        print("\nTasks:")

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}.{task}")

manager = TaskManager()

while True:

    manager.show_menu()

    choice = input("\nChoose how you are gonna proceed: ")
    
    if choice == "1":
        print("View Tasks Selected")
        print("------------------------")
        manager.view_tasks()
    elif choice == "2":
        print("Add Tasks Selected")
        print("------------------------")
        manager.add_task()
    elif choice == "3":
        print("Complete Tasks Selected")
        print("------------------------")
    elif choice == "4":
        print("Delete Tasks Selected")
        print("------------------------")
    elif choice == "5":
        print("GoodByee!")
        break

    else:
        print("Bad Move Buddy!!")    


        




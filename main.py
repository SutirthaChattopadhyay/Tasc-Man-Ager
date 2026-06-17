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

manager = TaskManager()

while True:

    manager.show_menu()

    choice = input("\nChoose how you are gonna proceed: ")
    
    if choice == "1":
        print("View Tasks Selected")
    elif choice == "2":
        print("Add Tasks Selected")
    elif choice == "3":
        print("Complete Tasks Selected")
    elif choice == "4":
        print("Delete Tasks Selected")
    elif choice == "5":
        print("GoodByee!")
        break

    else:
        print("Bad Move Buddy!!")    


        




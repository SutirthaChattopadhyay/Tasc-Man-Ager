import json



class TaskManager:

    def load_tasks(self):

        try:

            with open("tasks.json", "r") as file:

                self.tasks = json.load(file)

        except:
            self.tasks = []        


    
    def save_tasks(self):

        with open("tasks.json", "w") as file:

            json.dump(self.tasks, file, indent=4)

    def __init__(self):
        self.tasks = []

        self.load_tasks()

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
        
        new_id = len(self.tasks) + 1

        new_task = {
            "id": new_id,
            "task": task,
            "completed": False
        }

        self.tasks.append(new_task)
        self.save_tasks()

        print("Task Added Successfully")    


    def view_tasks(self):
        if not self.tasks:
            print("I Can't see anything ")
            return
        
        print("\nTasks:")

        for task in self.tasks:

            status = "[X]" if task["completed"] else "[ ]"

            print(
                f'{task["id"]}. {status} {task["task"]}'
                  )

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


        




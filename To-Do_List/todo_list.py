import os

FILE_NAME = "tasks.txt"

def load_tasks():
   
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                tasks.append(line.strip())
    return tasks

def save_task(task):
    
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            save_task(task)
            print("Task added successfully!")
            
        elif choice == "2":
            print("\nYour Tasks:")
            if not tasks:
                print("List is empty.")
            else:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

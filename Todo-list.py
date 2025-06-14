# Creating todo list 

tasks = []

def display_menu():
    print('1. Add Task')
    print('2. Edit Task')
    print('3. Delete Task')
    print('4. Exit')

while True:
    display_menu()

    user_choice = int(input('Select an option number: '))

    if user_choice == 1:
        task = input('Enter task: ')
        tasks.append(task)
        print('Task added Successfully!')
    elif user_choice == 2:
        if tasks:
            for index, task in enumerate(tasks):
                print(f'{index + 1}.{task}')

            try:
                task_idx = int(input('Enter task index to edit: ')) - 1
                if 0 <= task_idx < len(tasks):
                    new_task = input('Enter new task: ')
                    tasks[task_idx] = new_task
                    print('Task edited Successfully!')
                else:
                    print('Invalid index')
            except ValueError:
                print('Please enter a valid number')

        else: 
            print('No tasks available to edit.')

    elif user_choice == 3:
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks.pop(task_index)
                    print("Task deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to delete.")

    elif user_choice == 4:
        print('Exiting the application. Goodbye!')
        break

    else:
        print('Invalid choice. Please select a valid option.')

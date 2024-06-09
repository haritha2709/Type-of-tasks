#Add a task
#Remove a task
#Edit a task
#Add a description
# Edit a description


#Initail Tasks list
tasks=[]

#Auxilairy functions
def displayTasks(all_tasks):
    print('\n Your tasks:')
    if len(all_tasks)<=0:
        print('\n No tasks')
    else:
        for index,task in enumerate(all_tasks):
            print(f'{index+1}:{task}')


        #enumearte will iterate both index and task



def newOperation(all_tasks):
    operation=input("Press 'A' to add a new task, 'E' to edit  a task,'R'  to remove a task or 'F' to quit the application:")
    if operation=='A':
        addTask(all_tasks)
    elif operation=='E':
        editTask(all_tasks)
    elif operation=='R':
        removeTask(all_tasks)
    elif operation=='F':
        return
    else:
        newOperation(all_tasks)  # it goes to beginning of the program and starts executing all

def editTask(all_tasks):
    task_number=input('Enter the number of task to be edited:')
    new_task=input('Edit the task')
    all_tasks[int(task_number)-1]=new_task
    print(f'Item {task_number} edited!')
    displayTasks(all_tasks)
    newOperation(all_tasks)

def removeTask(all_tasks):
    task_number=input('Enter the number of the task you want to remove:')
    all_tasks.remove(all_tasks[int(task_number)-1])
    print(f'\n Item{task_number} removed ')
    displayTasks(all_tasks)
    newOperation(all_tasks)

def addTask(all_tasks):
    new_task=input('Add a task:')
    all_tasks.append(new_task)

    displayTasks(all_tasks)
    newOperation(all_tasks)




    #Start application
addTask(tasks)


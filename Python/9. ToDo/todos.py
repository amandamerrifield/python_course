#Code a script that provides for managing a todo list
# The script should prompt the user to choose one of:
# - view all todos
# - add a new todo
# - remove a todo
# - quit
# The script should run until the user chooses to quit, that is the user ought to be able to add many todos 
# and view his/her todo list in one running of the script
# Optional: ideally the user would be able to mark a todo as complete 
# user should select v,a,r,q in input to select the action
# list of strings is probably the easiest way to solve this problem 
# ideally can mark a toDo as complete as well 

class ToDoItem():
    def __init__(self, item=None):
        self.items_list = []
        self.item = item
        self.is_complete = False
        
    
    def view_todo(self):
        print(self.items_list)
        

    def add_new_todo(self, item):
        self.items_list.append(item)

    def remove_todo(self, item):
        self.items_list.remove(item)

    def quit():
        input("Thanks for visiting. Select A, D, R or V begin again. Type Q if you would like to start start over.")

counter = 0
action = ToDoItem()
while True: 
    if counter == 0:
        selection = input("Select A, D, R, or V to begin writing ToDos: ")
        counter += 1

    elif counter > 0:
        selection.strip().upper()
        if selection == "A":
            to_do_input = input("Please add a to-do list item: ")
            action.add_new_todo(to_do_input)
            print("Here is your list so far:")
            action.view_todo()
            counter += 1

        elif selection == "V":
            print("Here is your list so far:")
            action.view_todo()
            counter += 1
            
        elif selection == "R":
           # selection = input("Which item would you like to remove?", action.view_todo, ": ")
            counter += 1
            
        selection = input("Thanks for visiting. Select A, D, R or V to write more ToDos. Write Q to begin again.")
     
    elif selection == "Q":
        action.quit()
        counter = 0
    else:
        print("Invalid option")
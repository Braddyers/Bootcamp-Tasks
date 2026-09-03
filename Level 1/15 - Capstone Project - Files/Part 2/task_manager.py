#=====importing libraries=====#

from datetime import datetime

#=====Login Section=====#

# Initialise dictionary for usernames and passwords
usernames_passwords_dictionary = {}

# Open user.txt and put contents into dictionary (key are usernames, values are passwords)
with open("user.txt", "r") as file:
    for line in file:
        usernames, passwords = line.split(", ")
        usernames_passwords_dictionary[usernames] = passwords.replace("\n", "")
# Prompt user to login using username with corresponding password
while True:                                                                              
    username_input = input("\nEnter username: ")
    if username_input not in usernames_passwords_dictionary:
        print("\nThat username does not exist. Please try again.")
    else:
        password_input = input("\nEnter password: ")
        while password_input != usernames_passwords_dictionary[username_input]:
            print("\nInvalid password. Please try again.")
            password_input = input("\nEnter password: ")
        else:
            print(f"\nWelcome to your task manager {username_input}!")
            # =====Menu Section===== #
            # Initialise menu loop
            while True:
                if username_input == "admin":                                           # Ask admin to input selection
                    menu = input(                                        
                        "\nPlease select one of the following options: " +         
                        "\nr - register user" + 
                        "\na - add task" +
                        "\nva - view all tasks" + 
                        "\nvm - view my tasks" +
                        "\nds - display statistics" +
                        "\ne - exit\n\n"
                        ).lower()                                                       # Make input lowercase if not lowercase
                else:                                                                   # if user not admin, input selection from different menu
                    menu = input(
                        "\nPlease select one of the following options: " +         
                        "\na - add task" +
                        "\nva - view all tasks" + 
                        "\nvm - view my tasks" +
                        "\ne - exit\n\n"
                        ).lower()       
                # Register user
                if menu == "r" and username_input == "admin":                           # Added 'and' to make sure only admin could proceed
                    # Ask user for new username
                    new_username = input("\nEnter new username: ")                                          
                    # Additional check if username already exists
                    with open("user.txt", "r") as file:
                        for line in file:
                            usernames, passwords = line.split(", ")                                         
                            usernames_passwords_dictionary[usernames] = passwords.replace("\n", "")
                    while new_username in usernames_passwords_dictionary:
                        print("\nThat username already exists. Please choose a different username.")
                        new_username = input("\nEnter new username: ")
                    # Ask user for new user's password and ask to confirm password
                    new_password = input("\nEnter new password: ")
                    confirm_password = input("\nEnter in new password again to confirm new password: ")
                    # Password confirmation, ask until there is a match
                    while confirm_password != new_password:                
                        print("\nPasswords do not match. Please try again.")                                
                        new_password = input("\nEnter new password: ")
                        confirm_password = input("\nEnter new password again to confirm new password: ") 
                    # Write input to user.txt file
                    with open("user.txt", "a") as file:
                        file.write(f"\n{new_username}, {new_password}")
                # Add task to tasks.txt
                elif menu == "a":
                    # Request for 4 inputs for task data items
                    tasked_user = input("\nWhat is the username of the person the task is assigned to?\n\n")
                    # Open up-to-date user.txt file for additional check below
                    with open("user.txt", "r") as file:
                        for line in file:
                            usernames, passwords = line.split(", ")                                         
                            usernames_passwords_dictionary[usernames] = passwords.replace("\n", "")
                    # Additional check if username in user list, only proceed if username already exists
                    while tasked_user not in usernames_passwords_dictionary:                                        
                        print("\nThat username does not exist. Please register that user before adding a task under their name.")    
                        tasked_user = input("\nWhat is the username of the person the task is assigned to?\n\n")    
                    task_title = input("\nWhat is the task's title?\n\n")
                    task_description = input("\nWhat is the task description?\n\n")
                    while True:
                        raw_date_input = input("\nWhat is the task's due date (DDMMYYYY)?\n\n")
                        try:
                            parsed_date_input = datetime.strptime(raw_date_input, "%d%m%Y")
                            task_due_date = parsed_date_input.strftime("%d %b %Y")
                            break
                        except ValueError:
                            print("\nInvalid date format. Please try again.")
                    # Assign values to 2 task data items
                    current_date = datetime.now()
                    date_assigned = current_date.strftime("%d %b %Y")
                    completed_yes_no = "No"
                    # Write task data items to tasks.txt
                    with open("tasks.txt", "a") as file:
                        file.write(f"\n{tasked_user}, {task_title}, {task_description}, {date_assigned}, {task_due_date}, {completed_yes_no}")
                # View all tasks in tasks.txt
                elif menu == "va":
                    task_data = []
                    # Open the file tasks.txt in read mode
                    with open("tasks.txt", "r") as file:
                        task_data = [line.strip().split(", ") for line in file]
                    # Print the all tasks according to the required format
                    print("\nAll Tasks:")
                    for task in task_data:
                        tasked_user = task[0]
                        task_title = task[1]
                        task_description = task[2]
                        date_assigned = task[3]
                        task_due_date = task[4]
                        completed_yes_no = task[5]
                        # Required format
                        print(
                            "______________________________________________________" +
                            "__________________________________________________________\n\n" +
                            f"Task:                      {task_title}\n" + 
                            f"Assigned to:               {tasked_user}\n" + 
                            f"Date assigned:             {date_assigned}\n" + 
                            f"Due date:                  {task_due_date}\n" + 
                            f"Task Complete?             {completed_yes_no}\n" + 
                            f"Task description:\n {task_description}\n" + 
                            "_______________________________________________________" +
                            "________________________________________________________\n"
                            )
                # View tasks of current logged in user in tasks.txt
                elif menu == "vm":
                    # Initialize list for task data
                    task_data = []
                    # Open the file tasks.txt in read mode
                    with open("tasks.txt", "r") as file:
                        task_data = [line.strip().split(", ") for line in file]
                    # Print only tasks assigned to current logged in user, in the required format
                    print("\nMy Tasks:")
                    for task in task_data:
                        tasked_user = task[0]
                        task_title = task[1]
                        task_description = task[2]
                        date_assigned = task[3]
                        task_due_date = task[4]
                        completed_yes_no = task[5]
                        # Only tasks of logged in user
                        if tasked_user == username_input:                                                                                                   
                            # Required format
                            print(
                                "________________________________________________________________________" +
                                "________________________________________\n\n" +
                                f"Task:                      {task_title}\n" + 
                                f"Assigned to:               {tasked_user}\n" + 
                                f"Date assigned:             {date_assigned}\n" + 
                                f"Due date:                  {task_due_date}\n" + 
                                f"Task Complete?             {completed_yes_no}\n" + 
                                f"Task description:\n {task_description}\n" + 
                                "_________________________________________________________________________" +
                                "_______________________________________\n"
                                )
                    # Print message if no tasks for current logged in user
                    if not any(task[0] == username_input for task in task_data):
                        print("No tasks have been assigned to you yet.\n")
                # View total number of tasks and users, only if you are admin
                elif menu == "ds" and username_input == "admin":
                    # Total task statistics
                    with open ("tasks.txt", "r") as file:
                        task_total = len(file.readlines())
                    # Total user statistics
                    with open ("user.txt", "r") as file:
                        user_total = len(file.readlines())
                    # Print statistics in readable format
                    print(
                        "\nTask and user statistics:" +
                        f"\nThere is a total of {task_total} tasks." + 
                        f"\nThere is a total of {user_total} users.\n" 
                    )
                # Exit program
                elif menu == "e":
                    print("\nGoodbye!!!")
                    exit()
                # Print error if invalid input made in menu
                else:                                                                    
                    print("\nInvalid menu selection. Please try again.")

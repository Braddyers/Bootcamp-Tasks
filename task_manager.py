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

# Prompt user to login using their username with corresponding password
while True:                                                                              

    # While username is not in dictionary, prompt again 
    username_input = input("\nEnter your username: ")
    if username_input not in usernames_passwords_dictionary:
        print("\nThat username does not exist. Please try again.")

    # ADD elif blank "" input check

    # If username is in dictionary, prompt for password
    else:
        password_input = input("\nEnter your password: ")

        # While the password does not match in dictionary, prompt again
        while password_input != usernames_passwords_dictionary[username_input]:
            print("\nIncorrect password. Please try again.")
            password_input = input("\nEnter your password: ")

        # If password matches, move to menu loop
        else:
            print(f"\nWelcome to your Task Manager {username_input}!")

            # =====Menu Section===== #
            
            # ADD admin menu:
            # add and remove admin permissions for other users
            # add view overdue tasks option

            # ADD seperate menu for users and not admin:
            # remove register user
            # remove add task 

            # Initialise menu loop
            while True:
                menu = input(
                            " ________________________________________\n" +
                            "|______________>>> Menu <<<______________|\n" +
                            "|                                        |\n" +
                            "|    r   =   Register user               |\n" + 
                            "|    a   =   Add task                    |\n" +
                            "|    va  =   View all tasks              |\n" + 
                            "|    vm  =   View my tasks               |\n" +
                            "|    e   =   Logout                      |\n" +
                            "|________________________________________|\n" +
                            "|________________________________________|\n" +
                            "\nPlease enter one of the above options: "
                            ).lower()

                # Register user
                if menu == "r":                                 

                    # Additional check if username already exists
                    with open("user.txt", "r") as file:
                        for line in file:
                            usernames, passwords = line.split(", ")                                         
                            usernames_passwords_dictionary[usernames] = passwords.replace("\n", "")

                    # Ask user for new username
                    new_username = input("\nEnter new username: ")

                    # ADD blank "" input check

                    # While new user name input is in dictionary, prompt until it is not 
                    while new_username in usernames_passwords_dictionary:
                        print("\nThat username already exists. Please choose a different username.")
                        new_username = input("\nEnter new username: ")

                    #ADD password length, symbol and letter check

                    # Ask for new password and ask to confirm password
                    # Ask again for both if there is a typo
                    new_password = input("\nEnter new password: ")
                    confirm_password = input("\nEnter it again to confirm the new password: ")

                    # Password confirmation, ask until there is a match
                    while confirm_password != new_password:                
                        print("\nPasswords do not match. Please try again.")                                
                        new_password = input("\nEnter new password: ")
                        confirm_password = input("\nEnter it again to confirm the new password: ")

                    # Let user know its confirmed, then back to menu
                    print("\nNew user registered! Now back to the menu.\n") 

                    # Write input to user.txt file
                    with open("user.txt", "a") as file:
                        file.write(f"\n{new_username}, {new_password}")

                # Add task to tasks.txt
                elif menu == "a":

                    # Open up-to-date user.txt file for additional check below
                    with open("user.txt", "r") as file:
                        for line in file:
                            usernames, passwords = line.split(", ")                                         
                            usernames_passwords_dictionary[usernames] = passwords.replace("\n", "")

                    # Request for 4 inputs for task data items:

                    # 1 - tasked user name
                    tasked_user = input("\nWhat is the username of the person you are assigning a task to?\n\n")

                    while True:
                        #REWORK

                        # If nothing was entered, prompt again
                        if tasked_user == "":
                            tasked_user = input(
                                                "\nYou did not enter anything. " +
                                                "\nWhat is the username of the person the task is assigned to?\n\n"
                                                )

                        # Or if user name not in dictionary, prompt again
                        elif tasked_user not in usernames_passwords_dictionary[usernames]:
                            print("\nPlease enter .\n")
                            tasked_user = input("\nUsername not found in system. Please try again" +
                                                "\nWhat is the username of the person the task is assigned to?\n\n")

                        else:
                            # 2 - Prompt task title input
                            task_title = input("\nWhat is the task's title?\n\n")

                            # If they enter nothing, prompt again
                            while task_title == "":
                                print("\nYou did not enter anything.")
                                task_title = input("\nWhat is the task's title?\n\n")   

                            # 3 - Prompt task description input
                            task_description = input("\nWhat is the task description?\n\n")

                            # If nothing entered, prompt again
                            while task_description == "":
                                print("You did not enter anything.")
                                task_description = input("\nWhat is the task description?\n\n")

                            #4 - Prompt for date input
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

                    # Initialize list for task data
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

                        # EDIT task output design

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
                                f"Task description:\n{task_description}\n" + 
                                "_________________________________________________________________________" +
                                "_______________________________________\n"
                                )

                    # Print message if no tasks for current logged in user
                    if not any(task[0] == username_input for task in task_data):
                        print("No tasks have been assigned to you yet.\n")

                # Exit program
                elif menu == "e":
                    print("\nGoodbye!!!")
                    exit()

                # ADD blank "" input check

                # Print error if invalid input made in menu
                else:                                                                    
                    print("\nInvalid menu selection. Please try again.")

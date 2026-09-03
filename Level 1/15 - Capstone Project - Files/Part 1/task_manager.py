# =====Importing Libraries Section===== #

from datetime import datetime

# =====Login Section===== #

# Initialise dictionary for usernames and passwords
usernames_passwords_dictionary = {}

# Open user.txt and put contents into dictionary (key are usernames, values are passwords)
# CREATE FUNCTIONS/CLASSES (def) FOR READING AND EDITING TEXT FILES
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
            
            # ADD to admin menu:
            # View overdue tasks, and add == "admin"
            # View completed, 
                # and add username_input == "admin" to both


            # Initialise menu loop
            while True:

                if username_input == "admin":
                    menu = input(
                                " ________________________________________\n" +
                                "|______________>>> Menu <<<______________|\n" +
                                "|                                        |\n" +
                                "|    r   =   Register user               |\n" + 
                                "|    at  =   Add task                    |\n" +
                                "|    mt  =   View my tasks               |\n" +
                                "|    va  =   View all tasks              |\n" + 
                            #   "|    ct  =   View completed tasks        |\n" +
                            #   "|    ot  =   View overdue tasks          |\n" +
                                "|    l   =   Logout                      |\n" +
                                "|________________________________________|\n" +
                                "|________________________________________|\n" +
                                "\nPlease enter one of the above options: "
                                ).lower()

                # Add:
                # Outstanding task option, 
                # User task is completed, then change "no" to "yes", 
                    # and to both add username_input != admin
                    # and add print("back to main menu")
                else: 
                    menu = input(
                                " ________________________________________\n" +
                                "|______________>>> Menu <<<______________|\n" +
                                "|                                        |\n" +
                            #   "|    x   =   View oustanding tasks       |\n" + 
                            #   "|    tc  =   Task completed              |\n" + 
                                "|    mt  =   View my tasks               |\n" +
                                "|    l   =   Logout                      |\n" +
                                "|________________________________________|\n" +
                                "|________________________________________|\n" +
                                "\nPlease enter one of the above options: "
                                ).lower()

                # Register user
                if menu == "r" and username_input == "admin":                                 

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
                elif menu == "at" and username_input == "admin":

                    # Open up-to-date user.txt file for additional check below
                    with open("user.txt", "r") as file:
                        for line in file:
                            usernames, passwords = line.split(", ")                                         
                            usernames_passwords_dictionary[usernames] = passwords.replace("\n", "")

                    # Request for 4 inputs for task data items:

                    # 1 - Tasked user's name
                    tasked_user = input("\nWhat is the username of the person you are assigning the task to?\n\n")

                    # Additional check if username in user list, only proceed if username already exists
                    while tasked_user not in usernames_passwords_dictionary:                                        
                        print("\nThat username does not exist. Please register that user before adding a task under their name.")    
                        tasked_user = input("\nWhat is the username of the person the task is assigned to?\n\n")    

                    # 2 - Task title
                    task_title = input("\nWhat is the task's title?\n\n")

                    # 3 - Task description
                    task_description = input("\nWhat is the task description?\n\n")

                    # 4 - Task due date and note time/date that task was assigned
                    while True:
                        raw_date_input = input("\nWhat is the task's due date (DDMMYYYY)?\n\n")
                        try:
                            parsed_date_input = datetime.strptime(raw_date_input, "%d%m%Y")
                            task_due_date = parsed_date_input.strftime("%d %b %Y")
                            break
                        except ValueError:
                            print("\nInvalid date format. Please try again.")
                    
                    # Assign timestamp when tasks were assigned items
                    current_date = datetime.now()
                    date_assigned = current_date.strftime("%d %b %Y")

                    # Assign "no" to variable, "no" = Task incomplete
                    completed_yes_no = "No"

                    # Write task data items to tasks.txt
                    with open("tasks.txt", "a") as file:
                        file.write(
                                f"\n{tasked_user}, {task_title}, {task_description}, {date_assigned}, {task_due_date}, {completed_yes_no}")

                    # Let user know its confirmed, then back to menu
                    print("\nNew task added! Now back to the menu.\n") 

                # View all tasks in tasks.txt
                elif menu == "va" and username_input == "admin":

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
                        # add task number (indexing capability)

                        # Required format
                        print(
                            "______________________________________________________" +
                            "_____________________________________________________\n\n" +
                            f"Task:                      {task_title}\n" + 
                            f"Assigned to:               {tasked_user}\n" + 
                            f"Date assigned:             {date_assigned}\n" + 
                            f"Due date:                  {task_due_date}\n" + 
                            f"Task Complete?             {completed_yes_no}\n" + 
                            f"Task description:\n\n" +
                            f"{task_description}\n" + 
                            "_______________________________________________________" +
                            "________________________________________________________\n"
                            )

                       

                # View tasks of current logged in user in tasks.txt
                elif menu == "mt":

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
                elif menu == "l":
                    print("\nGoodbye!!!")
                    exit()

                # ADD blank "" input check

                # Print error if invalid input made in menu
                else:                                                                    
                    print("\nInvalid menu selection. Please try again.")

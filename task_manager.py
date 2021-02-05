# This is a Task Manager application which is designed to help team members manage tasks which are assigned to them.

# Import date class from datetime module
from datetime import date

# Returns the current local date
today = date.today()

print("TASK MANAGER LOGIN\n---------------------------------")
# This section is the login and it loops through all usernames and passwords to check if valid.
logged_in = False
back_to_menu = False
has_tasks = False
admin = "admin, adm1n"

# Ask user to login inputting username and password.
while logged_in == False:
    user = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    for line in open("user.txt", "r").readlines():
        login_info = line.strip().split(", ")

        if user == login_info[0] and password == login_info[1]:
            logged_in = True
            detect_users_tasks = login_info[0]
            logged_in_user = login_info[0] + ", " + login_info[1]

    if logged_in == False:
        print("\nInvalid entry, please try again.\n")

# This loop is to allow a user to select an option until they choose to exit (e).
selection = ""

while selection.lower() != "e":
    # This checks to see if the user is the admin and displays the admin menu.
    if logged_in_user == admin:
        print("""
            TASK MANAGER - ADMIN
            ---------------------------------
            What would you like to do next?
            ---------------------------------
            r - Register a user
            a - Add a task
            va - View all tasks
            vm - View my tasks 
            vs - View statistics
            e - Exit program               
                    """)
    else:
        # If the user is not admin, they will be given the menu below.
        if logged_in_user != admin:
            print("""
            TASK MANAGER
            ---------------------------------
            What would you like to do next?
            ---------------------------------
            a - Add a task
            va - View all tasks
            vm - View my tasks 
            e - Exit program        
            """)

    # If user inputs (r) run the following code.
    selection = input("Type your selection: ")

    # R - Registering a new user, this functionality is only available to admins.
    if selection == "r" and logged_in_user == admin:
        back_to_menu = False
        password_match = False

        user_file = open("user.txt", "a+")
        print("\nREGISTER A NEW USER\n---------------------------------")

        while password_match == False:
            user = input("Enter new username: ")
            password = input("Enter password: ")
            password_check = input("Re-enter password: ")

            if password == password_check and password != "":
                password_match = True
                user_file.write(f"\n{user}, {password}")
                print("\nYou have successfully added a new user.\n")
            else:
                password_match = False
                print("Passwords do not match, please try again.")

        user_file.close()

        # Back to menu Loop.
        while back_to_menu == False:
            main_menu = input("Return to main menu type (mm) and ENTER: ")
            if main_menu == "mm":
                back_to_menu = True
            if main_menu != "mm":
                print("\nInvalid input, please try again.\n")

        continue

    # A - The user can add a new task entry here.
    elif selection == "a":
        back_to_menu = False

        # Opens tasks.txt so data can be written to it after user input.
        task_file = open("tasks.txt", "a+")
        print("\nADD NEW TASK\n---------------------------------")
        # Asks user to input all the data for the task.
        user = input("Who is this task for:\t")
        task_title = input("Give the task a title:\t")
        task_assigned_date = today
        task_due_date = input("Due date (yyyy-mm-dd):\t")
        is_completed = "No"
        task_description = input("Give the task a description:\t")
        print("---------------------------------")

        # Writes the data to tasks.txt
        task_file.write(
            # Used the '$' to divide the data in case a comma or semi colon is used in the description.
            f"{user}$ {task_title}$ {task_description}$ {task_assigned_date}$ {task_due_date}$ {is_completed}\n")

        print("\nYour task has been successfully saved.\n")
        task_file.close()

        # Back to menu Loop.
        while back_to_menu == False:
            main_menu = input("Return to main menu type (mm) and ENTER: ")
            if main_menu == "mm":
                back_to_menu = True
            if main_menu != "mm":
                print("\nInvalid input, please try again.\n")

        continue

    # VA - This displays the tasks assigned to all the users.
    elif selection == "va":
        back_to_menu = False

        # Opens tasks.txt so we can read the data collected.
        task_file = open("tasks.txt", "r")
        print("\nALL TASKS\n---------------------------------")

        # Splits the string of each task by variable name.
        for line in task_file:
            user, task_title, task_description, task_assigned_date, task_due_date, is_completed = line.split("$ ")
            # This removes the newline after the is_completed.
            is_completed = is_completed.rstrip("\n")
            # Prints out all the tasks for the user.
            print(f"""
            Task title:\t\t{task_title}
            Assigned to:\t\t{user}
            Date assigned:\t\t{task_assigned_date}
            Due date:\t\t{task_due_date}
            Task completed:\t\t{is_completed}
            Task description:\n{task_description}\n
            ---------------------------------
            """)
        task_file.close()

        # Back to menu Loop.
        while back_to_menu == False:
            main_menu = input("Return to main menu type (mm) and ENTER: ")
            if main_menu == "mm":
                back_to_menu = True
            if main_menu != "mm":
                print("\nInvalid input, please try again.\n")

        continue

    # VM - Displays only the logged in user's tasks.
    elif selection == "vm":
        back_to_menu = False

        # Opens tasks.txt so we can read the data collected.
        task_file = open("tasks.txt", "r")
        print("\nMY TASKS\n---------------------------------")

        while has_tasks == False:
            # Splits the string of each task by variable name.
            for line in task_file:
                user, task_title, task_description, task_assigned_date, task_due_date, is_completed = line.split("$ ")
                # This removes the newline after the is_completed.
                is_completed = is_completed.rstrip("\n")
                # Prints out only the user's tasks, if they have any.
                if user == detect_users_tasks:
                    print(f"""
                    Task title:\t\t{task_title}
                    Assigned to:\t\t{user}
                    Date assigned:\t\t{task_assigned_date}
                    Due date:\t\t{task_due_date}
                    Task completed:\t\t{is_completed}
                    Task description:\n{task_description}\n
                    ---------------------------------
                    """)
                    has_tasks = True

            if has_tasks == False:
                # If no tasks match the username and admin, then display this message.
                print("You have no tasks!\n")

        task_file.close()

        # Back to menu Loop.
        while back_to_menu == False:
            main_menu = input("Return to main menu type (mm) and ENTER: ")
            if main_menu == "mm":
                back_to_menu = True
            if main_menu != "mm":
                print("\nInvalid input, please try again.\n")

        continue

    # S - Displays the user and task statistics, this functionality is only available to admins.
    elif selection == "vs" and logged_in_user == admin:
        back_to_menu = False
        task_file = open("tasks.txt", "r")
        user_file = open("user.txt", "r")
        num_tasks = 0
        num_users = 0

        print("\nSTATISTICS\n---------------------------------")

        # Open the task file and read the lines to calculate the total number of tasks.
        content = task_file.read()
        task_list = content.split("\n")
        for i in task_list:
            if i:
                num_tasks += 1
        print(f"Total number of tasks:\t {num_tasks}")
        task_file.close()

        # Open the users file and read the lines to calculate the total number of users.
        content = user_file.read()
        user_list = content.split("\n")
        for i in user_list:
            if i:
                num_users += 1
        print(f"Total number of users:\t {num_users}\n---------------------------------\n")
        user_file.close()

        # Back to menu Loop.
        while back_to_menu == False:
            main_menu = input("Return to main menu type (mm) and ENTER: ")
            if main_menu == "mm":
                back_to_menu = True

            if main_menu != "mm":
                print("\nInvalid input, please try again.\n")

        continue

    # E - Exits the application.
    elif selection == "e":
        print("Goodbye!")
        exit(0)
        break

    # If the user types in a wrong option, they will be shown this error message and loop back to the main menu.
    else:
        print("Invalid input, please try again.\n")
        continue


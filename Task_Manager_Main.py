# This program will provide assistance for a small business
# that can help it to manage tasks assigned to each member of the team

# ======Updates to file============
# Ammended the menu to add in additional section if the user is an admin
# Updated variable names
# Added new functions editing files &
# for viewing user and task statistics 
# 10/03/2022  -Updated login code
# Changed code to update user_overview each time a date is changed or assigned user is changed..
# 12/03/22
# Edited the task overview file writing code
# Updated the percentage calculation for both task and user overview


# =====importing libraries===========
# Import datetime libraries for recording current date
from datetime import datetime

assigned_date = datetime.today().strftime('%d %b %Y')

# ======Functions======================
# Function to register a new user
def reg_user():
    user_file = open('user.txt', 'r+')

    # Requesting user input
    new_user = (input('Please enter a new user name: '))
    user_registered = False

    # Looping until user is registered 
    while not user_registered:
        for lines in user_file.readlines():

            # Strip the white spaces between words
            # Split the words by the comma and a space
            # Using index slicing to create a temporary column for usernames and passwords in the file
            temp = lines.strip()
            temp = temp.split(', ')
            user_name_saved = temp[0]

        if user_name_saved == new_user:
            print('\n This username already exists, please enter a new 1 \n')
            reg_user()

        if new_user != user_name_saved:
            new_user_password = (
                input('Please enter a new password: '))

            # Add a 'while loop' untill the condition is met(True).
            # Admin user is requested to enter the password twice
            # Only if both passwords match will the data be saved to the user.txt file.    
            new_password = False
            while new_password == False:


                confirm_new_password = input(
                    'Please retype your password to confirm: ')

                if new_user_password == confirm_new_password:
                    new_password = True
                    user_registered = True
                    print(' \n User has been successfully registered \n')       

                    # Close file
                    user_file.write(f'\n{new_user}, {new_user_password}')

                elif new_password == False:
                    print('Your passwords do not match!')

    # End of function
    user_file.close()


# View_all function prints out all tasks for all users
def view_all():

    task_file = open('tasks.txt', 'r')

    # Looping through each line item, splitting it
    # Using list comprehension to create variables for each index in list
    for line in task_file:

        # Split data from file by comma
        project_number, task_username, task_title, task_description, task_due_date, assigned_date, completed = line.split(
            ', ', maxsplit=7)

        # Formatting the print display for an easy to read view and printing data
        print(f'''
        
        New task username:      {task_username}
        Task tile:              {task_title}
        Task description:       {task_description}
        Task due date:          {task_due_date}
        Assigned Date:          {assigned_date}
        Completed:              {completed}
        ''')

    # End of function, closing file
    task_file.close()

# This function will allow a user to mark a task as complete
def mark_as_complete():

    # Open tasks file
    with open('tasks.txt', 'r+') as tp:

        original_list = tp.readlines()

        # User input is used as index less 1
        list_of_lines = original_list[user_input-1]
        print(list_of_lines)
        
        # Initialize a new list
        new_line=[]
        
        # Loop through the index of each list
        for i in list_of_lines:

            # replacement carries the value
            # of the text to be replaced
            replacement = list_of_lines.replace('No', 'Yes')
            
            # Contains the full line of data with the new word
            l = replacement

        # Append all data to new list 
        new_line.append(replacement)

        # Inserts new line into original list index location
        original_list.insert(user_input,str(l))
        updated_tasks=original_list

        # Delete the original line in file as indicated by the index
        del updated_tasks[user_input-1]

    # Open the file and overwrite all lines of data to it
    file_out= open('tasks.txt','w+')
    
    for items in original_list:
        file_out.write('%s' %items)

    # End of function, close file
    file_out.close()

    print('\n The task has been successfully updated! Thank you ')
    update_userview()

# Function to edit user name within the task file
def edit_user_name():

    # Request user for input on the project number
    edit_task =int(input('Enter the number of the task you wish to update: \n '))

    # Open file
    with open('tasks.txt', 'r+') as tp:
        
        # Declare variable for readlines
        original_list = tp.readlines()

        # Locate correct index by subtracting user number by 1
        list_of_lines = original_list[edit_task-1]

    # Initilize list
    new_line=[]
    
    # Present user with the current user and request to insert new user name
    print(f'Enter the name of the current user assigned to task {edit_task} ')

    current_user_name=input('Type here: ')
    new_user_name=input('Enter in the new user name: ')

    for i in list_of_lines:

        # replacement carries the value
        # of the text to be replaced
        # Swap variables
        replacement = list_of_lines.replace(current_user_name, new_user_name)
        l = replacement
    new_line.append(l)

    # Insert line from list into variable that reads the lines or list
    # Line will get inserted directly below the original line
    original_list.insert(edit_task,str(l))
    updated_tasks=original_list

    # Delete old list with use of variable less 1, previous line in file will get deleted
    del updated_tasks[edit_task-1]

    # Write data to file
    file_out= open('tasks.txt','w+')
    for items in original_list:

        # %s for writing all string values into file
        file_out.write('%s' %items)
    file_out.close()    

    # End of function
    print('User name changed successfully')

    update_userview()

# Function to assist user in changing the due date of a task
def change_due_date():

    # Request user input
    edit_task =int(input('Enter the number of the project you wish to update: '))

    with open('tasks.txt', 'r+') as tp:

        # Read lines from file
        original_list = tp.readlines()

        # Get index of line from user less 1
        list_of_lines = original_list[edit_task-1]

        # Split file on comma
        project_number,task_username, task_title, task_description, task_due_date, assigned_date,completed = list_of_lines.split(
            ',', maxsplit=7)

        # Print all tasks for user to view
        print(f'''
                Project Number:         {project_number}
                New task username:      {task_username}
                Task tile:              {task_title}
                Task description:       {task_description}
                Task due date:          {task_due_date}
                Assigned date:          {assigned_date}
                Completed:              {completed}
                    ''')

        for list_of_lines in tp:

            
            list_of_lines = list_of_lines.split(', ')
            task_due_date = list_of_lines[4]
        
        # Printing it out to confirm last word in str
            print(list_of_lines[4])
        new_line=[]
            
        print(f'Enter the current due date for task number {edit_task} as displayed above ')
        current_due=input("Type here (format '12 Sep 2000'): ")
        new_due_date=input("Enter in the new due date in this formatt: 10 Sep 2020': ")
        for i in list_of_lines:

            # replacement carries the value
            # of the text to be replaced
            replacement = list_of_lines.replace(current_due, new_due_date)
            l = replacement
        new_line.append(replacement)


        original_list.insert(edit_task,str(l))
        updated_tasks=original_list
        
        # Delete old list with use of variable less 1, previous line in file will get deleted
        del updated_tasks[edit_task-1]


        file_out= open('tasks.txt','w+')
        for items in original_list:

            # %s for writing all string values into file
            file_out.write('%s' %items)
        file_out.close()    
    update_userview()

def task_overview():
       
    # Call function to get count of tasks
    task_count = Number_of_tasks()

    # Initialise counters
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_count=0

    # Get todays date
    today = datetime.today().date()

    # Open file to read the last index 'No' or 'Yes'
    tasks_file = open('tasks.txt', 'r')
    for line in tasks_file.readlines():
        list_of_lines = line.split(', ')
        
        # Declarings variables for indices
        task_due_date = list_of_lines[4]
        completed = list_of_lines[6].strip()
    tasks_file.close() 
    

    task_overview_file = open('task_overview.txt','w')

    # Create loop in order to get counts for index
    with open('tasks.txt','r') as tasks_file:
        for list_of_lines in tasks_file.readlines():

            list_of_lines = list_of_lines.split(', ')
            completed = list_of_lines[6].strip()      

            if completed == 'Yes':
                completed_tasks +=1
            else:
                
                incomplete_tasks +=1
                date_string = task_due_date

                # Converting the str into object
                date_object = datetime.strptime(date_string,'%d %b %Y').date()
                
                # Doing comparison with todays date
                if date_object > today:
                    overdue_count+=1 

        # Calculate percentages
        percentage_overdue=(overdue_count/task_count)
        percentage_incomplete=(incomplete_tasks/task_count)

        task_overview_file.write(f'''
        Statistics of the tasks \n
        Column header                        Statistics
        The total number of tasks       :           {task_count}
        Number of completed tasks       :           {completed_tasks}
        Number of incomplete tasks      :           {incomplete_tasks}
        Overdue and Incomplete          :           {overdue_count}
        Percentage of incomplete tasks  :           {percentage_incomplete:.0%}
        Number of overdue tasks         :           {percentage_overdue:.0%}
        ''')
        
        task_overview_file.close()


# This function will read the task and user file , and write the data in an easy to  user_overview.txt
def display_stats():

    # Total number of tasks and users
    # Initiliaze counters
    num_of_users = 0
    num_of_tasks = 0
    task_file=open('tasks.txt','r')
    user_file= open('user.txt', 'r')

    # Loop through each line to count the total number of registered users
    for line in user_file:
        num_of_users += 1

    # Loop through each line to count number of total number of tasks
    for line in task_file:
        num_of_tasks += 1

    # Write data to file, using 'w' to clear contents of file before writing new data
    with open('user_overview.txt','w') as user_overvew_file:
      
        user_overvew_file.write(f'''\n      
            See below task statistics \n
        Description                             Count
    Total number of tasks generated  :          {num_of_tasks}
    Total number of users registered :          {num_of_users}''')

    # Closing both files
    task_file.close()
    user_file.close()


# Function to get the num_of_tasks and pass it to user_overview
def Number_of_tasks():
    num_of_tasks = 0
    with open('tasks.txt','r') as task_file:
        
        for line in task_file:
            num_of_tasks+= 1
        return num_of_tasks
# End of function


# Function to collect and write user data stats
def user_overvew(username):

    # Declare variable from display_stats function
    num_of_tasks=Number_of_tasks()

    # Importing modules
    from datetime import date
    today = date.today()
    user_name_count=0
    user_task_incomplete =0
    user_task_complete = 0
    task_count = 0
    overdue_count = 0

    #user_overvew_file=open('user_overview.txt','w')
    with open('tasks.txt', 'r') as tasks_file:
        for list_of_lines in tasks_file.readlines():

            task_count +=1
        
            list_of_lines = list_of_lines.split(', ')
            task_username = list_of_lines[1].strip()
            task_due_date = list_of_lines[4]
            assigned_date = list_of_lines[5]
            completed = list_of_lines[6].strip()        

            if username == task_username:
                user_name_count += 1


                # Check case value
                if completed == 'Yes':
                    user_task_complete += 1


                else:
                    completed == 'No'
                    from datetime import datetime

                    date_string = task_due_date

                    # Converting the str into object
                    date_object = datetime.strptime(date_string,'%d %b %Y').date()
                    
                    # Doing comparison with todays date
                    if date_object < today:
                        overdue_count+=1 

                    else:
                        pass

        # Working our percentages of data
        overdue_incomplete=(overdue_count / user_name_count)
        total_task_percentage= (user_name_count / num_of_tasks)
        completed_percentage =(user_task_complete / user_name_count)
        incomplete_percentage = (user_task_incomplete / user_name_count  )


        with open ('user_overview.txt','a') as user_overview_file:

            user_overview_file.write(  f'''\n
                        Statistics for user {username}                               
    The total number of tasks       :           {user_name_count}
    The percentage of the total 
    amount of tasks which have been :           {total_task_percentage:.0%}
    assigned is                                
    Percentage of completed tasks   :           {completed_percentage:.0%}
    Percentage of incompleted tasks :           {incomplete_percentage:.0%}
    Total number of tasks overdue & incomplete  {overdue_incomplete}\n''')
    
# End of function
def update_userview():
    listed_task_names=[]

    # Open file
    with open('tasks.txt', 'r') as task_file:
        for list_of_lines in task_file.readlines():
            
            # SPlit data and declare variables
            list_of_lines = list_of_lines.split(', ')
            project_number = list_of_lines[0]
            task_username = list_of_lines[1].strip()
            listed_task_names.append(task_username)

        # Add user from file to list,
        # Using 'set' to remove duplicate usernames
        unique_user_list=set(listed_task_names)
    
    # Loop through list - for each user 
    for i in unique_user_list:
        user_overvew(i)  

        
# =====Login==========================
# Declaring variables for the while loop to run
logged_in = False

# Creating empty string variable that will be assigned new values
# Opening the file containing the registered usernames and passwords
user_name_saved = ''
password_saved = ''
user_file = open('user.txt', 'r')

# The loop will continue to request a user to login until
#  a user contained in the User.txt file logs in


while not logged_in:

    # Request user for input within the loop, so that it can continue requesting input
    # login_user = input('Kindly enter your username: ')

    login_user = input('Enter your username: ')
    login_pass = input('Enter your password: ')
    user = login_user + ', ' + login_pass

    if user in user_file.read():
        print('\n Logging successful \n Welcome to the task manager \n')
        logged_in = True
        break

    else:
        print('\n Incorrect username or password \n Please try again \n')
        login=False

user_file.close()

# New loop for logged in user
while True:

    if login_user != 'admin':
        # presenting the standard_menu to the user and
        # making sure that the user input is converted to lower case.
        standard_menu = input('''Select one of the following Options below:
        r  - Registering a user
        a  - Adding a task
        va - View all tasks
        vm - View my task

        e - Exit:
    ''').lower()

    if login_user == 'admin':
        # presenting the admin standard_menu to the user
        standard_menu = input('''Select one of the following Options below:
        r   -   Registering a user
        a   -   Adding a task
        va  -   View all tasks
        vm  -   View my task
        gr  -   Generate reports
        ds  -   Display statistics 
        e   -   Exit:
    ''').lower()

    # Setting a condition which will only allow the 'admin' user access to register a user
    if standard_menu == 'r':
        if login_user != 'admin':

            print('\n You are not an admin user, only admin can register new users. \n')

        elif login_user == 'admin':
            reg_user()

    # standard_menu item to add a task
    # Logged in user will be requested to enter some data
    # Data will be stored into the tasks.txt file
    elif standard_menu == 'a':
        pass

        user_name_task = input('Enter in the username: ')
        user_task_title = input('Enter in the title of the task: ')
        user_task_descrip = input('Enter in the description of the task: ')
        task_due_date = input('Enter in the due date: ')

        with open('temp_tasks.txt', 'a') as tasks:

            tasks.write(
                ('{}, {}, {}, {}, {}, No \n'.format(user_name_task, user_task_title, user_task_descrip, task_due_date, assigned_date)))

            print('\n Task has been successfully added!')

        # Open the original task file and write all data
        # to task_overview adding in the project number.
        task_file = open('tasks.txt', 'w')
        with open('temp_tasks.txt', 'r+') as temp_task_file:
            count = 0
            for line in temp_task_file:
                count += 1

                new_task_username, new_task_tile, new_task_description, new_task_due_date, assigned_date, completed = line.split(
                    ', ', maxsplit=5)

                task_file.write(str(count) + ', ' + new_task_username + ', ' + new_task_tile + ', ' + new_task_description + ', ' +
                                    new_task_due_date + ', ' + assigned_date + ', ' + completed)
        task_file.close()

    # standard_menu item which will allow the logged in user to view all the tasks
    # which are assigned to every user
    elif standard_menu == 'va':
        pass
        view_all()

    # standard_menu item to view the tasks assigned to the currently logged in user
    elif standard_menu == 'vm':


        with open('tasks.txt', 'r') as task_file:

            print('\n Listed below are all your tasks: \n')

            for line in task_file.readlines():
                project_number, task_username, task_tile, task_description, task_due_date, assigned_date, completed = line.split(
                    ', ', maxsplit=7)

                # Condition to check which user is actually logged in
                if login_user == task_username:

                    # Formatting the print display for an easy to read view
                    print(f'''
                    Project Number          {project_number}
                    New task username:      {task_username}
                    Task tile:              {task_tile}
                    Task description:       {task_description}
                    Task due date:          {task_due_date}
                    Assigned date:          {assigned_date}
                    Completed:              {completed}
                    ''')

        
            print('Would you like to update a task or return to the main menu?')


            choice = int(input('''
            Select from the below options:
            1.Edit a task
            -1. Return to the main menu
            '''))

            if choice == 1:

                print('''Choose from the below options:
                1.Update the Project status
                2.Edit the task''')
                
                # Present user options
                user_choice=int(input('Enter in your choice: '))

                if user_choice==1:
                    print('Enter the number of the project you wish to update: \n ')
                    user_input = int(input())

                    # Call function
                    mark_as_complete()
        
                elif user_choice==2:
                    print('''Select which items in the tasks to update: \n
                            1. User name
                            2. Due Date
                        ''')
                    edit_options =int(input('Enter in your selection: '))

                    if edit_options == 1:

                        # Call function
                        edit_user_name()
                        

                    elif edit_options == 2:

                        # Call function
                        change_due_date()
                    else:
                        print(' You have entered a wrong choice')
                    
            elif choice == -1:
                pass
            else:
                print('You have entered an incorrect selection, please try again')
                pass
    elif standard_menu == 'ds':
            if login_user != 'admin':

                print('\n You are not an admin user, only admin view statistics. \n')

            elif login_user == 'admin':
            # These varibles will only count the lines inside the 'txt' files,
            #     # but since we are storing every new task & user on a new line,
            #     # we can just count the lines for the desired results.
                num_of_tasks = 0
                num_of_users = 0

                with open('tasks.txt', 'r') as task_file:
                    for line in task_file:
                        num_of_tasks += 1
                print('\n See below statistics: \n')
                print(f'\nTotal number of tasks: {num_of_tasks}')

                with open('user.txt', 'r') as user_file:
                    for line in user_file:
                        num_of_users += 1
                print(f'Total number of users: {num_of_users}\n')

    elif standard_menu == 'gr':
        
        # Call function 
        task_overview()
        display_stats()

        # Initialize list
        listed_task_names=[]

        # Open file
        with open('tasks.txt', 'r') as task_file:
            for list_of_lines in task_file.readlines():
                
                # SPlit data and declare variables
                list_of_lines = list_of_lines.split(', ')
                project_number = list_of_lines[0]
                task_username = list_of_lines[1].strip()
                listed_task_names.append(task_username)

            # Add user from file to list,
            # Using 'set' to remove duplicate usernames
            unique_user_list=set(listed_task_names)
        
        # Loop through list - for each user 
        for i in unique_user_list:
            user_overvew(i)
        
        print('\n Files have been generated: user_over and task_overview \n')

    elif standard_menu == 'e':
        print('Goodbye!!!')

        exit()

    # Print the below message,if the user enters a value that is not listed in the menu
    else:
        print('You have made a wrong choice, Please Try again')

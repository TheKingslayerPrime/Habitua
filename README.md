# Habitua

# PROJECT OVERVIEW:
Introduction: 
Welcome to the Habitua website! Our objective is to create a MindGrowth and Personal Development Tracker. Through this website, users can seamlessly navigate through and use the various personal development tools provided to assist them in their daily/monthly tasks and habit development journey. The website contains a habit tracker, to-do list for daily and month tasks, pomodoro timer and a cat mascot. The cat mascot will appear hungry or satisfied based on the state of the tasks given. Once the tasks are completed in an orderly manner and within the specified time, coins will be credited to the user which can be used to buy food and toys from the shop. These will then be used to feed the cat or let it play with it, which will manipulate the happiness or health of the mascot, depending upon the type of item. 

The on-site shop sells food and items, which are further categorized into 3 qualitiy types- "bad", "normal" and "good". The health and happiness meter will be updated depending upon the quality of the item given to the mascot. Providing the cat with good will increase/decrease its heath meter while the happiness meter will be changed if toys are given to the cat. If good habits are maintained, coins will be accredited to the user and if bad habits are not reduced or maintained then coins will be deducted and the cat loses health and happiness. Similarly, completion of tasks lead to accredition of coins and missing out or late completion leads to deduction of the same.

This project aims to gamify completion of tasks and gaining/reduction of good or bad habits. It works on the principle of minor dopamine rushes caused due to petting or interacting with the mascot. This provides the user incentive to complete tasks, while not completing tasks or continuing with bad habits decreases the health and happiness meter of the cat, which guilt-trips the user to finish their work efficiently. The mascot can also be changed from a cat (default) to any animal of the user's choice (to be implemented later).

A pomodoro clock is placed on the website to allow the user to take quick breaks between focus periods. Pomodoro method works on 25 minutes of focus period for the user to "focus" on their work and finish it before taking a much needed 5 minutes break between the next focus period. The user can start the clock timer and reset it when required. 

Key Features of the Website:
1. Login/Sign Up Page- Users can use the beautifully designed login page to log in to the Habitua dashboard.
2. To-Do Task List- Users can list down their daily/monthly tasks in the task list to keep a track of them in an orderly manner.
3. Habits List- Users can note down new habits to develop or old tasks which they want to leave and track of them in an efficient manner.
4. Pomodoro Timer - The Habitua dashboard also features a pomodoro timer for time tracking set to 25 minutes which can be reset when requied.
5. Cat Mascot - The dashboard also features a well designed cat mascot to motivate the user to complete their tasks. When the tasks are not completed, the mascot appears hungry and unsatisfied and upon completion, it appears healthy and satisfied.

Technologies used: 
1. Python Flask - Python flask is a light web framework used for building web applications and APIs in python.
2. HTML & HTMX - HTML and HTMX are used to make the skeletal structure of the webpages.
3. CSS - Basic CSS is used to style the website.
4. JavaSript - Vanilla JS is used to add interactivity to the Habitua dashboard.

# INSTALLATION GUIDE:
System Requirements:

1. Python Flask:
    a. Moden Operating System like Windows, Mac or Linux
    b. Stable release of Python
    c. Adequate disc space for Python and its required packages.
    d. Requires stable network access.

2. HTML & CSS:
    a. Modern web browser such as Firefox, Google Chrome, etc.
    b. A text editor like Notepad, Visual Studio Code, etc.
    c. Sufficient resources to run a web browser on the required device.

3. JavaScript: 
    a. Modern web browser such as Firefox, Google Chrome, etc.
    b. A text editor or IDE like Visual Studio Code, Sublime Text, Atom, and WebStorm.
    c. Requires stable network access.


Dependency installation steps : (FOR EACH OS)
1. Python (version 3.x):
    a. WINDOWS- 
        i. Open Command prompt or the Windows terminal.
        ii. Type `winget install python`
        iii. Use pip commands to install the required flask packages.
    b. Linux-
        i. Open the terminal of your choice.
        ii. Download python using the package manager provided in the system.
            For example - `sudo apt-get install python3`
        iii. Use `pip install <package-name>` to install the pip package for flask.
    c. MacOS-
        i. Open the terminal of your choice.
        ii. Download python using Homebrew using - `brew install python` command. 
        iii. Use `pip install <package-name>` to install the pip package for flask.

2. HTML, CSS and JavaScript can be written on any text editor or IDE and can be opened with any web browser such as Firefox, Google Chrome, etc.

Commands:
1. Manipulating Repositories:
    a. Use command `git clone <repository_url>` if you just want to copy into current directory. 
    b. Use command `git clone <repository_url> <directory_name>` to copy to a specific directory. 
    c. Use command `git add .` for staging the changed files.
    d. Use command `git commit -m "<description>"` for committing the changes.
    e. Use command `git status` to view the status of the commited files.
    f. Use command `git push` to push it to the repository.  

2. Creating Virtual Environment:
    a. WINDOWS-
        i. Use `python -m venv myenv` command in terminal to create virtual environment.
        ii. Use `myenv\Scripts\activate` command in terminal to activate virtual environment. 

    b. macOS-
        i. Use `python3 -m venv myenv` command in terminal to create virtual environment. 
        ii. Use `source myenv/bin/activate` command in terminal to activate vitual environment.  

    c. Linux-
        i. Use `python3 -m venv myenv` command in terminal to create virtual environment. 
        ii. Use `source myenv/bin/activate` command in terminal to activate vitual environment.

# USAGE:
1. The user will first sign up to the website where his details will be saved to a secure database. 
2. Upon signing up, login using the same credentials will be required. 
3. Upon successful login, the dashboard will open with a variety of services to offer. 
4. The user can set new tasks for themselves using the New Task option and can even set new habits to integrate into themselves using the New Habits option. 
5. A pomodoro clock displaying 25mins of focus period followed by 5 mins of break is also available for the user to focus on chosen task. 
6. A reward system is put in place where upon completion of a task, certain number of coins will be accredited to the user which can then be spent to feed the pet cat of the user or buy them toys. 
7. Each material has their own parameters which will affect the health and happiness of the cat. 
8. On the other side, not completing tasks or doing a negative habit will decrease the health and happiness of the cat, thus guilt tripping the user into working hard to better themselves. 
9. Users can logout from the page using the sign out option. 
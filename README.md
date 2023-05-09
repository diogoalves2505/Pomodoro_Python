# Pomodoro_Python
A pomodoro app in Python using Pygame for beginners 


This is a program that implements a Pomodoro timer with a graphical user interface using the Pygame library in Python. The user can select the length of the Pomodoro session and the length of the breaks. The program keeps track of the remaining time and updates a timer display on the screen. When the Pomodoro session ends, the program adds XP to the user's account and starts a new session. The user can also see their level on the screen, which increases when they accumulate 100 XP.

The program has a main loop that listens for user events, updates the display, and keeps track of the timer. The program uses the Button class to create buttons on the screen that the user can click to select the Pomodoro session or the break lengths, or to start or stop the timer. The program also writes the user's level and XP to a file called "level.txt" when the user exits the program.

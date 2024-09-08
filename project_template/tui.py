"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import process
# Annotation// taking text as argument
def annotation(text):
    # top and bottom lines/ one for every letter
    line = "-" * len(text)
    print(line)
    print(text)
    print(line)

annotation("DisneyLand Review Analyser")

#MAIN MENU
def menu(data):
    while True:
        opt = input("""Please enter The letter which corresponds with your desired menu choise:
[A]-View Data
[B]-Visualize Data
[X]-Exit\n\n""").upper()
        if  opt == "A":
            print(f"You have chosen option {opt}")
            sub_menu_a(data)
        elif opt == "B":
            print(f"You have chosen option {opt}")


        elif opt == "X":
            break
        else:
            print("No valid option! please enter correct letter.")

#SUBMENU A
def sub_menu_a(data):
    opt2 = input("""Please enter one of the following options\n\n
[A] - View Reviews by Park
[B] - Number of Reviews by Park and Reviewer Location
[C] - Average Score per Year by Park
[D] - Average Score per Park by Reviewer Location\n""").upper()

    if opt2 == "A":
        process.view_reviews_by_park(data)  # Function to view reviews by park
    elif opt2 == "B":   # Funtion for reviews by park and location
        process.number_of_reviews_by_park_and_location(data)

        pass
    elif opt2 == "C":
        #add coment when ready

        pass
    elif opt2 == "D":  #add comment when ready

        pass
    else:
        print("Wrong input! Please choose the correct option.")

#SUBMENU B
def sub_menu_b(data):
    opt3 = input("""Please enter one of the following options\n\n
[A] - Most Reviewed Parks
[B] - Average Scores
[C] - Park Ranking by Nationality
[D] - Most Popular Month by Park \n""").upper()

    if opt3 == "A":
        # Function to visualize reviews by park
        pass
    elif opt3 == "B":
        # Function to visualize Average scores
        pass
    elif opt3 == "C":
        # Function to visualize park ranking by nationality
        pass
    elif opt3 == "D":
        # Function to visualize most popular month by park
        pass
    else:
        print("Wrong input! Please choose the correct option.")



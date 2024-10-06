"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import process
import visual
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
            sub_menu_b(data)


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

    elif opt2 == "C":
        process.average_score_per_year_by_park(data)

    elif opt2 == "D":
        process.average_score_per_park_by_location(data)


    else:
        print("Wrong input! Please choose the correct option.")
        sub_menu_a(data)

#SUBMENU B
def sub_menu_b(data):
    opt3 = input("""Please enter one of the following options\n\n
[A] - Most Reviewed Parks
[B] - Average Scores
[C] - Park Ranking by Nationality
[D] - Most Popular Month by Park \n""").upper()

    if opt3 == "A":
        visual.most_reviewed_parks(data)

    elif opt3 == "B":
        visual.average_scores(data)

    elif opt3 == "C":
        visual.top_10_locations_by_rating(data)

    elif opt3 == "D":
        visual.average_rating_by_month(data)

    else:
        print("Wrong input! Please choose the correct option.")
        sub_menu_b(data)



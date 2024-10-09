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
from export import ParkDataExporter
# Annotation// taking text as argument
def annotation(text):

    line = "-" * len(text)
    print(line)
    print(text)
    print(line)

annotation("DisneyLand Review Analyser")

#MAIN MENU
def menu(data):
    while True:
        opt = input("""Please enter the letter which corresponds with your desired menu choice:
[A] - View Data
[B] - Visualize Data
[C] - Export Data
[X] - Exit\n\n""").upper()

        if opt == "A":
            print(f"You have chosen option {opt}")
            sub_menu_a(data)
        elif opt == "B":
            print(f"You have chosen option {opt}")
            sub_menu_b(data)
        elif opt == "C":
            print(f"You have chosen option {opt}")
            export_data_menu(data)
        elif opt == "X":
            print("Exiting the program.")
            break
        else:
            print("No valid option! Please enter the correct letter.")

#SUBMENU A
def sub_menu_a(data):
    opt2 = input("""Please enter one of the following options\n\n
[A] - View Reviews by Park
[B] - Number of Reviews by Park and Reviewer Location
[C] - Average Score per Year by Park
[D] - Average Score per Park by Reviewer Location
[E] - Average Score per Park by Reviewer Location \n""").upper()

    if opt2 == "A":
        process.view_reviews_by_park(data)
    elif opt2 == "B":
        process.number_of_reviews_by_park_and_location(data)
    elif opt2 == "C":
        process.average_score_per_year_by_park(data)
    elif opt2 == "D":
        process.average_score_per_park_by_location(data)
    elif opt2 == "E":
        process.average_score_per_park_by_location(data)
    else:
        print("Invalid option, please try again.")

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


def export_data_menu(data):
    print("\nExport Data:")
    print("[1] - Export to TXT")
    print("[2] - Export to CSV")
    print("[3] - Export to JSON")

    format_choice = input("Select an export format: ")

    exporter = ParkDataExporter(data)

    if format_choice == "1":
        exporter.export_to_txt('parks_report.txt')
        print("Data exported to parks_report.txt")
    elif format_choice == "2":
        exporter.export_to_csv('parks_report.csv')
        print("Data exported to parks_report.csv")
    elif format_choice == "3":
        exporter.export_to_json('parks_report.json')
        print("Data exported to parks_report.json")
    else:
        print("Invalid choice. Please try again.")



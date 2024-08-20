"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""


import csv
#csv file path
file_name = "disneyland_reviews.csv"
#list to store the data

data = []
#read data from file


# Annotation// taking text as argument
def annotation(text):
    # top and bottom lines/ one for every letter
    line = "-" * len(text)
    print(line)
    print(text)
    print(line)

annotation("DisneyLand Review Analyser")
#Reading data from the file and / informing user how many rows
def reading():
    data=[]
    with open("data/disneyland_reviews.csv", "r") as f:
        reader = csv.reader(f)
        nr_rows = 0
        for row in reader:
            data.append(row)
            nr_rows += 1

        print("Data set for 'disneyland_reviews.csv' has been uploaded.")
        print(f"There is {nr_rows} in the dataset.")
    return data
# Main menu
def menu():
    while True:
        opt = input("""Please enter The letter which corresponds with your desired menu choise:
[A]-View Data
[B]-Visualize Data
[X]-Exit\n\n""").upper()
        if  opt == "A":
            print(f"You have chosen option {opt}")
            sub_menu_a()
        elif opt == "B":
            print(f"You have chosen option {opt}")


        elif opt == "X":
            break
        else:
            print("No valid option! please enter correct letter.")
def sub_menu_a():
    opt2 = input("""Please enter one of the following options\n\n
[A]-View Reviews by park
[B]-Number of Reviews by Park and Reviewer Location
[C]-Average Score per year by Park
[D]-Average Score per Park by Reviewer Location\n""").upper()
    if opt2 == "B":
        sub_menu_b()




#Submenu B from section A
def sub_menu_b():
    opt3 = input("""Please enter one of following options: 
[A]-Most Reviewed Parks
[B]-Average Scores
[C]-Park Ranking by Nationality
[D]-Most Popular Month by Park\n""")

def menu_a1():
    park = input("Which park do you with to see reviews for?")






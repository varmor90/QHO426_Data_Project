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
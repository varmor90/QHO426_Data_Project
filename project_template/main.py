"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import process
import tui


def main():
    #read the data from the file
    data = process.reading()

    # run the menu
    tui.menu(data)


# make sure
if __name__ == "__main__":
    main()




















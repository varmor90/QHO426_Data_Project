"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
def reading(file_path="data/disneyland_reviews.csv"):
    data = []

    with open(file_path, mode="r") as f:
        reader = csv.reader(f)
        headers = next(reader)
#changing data from list to dictionary
        for row in reader:
            if len(row) == len(headers):
                row_dict = {headers[i]: row[i] for i in range(len(headers))}
                data.append(row_dict)

    print("Data set for 'disneyland_reviews.csv' has been uploaded.")
    print(f"There are {len(data)} rows in the dataset.")

    return data


def view_reviews_by_park(data):
    valid_parks = ["Disneyland_HongKong", "Disneyland_California", "Disneyland_Paris"]
    park_reviews = []

    while True:
        park_name = input("""Enter the park name:\n
        Disneyland_HongKong\n
        Disneyland_California\n
        Disneyland_Paris\n
        """)
# check if input is correct
        if park_name in valid_parks:
            for review in data:
                if review['Branch'] == park_name:
                    park_reviews.append(review)
            break
        else:
            print("Please enter a correct park name.\n")

    # results
    if park_reviews:
        print(f"\nReviews for {park_name}:")
        for review in park_reviews:
            print(f"Review ID: {review['Review_ID']}, Rating: {review['Rating']}, "
                  f"Date: {review['Year_Month']}, Location: {review['Reviewer_Location']}")
    else:
        print(f"\nNo reviews found for {park_name}.")


def number_of_reviews_by_park_and_location(data):

    park_location_counts = {}


    for review in data:
        park = review['Branch']
        location = review['Reviewer_Location']


        key = f"{park} - {location}"

        if key not in park_location_counts:
            park_location_counts[key] = 0  #

        park_location_counts[key] += 1  #


    for key, count in park_location_counts.items():
        print(f"{key}: {count} reviews")



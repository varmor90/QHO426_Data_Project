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

        for row in reader:
            if len(row) == len(headers):
                row_dict = {}
                for i in range(len(headers)):
                    row_dict[headers[i]] = row[i]
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

        if park_name in valid_parks:
            for review in data:
                if review['Branch'] == park_name:
                    park_reviews.append(review)
            break
        else:
            print("Please enter a correct park name.\n")


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

#printing results
    for key, count in park_location_counts.items():
        print(f"{key}: {count} reviews")

def average_score_per_year_by_park(data):
    """
    Funtion counts the average score for each park and prints the results in 'park - year' format



    """

    park_year_scores = {}
    park_year_counts = {}



    for review in data:
        park = review['Branch']
        year = review['Year_Month'][:4]
        rating = float(review['Rating'])


        key = (park, year)


        if key not in park_year_scores:
            park_year_scores[key] = 0.0
            park_year_counts[key] = 0

            park_year_scores[key] += rating
            park_year_counts[key] += 1



    for key in park_year_scores:
        park, year = key
        total_score = park_year_scores[key]
        count = park_year_counts[key]
        average_score = total_score / count
        print(f"{park} - {year}: {average_score:.2f}")


def average_score_per_park_by_location(data):
    """
    Function counts average score for every park, based on reviewer location and
    prints Park- location : average score format

    """

    park_location_scores = {}
    park_location_counts = {}


    for review in data:
        park = review['Branch']
        location = review['Reviewer_Location']
        rating = float(review['Rating'])

        key = (park, location)


        if key not in park_location_scores:
            park_location_scores[key] = 0.0
            park_location_counts[key] = 0

        # add review to the dictionary
        park_location_scores[key] += rating
        park_location_counts[key] += 1


    for key in park_location_scores:
        park,location =key
        total_score = park_location_scores[key]
        count = park_location_counts[key]
        average_score = total_score / count
        print(f"{park} - {location}: {average_score:.2f}")





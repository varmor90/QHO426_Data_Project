"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import process
import matplotlib.pyplot as plt

#Funtion to count all the reviews for each park and show result by bar chart
def most_reviewed_parks(data):

    park_counts = {}

    for review in data:
        park = review['Branch']
        if park in park_counts:
            park_counts[park] += 1
        else:
            park_counts[park] = 1

    # Pie chart
    parks = list(park_counts.keys())
    counts = list(park_counts.values())

    plt.figure(figsize=(10, 6))
    plt.pie(counts, labels=parks)
    plt.title('Most Reviewed Parks')
    plt.show()

#funtion to count average scores for each park show results in bar chart
def average_scores(data):
    #dictionaries total ratings and number of reviews
    scores = {}
    counts = {}


    #loop through the reviews in database
    for review in data:
        park = review['Branch']
        rating = float(review['Rating'])

        #if park not in dictionary, add it
        if park not in scores:
            scores[park] = 0.0
            counts[park] = 0

        # sum up reviews
        scores[park] += rating
        counts[park] += 1

    # counting average score
    average_scores = {}
    for park in scores:
        total_score = scores[park]
        total_count = counts[park]
        average_scores[park] = total_score / total_count


    parks = list(average_scores.keys())
    average = list(average_scores.values())

    plt.bar(parks, average)
    plt.show()

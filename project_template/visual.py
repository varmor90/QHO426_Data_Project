"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import process
import matplotlib.pyplot as plt


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


def average_scores(data):
    #dictionaries total ratings and number of reviews
    scores = {}
    counts = {}



    for review in data:
        park = review['Branch']
        rating = float(review['Rating'])


        if park not in scores:
            scores[park] = 0.0
            counts[park] = 0

        # sum up reviews
        scores[park] += rating
        counts[park] += 1


    average_scores = {}
    for park in scores:
        total_score = scores[park]
        total_count = counts[park]
        average_scores[park] = total_score / total_count


    parks = list(average_scores.keys())
    average = list(average_scores.values())

    plt.bar(parks, average)
    plt.show()


def top_10_locations_by_rating(data):
    park_name = input("Enter the name of the park (Disneyland_HongKong, Disneyland_California, Disneyland_Paris): ")

    location_scores = {}
    location_counts = {}

    for review in data:
        park = review['Branch']
        location = review['Reviewer_Location']
        rating = float(review['Rating'])

        if park == park_name:
            if location not in location_scores:
                location_scores[location] = 0.0
                location_counts[location] = 0

            location_scores[location] += rating
            location_counts[location] += 1

    average_scores = {}
    for location in location_scores:
        average_scores[location] = location_scores[location] / location_counts[location]

    sorted_locations = []
    for location, score in average_scores.items():
        sorted_locations.append((location, score))

    sorted_locations.sort(key=lambda x: x[1], reverse=True)
    top_10_locations = sorted_locations[:10]

    locations = [item[0] for item in top_10_locations]
    avg_ratings = [item[1] for item in top_10_locations]

    plt.figure(figsize=(10, 6))
    plt.barh(locations, avg_ratings, color='purple')
    plt.xlabel('Average Rating')
    plt.ylabel('Location')
    plt.title(f'Top 10 Locations by Average Rating for {park_name}')
    plt.tight_layout()
    plt.show()



def average_rating_by_month(data):
    park_name = input("Enter the name of the park (Disneyland_HongKong, Disneyland_California, Disneyland_Paris): ")

    month_scores = {month: 0.0 for month in range(1, 13)}
    month_counts = {month: 0 for month in range(1, 13)}

    months_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']

    for review in data:
        park = review['Branch']
        if park == park_name:
            date = review['Year_Month']
            if date and len(date.split('-')) == 2:
                try:
                    month = int(date.split('-')[1])
                    rating = float(review['Rating'])
                    month_scores[month] += rating
                    month_counts[month] += 1
                except ValueError:
                    print(f"Invalid rating value for review: {review}")

    average_scores = []
    for month in range(1, 13):
        if month_counts[month] > 0:
            average = month_scores[month] / month_counts[month]
        else:
            average = 0
        average_scores.append(average)

    plt.figure(figsize=(10, 6))
    plt.bar(months_labels, average_scores, color='blue')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title(f'Average Rating by Month for {park_name}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
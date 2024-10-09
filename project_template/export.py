import csv
import json


class ParkDataExporter:
    def __init__(self, data):
        self.data = data
        self.parks = ["Disneyland_HongKong", "Disneyland_California", "Disneyland_Paris"]

    def export_to_txt(self, filename):
        with open(filename, 'w') as file:
            for park in self.parks:
                park_data = self.calculate_park_data(park)
                self.write_txt(file, park_data)

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.get_csv_headers())
            writer.writeheader()
            for park in self.parks:
                writer.writerow(self.calculate_park_data(park))

    def export_to_json(self, filename):
        park_data_list = [self.calculate_park_data(park) for park in self.parks]
        with open(filename, 'w') as file:
            json.dump(park_data_list, file, indent=4)

    def write_txt(self, file, park_data):
        file.write(f"{park_data['Park']}: {park_data['Number of Reviews']} reviews, "
                   f"{park_data['Positive Reviews']} positive, "
                   f"Average score: {park_data['Average Score']:.2f}, "
                   f"{park_data['Countries']} countries\n")

    def calculate_park_data(self, park_name):
        reviews = [row for row in self.data if row['Branch'] == park_name]
        review_count = len(reviews)
        positive_review_count = sum(1 for row in reviews if float(row['Rating']) >= 3)
        average_score = round(sum(float(row['Rating']) for row in reviews) / review_count, 2) if review_count > 0 else 0
        countries = len(set(row['Reviewer_Location'] for row in reviews))

        return {
            'Park': park_name,
            'Number of Reviews': review_count,
            'Positive Reviews': positive_review_count,
            'Average Score': average_score,
            'Countries': countries
        }

    def get_csv_headers(self):
        return ['Park', 'Number of Reviews', 'Positive Reviews', 'Average Score', 'Countries']


if __name__ == "__main__":
    data = [
        {'Branch': 'Disneyland_HongKong', 'Rating': '2', 'Reviewer_Location': 'USA'},
        {'Branch': 'Disneyland_California', 'Rating': '3', 'Reviewer_Location': 'UK'},
        {'Branch': 'Disneyland_Paris', 'Rating': '4', 'Reviewer_Location': 'UK'},
        {'Branch': 'Disneyland_Paris', 'Rating': '5', 'Reviewer_Location': 'Germany'},
        {'Branch': 'Disneyland_Paris', 'Rating': '2', 'Reviewer_Location': 'Germany'},
    ]

    exporter = ParkDataExporter(data)
    exporter.export_to_txt('parks_report.txt')
    exporter.export_to_csv('parks_report.csv')
    exporter.export_to_json('parks_report.json')
    print("Export completed.")
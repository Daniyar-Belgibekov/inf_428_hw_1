import numpy as np
import csv

import requests


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def generate_and_save_data():
    filenames = []

    test_case_1 = {
        'Engineering': generate_random_data(50, 10, 100),
        'Marketing': generate_random_data(50, 10, 100),
        'Finance': generate_random_data(50, 10, 100),
        'HR': generate_random_data(50, 10, 100),
        'Science': generate_random_data(50, 10, 100)
    }
    file_1 = 'test_case_1.csv'
    filenames.append(file_1)
    with open(file_1, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department', 'Threat_Score'])
        for department, scores in test_case_1.items():
            for score in scores:
                writer.writerow([department, score])
    print(f"Data saved to {file_1}")

    test_case_2 = {
        'Engineering': generate_random_data(50, 10, 100),
        'Marketing': generate_random_data(50, 10, 100),
        'Finance': generate_random_data(85, 15, 100),
        'HR': generate_random_data(50, 10, 100),
        'Science': generate_random_data(50, 10, 100)
    }
    file_2 = 'test_case_2.csv'
    filenames.append(file_2)
    with open(file_2, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department', 'Threat_Score'])
        for department, scores in test_case_2.items():
            for score in scores:
                writer.writerow([department, score])
    print(f"Data saved to {file_2}")

    test_case_3 = {
        'Engineering': generate_random_data(50, 10, 50),
        'Marketing': generate_random_data(50, 10, 50),
        'Finance': generate_random_data(50, 10, 150),
        'HR': generate_random_data(50, 10, 50),
        'Science': generate_random_data(50, 10, 50)
    }
    file_3 = 'test_case_3.csv'
    filenames.append(file_3)
    with open(file_3, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department', 'Threat_Score'])
        for department, scores in test_case_3.items():
            for score in scores:
                writer.writerow([department, score])
    print(f"Data saved to {file_3}")

    test_case_4 = {
        'Engineering': generate_random_data(50, 10, 100),
        'Marketing': generate_random_data(50, 10, 80),
        'Finance': generate_random_data(50, 10, 150),
        'HR': generate_random_data(50, 10, 60),
        'Science': generate_random_data(50, 10, 120)
    }
    file_4 = 'test_case_4.csv'
    filenames.append(file_4)
    with open(file_4, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department', 'Threat_Score'])
        for department, scores in test_case_4.items():
            for score in scores:
                writer.writerow([department, score])
    print(f"Data saved to {file_4}")

    return filenames



def create_index():
    url = f"http://localhost:9200/threat_scores"
    payload = {
        "mappings": {
            "properties": {
                "Department": {"type": "keyword"},
                "Threat_Score": {"type": "integer"}
            }
        }
    }



def populate_index(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            response = requests.post(f"http://localhost:9200/threat_scores/_doc", json=row)



if __name__ == "__main__":
    generate_and_save_data()




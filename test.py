import unittest
import csv


def calculate_aggregated_score(filename):
    department_scores = {}

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            department = row['Department']
            score = int(row['Threat_Score'])
            if department not in department_scores:
                department_scores[department] = []
            department_scores[department].append(score)

    aggregated_scores = {}
    for department, scores in department_scores.items():
        aggregated_scores[department] = sum(scores) / len(scores)

    overall_mean_score = sum(aggregated_scores.values()) / len(aggregated_scores)
    return overall_mean_score


class TestCyberSecurityData(unittest.TestCase):

    def test_case_1(self):
        filename = 'test_case_1.csv'
        aggregated_score = calculate_aggregated_score(filename)

        print(f"Aggregated Score 1 {aggregated_score:.2f}")

        self.assertAlmostEqual(aggregated_score, 50, delta=1)

    def test_case_2(self):
        filename = 'test_case_2.csv'
        aggregated_score = calculate_aggregated_score(filename)

        print(f"Aggregated Score 2 {aggregated_score:.2f}")

        self.assertGreater(aggregated_score, 50)

    def test_case_3(self):
        filename = 'test_case_3.csv'
        aggregated_score = calculate_aggregated_score(filename)

        print(f"Aggregated Score 3 {aggregated_score:.2f}")

        self.assertGreater(aggregated_score, 50)

    def test_case_4(self):
        filename = 'test_case_4.csv'
        aggregated_score = calculate_aggregated_score(filename)

        print(f"Aggregated Score 4 {aggregated_score:.2f}")

        self.assertTrue(aggregated_score > 0)


if __name__ == "__main__":
    unittest.main()

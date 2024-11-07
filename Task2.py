import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculateDepartmentMean(data):
    return np.mean(data)

def calculateAggregateThreatScore(mean, importance):
    sum = 0
    totalImportance = 0

    for i in range(len(mean)):
        sum += mean[i] * importance[i]
        totalImportance += importance[i]

    return sum / totalImportance

def main():
    departments = [
        generate_random_data(35, 5, 150),
        generate_random_data(36, 5, 150),
        generate_random_data(34, 5, 150),
        generate_random_data(37, 5, 150),
        generate_random_data(35, 5, 150)
    ]

    departmentMeans = [calculateDepartmentMean(data) for data in departments]

    importance = [1, 1, 1, 1, 1]
    aggregatedScore = calculateAggregateThreatScore(departmentMeans, importance)
    print(aggregatedScore)


main()

import numpy as np

print("Welcome to Yiyang Chen's ML project2!")
print("This project is a feature selection algorithm, using Nearest Neighbor as the classifier!")

print("\nPlease pick a dataset you want:")
print("1) Small dataset")
print("2) Large dataset")

while True:
    dataset_choose = input()
    if dataset_choose == '1':
        dataset = np.loadtxt('CS170_Small_DataSet__1.txt')
        break
    elif dataset_choose == '2':
        dataset = np.loadtxt('CS170_Large_DataSet__1.txt')
        break
    else:
        print("Invalid input, please choose 1 or 2 again.")

features_num = dataset.shape[1] - 1
instance_num = dataset.shape[0]
print(f"This dataset has {features_num} features(not including class label) and {instance_num} instances.")

while True:
    print("\nPlease pick a feature selection algorithm you want:")
    print("1) Forward Selection")
    print("2) Backward Elimination")
    algorithm_choose = input()
    if algorithm_choose == "1" or algorithm_choose == "2":
        break
    else:
        print("Invalid input, please choose 1 or 2 again.")
import numpy as np

#calculate distance
def Euclidean_distance(point1, point2):
    total = 0
    for i in range(len(point1)):
        diff = point1[i] - point2[i]
        total += diff** 2
    distance = total ** 0.5
    return distance
# tsetpoint_a = [1, 2, 3]
# tsetpoint_b = [4, 6, 3]
# print(Euclidean_distance(tsetpoint_a, tsetpoint_b))

#Compare distance between the point and all other points in the dataset, return the class label as the nearest neighbor
def nn_classify(dataset, feature_set):
    correct_classification_number = 0
    for i in range (len(dataset)):
        current_sample = dataset [i, feature_set]
        label = dataset [i, 0]
        nearest_neighbor_label = None  #The nearest neighbor's class label
        nearest_distance = float('inf')  #The current nearest distance, initialized to infinity.
        for j in range (len(dataset)):
            if j != i:  # Skip the current sample
                distance = Euclidean_distance(current_sample, dataset[j, feature_set])    #Important! Here we only calculate distance based on the selected features.
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_neighbor_label = dataset[j, 0]  # Update the nearest neighbor's class label
        if label == nearest_neighbor_label:
            correct_classification_number += 1
    accuracy = correct_classification_number / len(dataset)
    return accuracy


def forward_selection():
    current_feature_set = []
    the_best_overall_accuracy = 0

def backward_elimination():
    
                

print("Welcome to Yiyang Chen's ML project2!")
print("This project is a feature selection algorithm, using Nearest Neighbor as the classifier!")

print("\nPlease pick a dataset you want:")
print("1) Small dataset")
print("2) Large dataset")

while True:
    dataset_choose = input()
    if dataset_choose == '1':
        dataset = np.loadtxt('CS170_Small_DataSet__1.txt')#Note that Dr.Eamoon suggested me to use small and large dataset 1 because my name was not in the list.
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
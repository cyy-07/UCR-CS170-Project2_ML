import numpy as np
import time
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
                    nearest_neighbor_label = dataset[j, 0]  # Update the nearest neighbor's class label.
        if label == nearest_neighbor_label:
            correct_classification_number += 1
    accuracy = correct_classification_number / len(dataset)
    return accuracy


def forward_selection(dataset, features_num):
    start = time.time()
    current_feature_set = []
    the_best_overall_accuracy = 0
    the_best_overall_feature_set = []
    all_features = []                   #Here we initialize a list to store all the features, using a for loop to add all the features to this list. We will use this list to calculate the accuracy of using all features at the beginning of forward selection algorithm, and we will also use this list to make sure we are testing all the features in the dataset during the search process.
    for f in range(1, features_num + 1):
        all_features.append(f)
    overall_accuracy = nn_classify(dataset, all_features)
    print(f'Running nearest neighbor with all {features_num} features, using "leaving-one-out" evaluation, I get an accuracy of {overall_accuracy * 100:.1f}%')
    print("Beginning search. The current feature set is empty.")
    #For each level, we will add a new feature to the current feature set,
    #and we compute each feature's accuracy. 
    #Finally, we will pick the feature with the highest accuracy and add it to the current feature set.
    for i in range (1,features_num+1):
        best_accuracy_this_level = 0
        best_feature_this_level = None
        for j in range (1,features_num+1):      #note that we start from one because the feature index begins from 1!
            if j not in current_feature_set:     #consider only the features that are not in the current feature set
                current_feature_set.append(j)              #add the feature to the current feature set temporarily
                accuracy = nn_classify(dataset, current_feature_set)
                print(f"Using feature(s) {current_feature_set} accuracy is {accuracy:.2f}%")
                current_feature_set.remove(j)              #debug: remove the feature from the current (temporary) feature set.
                if accuracy > best_accuracy_this_level:    #if the accuracy is better than the best accuracy we have now, update the best accuracy. 
                    best_feature_this_level = j
                    best_accuracy_this_level = accuracy
        #After we finish testing all the features that are not in the current feature set, we add the best feature of this level to current feature set.
        current_feature_set.append(best_feature_this_level)  
        print(f"Feature set {current_feature_set} was best, accuracy is {best_accuracy_this_level:.2f}%")
        if best_accuracy_this_level > the_best_overall_accuracy:
            the_best_overall_accuracy = best_accuracy_this_level
            the_best_overall_feature_set = current_feature_set.copy()
        else:
            print("(Warning! At this level, the best accuracy is worse than the best overall accuracy! Continue search to see if we can find a better feature subset.(Avoiding local maximum!))")
    print(f"Finished search! The best feature subset is {the_best_overall_feature_set}, which has an accuracy of {the_best_overall_accuracy:.2f}%")
    print(f"Total search time: {time.time() - start:.1f} seconds")           #Here we calculate the total search time.


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
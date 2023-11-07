
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def WinePredictor():

    # Load the data
    Wine_file = 'WinePredictor.csv'
    data = pd.read_csv(Wine_file)

    print("All data from the csv file is : ")
    print(data)

    print("Size of data set : ",len(data))

    # clean , Prepare and Manipulate data

    features = data.drop("Class",axis = 1)
    print("Features is : ",features)

    labels = data["Class"]
    print("Labels is : ",labels)

    classifier = KNeighborsClassifier(n_neighbors=3)

    # train the data

    data_train, data_test, target_train, target_test = train_test_split(features,labels,test_size=0.3)
    classifier.fit(data_train,target_train)

    # test the data

    predictions = classifier.predict(data_test)

    # Calculate the Accuracy
    accuracy = accuracy_score(target_test,predictions)

    return accuracy

def main():

    print("---Wine Predictor using KNN Algorithm---")

    Accuracy = WinePredictor()

    print("Accuracy of Wine Predictor using KNN is : ",Accuracy*100,"%")

if __name__ == "__main__":
    main()
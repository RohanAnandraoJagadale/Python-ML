from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def MarvellousSVM():
    #Load DAtaset
    canser = datasets.load_breast_cancer()

    # print the names of the 13 features
    print("Features of the cancer dataset : ",canser.feature_names)

    # print the label type of cancer('maligant' 'benign')
    print("Labels of the cancer dataset : ",canser.target_names)

    # print data(features)shape
    print("Shape of dataset is : ",canser.data.shape)

    # print the cancer data features (top 5 records)
    print("First 5 records are : ")
    print(canser.data[0:5])

    # print the cancer labels (0:maligant, 1:benign)
    print("Target of dataset : ",canser.target)

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(canser.data, canser.target,test_size=0.3,random_state=109) #70% training and 30% test

    # Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear kernel

    # Train the model using the training sets
    clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy : how often is the classifier correct ?
    print("Accuracy of the model is :",metrics.accuracy_score(y_test,y_pred)*100)

def main():
    print("-------Rohan Jagadale---------")

    MarvellousSVM()

if __name__ == "__main__":
    main()

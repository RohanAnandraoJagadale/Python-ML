import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import  KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    # Step 1 : Load the data
    data = pd.read_csv(data_path, index_col=0)

    print("Size of actual data set is : ",len(data))

    # Step 2 : Clean, Prepare and manipulate data
    feature_names = ['Whether','Temperature']

    print("Names of Features",feature_names)

    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # ceating labelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers.
    weather_encoded = le.fit_transform(whether)
    print(weather_encoded)

    # Converting string labels into numbers
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    # Combining weather and temp into single list of tuples
    features = list(zip(weather_encoded,temp_encoded))

    # Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors = 3)

    # Train the model using the training sets
    model.fit(features,label)

    # Step 4 : Test data
    predicted = model.predict([[0,2]]) # 0:Overcast, 2:Mild
    print(predicted)

def main():
    print("Machine Learning Application")

    print("Play predictor application using K Nearest knighbor algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
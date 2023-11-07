from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
# Import train_test_split function
from sklearn.model_selection import train_test_split
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Load Data
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Split dataset into training set and test set
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.3) # 70% training and 30% test

# Create adaboost classifier object
abc = AdaBoostClassifier(n_estimators = 50, learning_rate = 1)

# Train Adaboost Classifier
model = abc.fit(X_train,y_train)

# Predict the response for test dataset
y_pred = model.predict(X_test)

print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))
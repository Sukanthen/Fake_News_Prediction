
# Fake News Prediction in Python  


# Import necessary packages
import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.meetrics import accuracy_score, confusion_matrix

# Read the data
df=pd.read_csv("............")  # enter your file locatory path 

# Exploratory Data Analysis
df.shape
df.head()
df.tail()

# Get the labels
labels=df.label
labels.head()

# Apply ML algorithm 
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train=tfidf_vectorizer.fit_transform(x_train)

tfidf_test=tfidf_vectorizer.transform(x_test)

pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

# Predict on the accuracy of our model
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print('Accuracy: {round(score*100,2)}%')

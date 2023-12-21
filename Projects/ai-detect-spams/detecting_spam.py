import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Data Collection
print("================================================= DATA COLLECTION =================================================")
data = pd.read_csv("spam.csv", encoding="utf-8")

# Convert data into a frame for easy data processing
df = pd.DataFrame(data)
print(df)

# Data Processing
# We use CountVectorizer() to transform texts into numerical format.
print("================================================= DATA PROCESSING =================================================")
vectorizer = CountVectorizer()
numerical_data = vectorizer.fit_transform(df['Message'])
print(numerical_data)

label = df['Classification']
numerical_data_train, numerical_data_test, label_train, label_test = train_test_split(numerical_data,label,test_size=0.2)

# Model Training
classifier=MultinomialNB()
classifier.fit(numerical_data_train,label_train)

# Model Evaluation
print("================================================= MODEL EVALUATION =================================================")
label_prediction = classifier.predict(numerical_data_test)
print(classification_report(label_test,label_prediction))

# Test the Model
print("================================================= MODEL TESTING =================================================")
message = "Today's Offer! Claim ur £150 worth of discount vouchers! Text YES to 85023 now! SavaMob, member offers mobile! T Cs 08717898035. £3.00 Sub. 16 . Unsub reply X "
vectorized_message = vectorizer.transform([message])
prediction = classifier.predict(vectorized_message)
print("Testing message: {}".format(message))
print("The email is :", prediction[0])

print("================================================= TESTING AGAINST NEW SET OF DATA =================================================")
print("Testing the model against test_emails.csv")
# Running a new set of of test data
test_data=pd.read_csv("test_emails.csv")
numerical_data_new = vectorizer.transform(test_data['Messages'])
new_predictions = classifier.predict(numerical_data_new)
results_df = pd.DataFrame({'Messages': test_data['Messages'],'Prediction':new_predictions})
print(results_df)

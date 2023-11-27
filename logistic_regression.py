import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_recall_fscore_support
import seaborn as sns
import matplotlib.pyplot as plt

# Read in DataFrame
df = pd.read_csv('san_francisco_weather_cleaned.csv')

# Features and target variable
features = ['humidity', 'pressure', 'temperature', 'wind_direction', 'wind_speed']
target = 'weather_desc'

# Data preprocessing
# (Assuming label encoding for 'weather_desc' has been done previously)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Logistic Regression
lr_model = LogisticRegression(random_state=42, max_iter=10000)
lr_model.fit(X_train, y_train)
print(f"Number of iterations: {lr_model.n_iter_}")


# Predictions
y_pred = lr_model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Additional metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=1))


# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=lr_model.classes_, yticklabels=lr_model.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted', zero_division=1)
print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {fscore:.2f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # Import RandomForestClassifier
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

# Random Forest
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)  # You can adjust the number of trees with the 'n_estimators' parameter
rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Additional metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=1))

# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=rf_model.classes_, yticklabels=rf_model.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted', zero_division=1)
print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {fscore:.2f}")

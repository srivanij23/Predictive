from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Load the dataset
df = pd.read_csv('machine_data.csv')

# Features and Target variable
X = df.drop('Maintenance', axis=1)
y = df['Maintenance']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model: Random Forest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model (you can use this model for deployment)
import joblib
joblib.dump(model, 'maintenance_model.pkl')

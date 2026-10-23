import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Educational demonstration using synthetic data only.
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    "duration": np.random.randint(1, 500, n),
    "packet_count": np.random.randint(1, 2000, n),
    "bytes_sent": np.random.randint(100, 100000, n),
    "failed_logins": np.random.randint(0, 10, n),
    "unusual_port": np.random.randint(0, 2, n),
    "connection_rate": np.random.randint(1, 500, n)
})
attack_score = ((data["failed_logins"] >= 5).astype(int)
                + data["unusual_port"]
                + (data["connection_rate"] >= 350).astype(int))
data["label"] = (attack_score >= 2).astype(int)

X = data.drop("label", axis=1)
y = data["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("AI-Based Network Intrusion Detector")
print("-----------------------------------")
print("Data source: synthetic demonstration data")
print(f"Test accuracy: {accuracy_score(y_test, predictions):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, predictions,
      target_names=["Benign", "Attack"], zero_division=0))

cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Benign", "Attack"],
            yticklabels=["Benign", "Attack"])
plt.title("Network Traffic Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()
plt.show()

importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nImportant Features:")
print(importance)
importance.plot(kind="bar", title="Feature Importance")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

new_traffic = pd.DataFrame([{
    "duration": 20, "packet_count": 800, "bytes_sent": 50000,
    "failed_logins": 8, "unusual_port": 1, "connection_rate": 420
}])
result = model.predict(new_traffic)[0]
print("\nNew Traffic Prediction:", "ATTACK" if result == 1 else "BENIGN")
joblib.dump(model, "intrusion_detection_model.pkl")
print("Model saved as intrusion_detection_model.pkl")

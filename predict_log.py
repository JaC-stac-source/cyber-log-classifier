import joblib

# Load trained model
model = joblib.load("models/model.pkl")

print("----------------------------")
print("Cybersecurity Log Classifier")
print("----------------------------")

# Collect user input
failed_logins = int(input("Failed Login Attempts: ")
)

off_hours_login = int(input("Off Hours Login (0 = No, 1 = Yes): ")
)

file_download_mb = int(input("File Download Size (MB): ")
)

# Run inference
prediction = model.predict(
  [
    [failed_logins, off_hours_login, file_download_mb]
  ]
)

# Display result
print()
print(f"Classification: {prediction[0]}")

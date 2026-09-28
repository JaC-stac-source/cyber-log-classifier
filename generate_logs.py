import pandas as pd
import random

records = []

for _ in range(1000):

    failed_logins = random.randint(0, 20)

    off_hours_login = random.choice([0, 1])

    file_download_mb = random.randint(0, 1000)

    # Simple rule used to create labels
    if failed_logins > 8 or (off_hours_login == 1 and file_download_mb > 200):
        result = "Suspicious"
    else:
        result = "Normal"

    records.append([failed_logins, off_hours_login, file_download_mb, result])

df = pd.DataFrame(records, columns=[
        "failed_logins",
        "off_hours_login",
        "file_download_mb",
        "result"
    ]
)

df.to_csv("data/logs.csv", index=False)

print("Cybersecurity log dataset created.")
print(f"Records generated: {len(df)}")

import requests
import time
import csv
import os
from datetime import datetime

up_count = 0
down_count = 0
total_response_time = 0

websites = [
    "https://google.com",
    "https://github.com",
    "https://bbc.co.uk"
]

for url in websites:
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)

        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time

        print("========================================")
        print("Checking:", url)
        print("========================================")
        print("Status code:", response.status_code)
        print("Response time:", round(response_time, 3), "seconds")

        if response_time < 1:
            performance = "GOOD"
        else:
            performance = "SLOW"

        print("Performance:", performance)

        if response.status_code == 200:
            status = "UP"
            up_count += 1
        else:
            status = "DOWN"
            down_count += 1
        print("Status:", status)

        file_exists = os.path.exists("health_log.csv")

        with open("health_log.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Website",
                    "Status",
                    "Response Time",
                    "Performance",
                    "Timestamp"
                ])

            writer.writerow([
                url,
                status,
                round(response_time, 3),
                performance,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

    except requests.exceptions.RequestException:
        print("========================================")
        print("Checking:", url)
        print("========================================")
        print("Status: DOWN")
        print("Error: Website could not be reached")

        file_exists = os.path.exists("health_log.csv")

        with open("health_log.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Website",
                    "Status",
                    "Response Time",
                    "Performance",
                    "Timestamp"
                ])

            writer.writerow([
                url,
                "DOWN",
                "N/A",
                "N/A",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

if up_count > 0:
    average_response_time = total_response_time / up_count
else:
    average_response_time = 0
print()
print("========================================")
print("Health Check Summary")
print("========================================")
print("Websites checked:", len(websites))
print("Websites UP:", up_count)
print("Websites DOWN:", down_count)
print("Average response time:", round(average_response_time, 3), "seconds")
from flask import Flask
import requests
import time
import csv
import os
from datetime import datetime

app = Flask(__name__)

websites = [
    "https://google.com",
    "https://github.com",
    "https://bbc.co.uk"
]

up_count = 0
down_count = 0
total_response_time = 0

results = []

for url in websites:
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)

        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time

        if response.status_code == 200:
            status = "UP"
            up_count += 1
        else:
            status = "DOWN"
            down_count += 1

        if response_time < 1:
            performance = "GOOD"
        else:
            performance = "SLOW"

        results.append({
            "url": url,
            "status": status,
            "response_time": round(response_time, 3),
            "performance": performance
        })

        print("========================================")
        print("Checking:", url)
        print("========================================")
        print("Status code:", response.status_code)
        print("Response time:", round(response_time, 3), "seconds")
        print("Performance:", performance)
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
        down_count += 1

        results.append({
            "url": url,
            "status": "DOWN",
            "response_time": "N/A",
            "performance": "N/A"
        })

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


@app.route("/")
def home():
    result_html = ""

    for result in results:
        result_html += f"""
        <li>
            <strong>{result["url"]}</strong><br>
            Status: {result["status"]}<br>
            Response time: {result["response_time"]} seconds<br>
            Performance: {result["performance"]}
            <br><br>
        </li>
        """

    return f"""
    <html>
    <head>
        <title>Deployment Health Checker</title>
    </head>

    <body>
        <h1>Deployment Health Checker</h1>

        <p>Cloud monitoring service is running successfully.</p>

        <h2>Live Health Check Results</h2>

        <ul>
            {result_html}
        </ul>

        <h2>Summary</h2>

        <p>Websites checked: {len(websites)}</p>
        <p>Websites UP: {up_count}</p>
        <p>Websites DOWN: {down_count}</p>
        <p>Average response time: {round(average_response_time, 3)} seconds</p>
    </body>
    </html>
    """


app.run(host="0.0.0.0", port=10000)
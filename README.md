# Deployment Health Checker

A Python-based website health monitoring tool that checks website availability, measures response time, logs results to a CSV file, and provides a summary of overall website health.

## Project Overview

The Deployment Health Checker is a lightweight monitoring tool designed to simulate a basic infrastructure health-check process.

The program sends HTTP requests to a list of websites and records whether each website is available, how quickly it responds, and the overall health of the monitored services.

This project was built to develop practical skills relevant to **cloud computing, infrastructure monitoring, and DevOps**.

## Features

* Checks multiple websites automatically
* Detects whether websites are UP or DOWN
* Measures HTTP response time
* Handles request errors and timeouts
* Logs monitoring results to a CSV file
* Calculates average response time
* Provides an overall health summary
* Uses Git for version control
* Hosted publicly on GitHub

## Technologies Used

* Python
* Requests
* CSV
* Git
* GitHub
* Docker

## How It Works

1. A list of websites is defined.
2. The program sends an HTTP request to each website.
3. Response time is measured.
4. The website is classified as UP or DOWN.
5. The result is recorded in `health_log.csv`.
6. The average response time is calculated.
7. A final health summary is displayed in the terminal.

### Monitoring Workflow

```text
Websites
    ↓
HTTP Requests
    ↓
Availability Check
    ↓
Response Time Measurement
    ↓
CSV Logging
    ↓
Health Summary
```

## Example Output

```text
========================================

Health Check Summary

========================================

Websites checked: 3
Websites UP: 3
Websites DOWN: 0
Average response time: 0.742 seconds
```

## Project Structure

```text
deployment-health-checker/
│
├── health_checker.py
├── health_log.csv
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/SOblaize/deployment-health-checker.git
```

### 2. Navigate into the project

```bash
cd deployment-health-checker
```

### 3. Install the required Python package

```bash
pip install requests
```

### 4. Run the health checker

```bash
python3 health_checker.py
```

## Running with Docker

### 1. Build the Docker image

```bash
docker build -t deployment-health-checker .
```

### 2. Run the container

```bash
docker run --rm deployment-health-checker
```

The container runs the health checker and displays the availability and response-time results in the terminal.

## Skills Demonstrated

* Python scripting
* HTTP requests
* Website monitoring
* Infrastructure health checks
* Error handling
* Response-time measurement
* CSV data logging
* Command-line execution
* Git version control
* GitHub repository management

## Future Improvements

* Add continuous monitoring at scheduled intervals
* Add email or notification alerts when a website goes DOWN
* Create a monitoring dashboard
* Store monitoring data in a database
* Containerise the application using Docker
* Deploy the monitoring system to a cloud environment
* Add automated testing
* Add CI/CD using GitHub Actions

## Author

**Shana Blaize**

Computer Science student interested in **cloud computing, infrastructure, and technology operations**.

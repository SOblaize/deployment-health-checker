# Deployment Health Checker

A Python project that checks whether websites are working, measures how quickly they respond, and records the results.

I built this project to learn more about **cloud computing, infrastructure monitoring, Docker and DevOps**.

The project is also deployed online using Render, so the health checker can be accessed through a web browser.

**Live app:** https://deployment-health-checker.onrender.com

**GitHub:** https://github.com/SOblaize/deployment-health-checker

## What it does

The health checker currently monitors:

* Google
* GitHub
* BBC

For each website, it:

* Checks whether the website is UP or DOWN
* Measures the response time
* Marks the performance as GOOD or SLOW
* Records the result in a CSV file
* Calculates the average response time

The results are also shown on a simple Flask web page.

## Example

```text
Health Check Summary

Websites checked: 3
Websites UP: 3
Websites DOWN: 0
Average response time: 0.270 seconds
```

The web page displays the individual results, including the website status, response time and performance.

## How it works

```text
Websites
    ↓
HTTP Requests
    ↓
Check Status
    ↓
Measure Response Time
    ↓
Save Results
    ↓
Display Results
```

## Technologies

* Python
* Flask
* Requests
* CSV
* Git
* GitHub
* Docker
* GitHub Actions
* Render

## Project Structure

```text
deployment-health-checker/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── health_checker.py
├── health_log.csv
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Running it locally

### Clone the repository

```bash
git clone https://github.com/SOblaize/deployment-health-checker.git
```

### Go into the project

```bash
cd deployment-health-checker
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python3 health_checker.py
```

Then open:

```text
http://127.0.0.1:10000
```

## Running with Docker

Build the image:

```bash
docker build -t deployment-health-checker .
```

Run the container:

```bash
docker run --rm -p 10000:10000 deployment-health-checker
```

Then open:

```text
http://localhost:10000
```

## GitHub Actions

I added a GitHub Actions workflow that runs the health checker when changes are pushed to the `main` branch or when a pull request is created.

The workflow installs the dependencies and runs the Python application to make sure it still works.

The workflow is located at:

```text
.github/workflows/ci.yml
```

## Docker

The application is packaged into a Docker container using the `Dockerfile`.

This means the application and its dependencies can be run in a consistent environment rather than relying on the setup of a particular computer.

## Cloud Deployment

The application is deployed as a Docker web service on Render.

The deployment flow is:

```text
Code
  ↓
Git
  ↓
GitHub
  ↓
GitHub Actions
  ↓
Docker
  ↓
Render
  ↓
Live Application
```

Live application:

https://deployment-health-checker.onrender.com

## What I learned

Through this project I gained experience with:

* Building a Python monitoring script
* Making HTTP requests
* Handling errors and timeouts
* Measuring response times
* Working with CSV files
* Using Git and GitHub
* Creating a Docker image
* Setting up GitHub Actions
* Deploying an application to the cloud
* Running a Flask web service
* Understanding how an application moves from local development to a cloud environment

## Possible improvements

Some things I could add in the future:

* Run checks continuously instead of only when the application starts
* Add alerts when a website goes down
* Add graphs showing response times over time
* Store results in a database
* Add more websites to monitor
* Add automated tests
* Use a production WSGI server

## Author

**Shana Blaize**

BSc Computer Science student interested in cloud computing, infrastructure and DevOps.

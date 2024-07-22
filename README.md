# Password Generator Flask App

This project is a simple web application for generating passwords using Flask. Users can specify the length and types of characters to include in the generated password. The app is containerized using Docker for easy deployment.

## Project Structure

password-generator-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── static/
│ └── style.css
└── templates/
└── index.html


### Files and Folders

- **`app.py`**: The main Flask application file containing the logic for generating passwords.
- **`Dockerfile`**: The Dockerfile used to build the Docker image for the app.
- **`requirements.txt`**: Contains the Python dependencies for the project.
- **`README.md`**: This file, containing the project documentation.
- **`static/`**: Contains static files such as CSS, JavaScript, and images.
  - `style.css`: CSS styles for the application.
- **`templates/`**: Contains HTML templates for rendering pages.
  - `index.html`: HTML template for the password generator form and result.

## Installation

To run this application locally using Docker, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/password-generator-app.git
cd password-generator-app

2. Build the Docker Image
Build the Docker image using the provided Dockerfile:

docker build -t password_gen .

-t password_gen tags the Docker image with the name password_gen.
. specifies the build context (the current directory).

3. Run the Docker Container
Run a container from the built Docker image:
docker run -p 5000:5000 password_gen

-p 5000:5000 maps port 5000 on your local machine to port 5000 in the container.
password_gen is the name of the Docker image you built.

4. Access the Application
Open a web browser and go to http://localhost:5000 to access the Password Generator app.

Code Overview
app.py
This file contains the Flask application code. It handles the form submission, generates the password based on user input, and renders the result.

Dockerfile
The Dockerfile sets up the Python environment, installs the necessary dependencies, and runs the Flask application. Here’s what each part does:

FROM python:3.9-slim: Uses a slim version of the Python 3.9 image.
WORKDIR /app: Sets the working directory in the container to /app.
COPY requirements.txt .: Copies the requirements.txt file into the container.
RUN pip install --no-cache-dir -r requirements.txt: Installs the Python dependencies.
COPY . .: Copies the rest of the application code into the container.
EXPOSE 5000: Exposes port 5000 in the container.
ENV FLASK_APP=app.py: Sets the Flask application environment variable.
CMD ["flask", "run", "--host=0.0.0.0"]: Runs the Flask application, listening on all network interfaces.

requirements.txt
Lists the Python dependencies for the project. For this app, it includes:
Flask==2.2.3

static/style.css
Contains the CSS styles for the application, including dark mode and transparent styling.

templates/index.html
The HTML template for the password generator form and result, including the "Copy Password" button with JavaScript functionality.

<p align="center">
  <img src="./src/templates/static/logo.png" alt="ABUAD HMS Logo", width="120", height="120">
</p>
<h1 align="center">ABUAD HMS (Hostel Monitoring System)</h1>
<div align="center">

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Flask-darkgreen.svg?style=flat&logo=flask&logoColor=white)](https://github.com/Nneji123/abuad-hms)
[![HTML](https://img.shields.io/badge/HTML-black.svg?style=flat&logo=html5&logoColor=white)](https://github.com/Nneji123/abuad-hms)
[![CSS](https://img.shields.io/badge/CSS-blue.svg?style=flat&logo=css3&logoColor=white)](https://github.com/Nneji123/abuad-hms)
[![Javascript](https://img.shields.io/badge/Javascript-yellow.svg?style=flat&logo=javascript&logoColor=white)](https://github.com/Nneji123/abuad-hms)
[![Postgres](https://img.shields.io/badge/Postgres-darkblue.svg?style=flat&logo=postgres&logoColor=white)](https://github.com/Nneji123/abuad-hms)
![hosted](https://img.shields.io/badge/Railway-430098?style=flat&logo=railway&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
[![Gitpod](https://img.shields.io/badge/Gitpod-orange?style=flat&logo=gitpod&logoColor=white)](https://gitpod.io/#https://github.com/Nneji123/abuad-hms)
![reposize](https://img.shields.io/github/repo-size/Nneji123/abuad-hms)

</div>

> ABUAD HMS is a web/desktop-based application  that allows the efficient monitoring of hostels in Afe Babalola University. It is a part of the ABUAD Smart School Environment Project carried out by [Ifeanyi Nneji](https://github.com/Nneji123) and [Ogunkuade Ayobamidele](https://github.com/devXcant). 

> Visit the [ABUAD Smart School Environment](https://github.com/Nneji123/ABUAD-SMART-SCHOOL-ENVIRONMENT) Repository to learn more details about other aspects of the project. 

# Table Of Contents
- [Table Of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Tools Used](#tools-used)
- [Flowchart](#flowchart)
- [Use Case Diagram](#use-case-diagram)
- [Screenshots](#screenshots)
- [Demo Videos](#demo-videos)
- [Installation](#installation)
- [How to Run ABUAD HMS](#how-to-run-abuad-hms)
  - [How to Run as Desktop App](#how-to-run-as-desktop-app)
    - [Building Desktop App with cx\_freeze](#building-desktop-app-with-cx_freeze)
  - [How to run in Docker and Docker Compose](#how-to-run-in-docker-and-docker-compose)
- [Deployment](#deployment)
- [References](#references)
- [License](#license)

# Introduction
ABUAD HMS (Abuad Hostel Monitoring System) is a part of the Abuad Smart School Environment, a comprehensive system that integrates technology into various aspects of the school environment to enhance learning, safety, and convenience. ABUAD HMS is a web-based application developed to simplify the process of monitoring student activity in hostels of Afe Babalola University.

The system utilizes state-of-the-art object detection and classification models to monitor and detect violence in hostels. With the real-time monitoring feature, the authorities can take necessary actions promptly, ensuring the safety and well-being of students in the hostels.

# Motivation

The development of ABUAD HMS was motivated by the need to ensure a safe and secure environment for students in the hostels. Violence in hostels is a serious issue that poses a threat to the well-being of students. The traditional methods of monitoring and detecting such activities are not always effective, and there is a need for a more advanced and automated system.

ABUAD HMS aims to provide a solution to this problem by leveraging technology to monitor and detect violence in hostels. The system is designed to be user-friendly, efficient, and effective, and it ensures that the authorities can take prompt and necessary actions when needed. The development of ABUAD HMS demonstrates Afe Babalola University's commitment to providing a safe and secure environment for its students.

# Features 
ABUAD HMS (Abuad Hostel Monitoring System) is a comprehensive system that offers various features to simplify the process of hostel management and ensure the safety and well-being of students. Some of the key features of ABUAD HMS are:

- Real-time Monitoring: ABUAD HMS offers real-time monitoring of hostels using state-of-the-art object detection and classification models. The system alerts the authorities when it detects any suspicious activities such as violence or smoking, enabling them to take prompt action.

- Smoking and Violence Detection: ABUAD HMS uses advanced algorithms to detect smoking and violence in hostels. The system monitors various activities such as movement, sound, and temperature to identify any suspicious activities and sends an alert to the authorities.

- Offenders List: ABUAD HMS allows the authorities to view a list of offenders who have engaged in activities such as smoking or violence in the hostels. The system maintains a record of such activities and provides the necessary information to the authorities for taking appropriate actions.

# Repository Structure
```
|-- Dockerfile
|-- LICENSE.md
|-- README.md
|-- docker-compose.yml
|-- render.yaml
|-- requirements.txt
|-- screens
|   |-- app.py
|   |-- config.py
|   |-- database.db
|   |-- deep_sort
|   |-- home.py
|   |-- index.py
|   |-- init.py
|   |-- instance
|   |-- login.py
|   |-- logo.ico
|   |-- logout.py
|   |-- models
|   |   |-- smoking_large.onnx
|   |   |-- smoking_small.onnx
|   |   |-- violence_small.onnx
|   |   |-- violence_large.onnx
|   |-- schema.py
|   |-- setup.iss
|   |-- setup.py
|   |-- templates
|   |   |-- admin
|   |   |   |-- index.html
|   |   |   `-- templates
|   |   |       |-- README.txt
|   |   |       |-- base.html
|   |   |       `-- master.html
|   |   |-- base.html
|   |   |-- error.html
|   |   |-- index.html
|   |   |-- login.html
|   |   |-- monitor.html
|   |   |-- static
|   |   |   |-- admin.css
|   |   |   |-- favicon.ico
|   |   |   |-- google_fonts.css
|   |   |   |-- logo.png
|   |   |   |-- main.css
|   |   |   |-- offenders
|   |   |   |   `-- placeholder
|   |   |   `-- style.css
|   |   `-- view_offenders.html
|   `-- utils.py
```

# Tools Used 
 Some of the key tools used in the development of ABUAD HMS are:

1. HTML: HTML was used to develop the structure and content of the web pages in ABUAD HMS.

2. CSS: CSS was used to style the web pages and enhance the visual appeal of ABUAD HMS.

3. JavaScript: JavaScript was used to add dynamic behavior to the web pages and provide a better user experience.

4. Datatables: Datatables is a plugin used in ABUAD HMS to enable the display of data in a tabular format with advanced features such as searching, filtering, and sorting.

5. Bootstrap: Bootstrap is a front-end framework used in ABUAD HMS to ensure a responsive design and improve the overall look and feel of the application.

6. Python: Python is a programming language used in the development of ABUAD HMS.

7. Flask: Flask is a micro web framework used in ABUAD HMS to develop the web application.

8. Postgres: Postgres is an open-source relational database management system used in ABUAD HMS to store and manage data.

9. SQLite: SQLite is a lightweight relational database management system used in ABUAD HMS for development and testing purposes.

10. Flask_Admin: Flask_Admin is a plugin used in ABUAD HMS to provide a user-friendly interface for managing the database.

11. Flask_Mail: Flask_Mail is a plugin used in ABUAD HMS to enable email functionality such as sending alerts of new offenders to admin.

12. YOLOv5: YOLOv5 is an object detection and classification model used in ABUAD HMS to detect and classify violent and smoking activities.

13. cx_Freeze: cx_Freeze is a tool used in ABUAD HMS to convert Python scripts into standalone executable files.

14. Inno Setup: Inno Setup is a free installer for Windows programs used in ABUAD HMS to create an installation package for the application.


# Flowchart
<p align="center">
  <img src="./screens/flowchart.png" alt="Flow Chart", width="500", height="500">
</p>

# Use Case Diagram
<p align="center">
  <img src="./screens/usecasediagram.png" alt="Flow Chart", width="500", height="500">
</p>

# Screenshots

|     |     |     |
| --- | --- | --- |
| *Screenshot 1: Login page* | *Screenshot 2: Admin panel* | *Screenshot 3: View offenders page* |
|![Screenshot 1](./screens/abuad_hms0.png "Screenshot 1") | ![Screenshot 2](./screens/abuad_hms1.png "Screenshot 2") | ![Screenshot 3](./screens/abuad_hms2.png "Screenshot 3") |
| *Screenshot 4: View database page* | *Screenshot 5: Monitoring page (Smoking)* | *Screenshot 6: Monitoring page (Violence)* |
| ![Screenshot 4](./screens/abuad_hms3.png "Screenshot 4") | ![Screenshot 5](./screens/abuad_hms4.png "Screenshot 5") | ![Screenshot 6](./screens/abuad_hms5.png "Screenshot 6") |




# Demo Videos
# Installation
To use the Abuad HMS application, you can to download and install the application package from the GitHub releases section. Follow these steps to install the application:

1. Go to the GitHub releases page for the project.
2. Download the latest version of the application package (.exe file) to your computer.
3. Double-click the downloaded .exe file to begin the installation process.
4. Follow the on-screen instructions to install the application.
5. Once the installation is complete, launch the application by double-clicking the shortcut on your desktop.

>Note that the installation process may vary depending on your operating system and system configuration. If you encounter any issues during the installation process, please refer to the project documentation or contact the project maintainers for assistance.

# How to Run ABUAD HMS 
Running the Application
To run the Abuad HMS application using Python, follow these steps:

1. Clone the repository to your computer.
```  
git clone https://github.com/Nneji123/ABUAD-HMS.git
cd ABUAD-HMS
```

2. Create and activate your virtual environment. For Windows users, you can activate your environment by running the following command in your terminal:

```bash
python -m venv env
source env\Scripts\activate
```

3. Set the environment variables required for the application. Create a file named `.env` or edit the `.env.example` and add the following environment variables:

```bash
# DATABASE AND SERVER CONFIG
POSTGRES = "postgresql://postgres:password@url:port/database" # POST SERVER
SQLITE = "sqlite:///../database.db" # LOCATION OF SQLITE DATABASE
SERVER_NAME="http://127.0.0.1:3000" # CHANGE THIS TO YOUR PRODUCTION SERVER LINK
SERVER_MODE="DEV" # CHANGE TO `PROD` TO ENABLE PRODUCTION READY SETTINGS
SERIAL="secret" # FOR GENERATING EMAIL HASHCODE

# ADMIN DETAILS
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"
ADMIN_ROLE = "admin"
IS_ADMIN = True

# DEV SERVER CONFIG
DEV_MAIL_SERVER="sandbox.smtp.mailtrap.io"
DEV_MAIL_PORT=2525
DEV_MAIL_USERNAME=""
DEV_MAIL_PASSWORD=""
DEV_SECRET_KEY=""
DEV_SENDER_EMAIL="" # SHOULD BE THE SAME AS DEV_MAIL_USERNAME

# PROD SERVER CONFIG
PROD_MAIL_SERVER= "smtp.gmail.com"
PROD_MAIL_PORT= 465
PROD_MAIL_USERNAME= ""
PROD_MAIL_PASSWORD= ""
PORD_SECRET_KEY=""
PROD_SENDER_EMAIL=""
```

Note that you should replace the values of the environment variables with your own server and database settings, as well as your own email credentials.

4. Install the required Python packages by running the following command in your terminal:


> `pip install -r requirements.txt`

5. Change your directory to the src directory:
> cd src

6. Initialize the local database by running the following command in your terminal:

> `python init.py`

7. Finally, run the application by running the following command in your terminal:

> `python app.py`
Once the application is running, you can visit it in your web browser by going to http://localhost:3000/.


## How to Run as Desktop App
To run the application as a desktop app, follow these steps:

1. Open the app.py file in a text editor.
2. Uncomment the line ui.run() by removing the # symbol in front of it.
3. Comment out the line app.run(...) by adding a # symbol in front of it.
4. Save the changes to the app.py file.

You can now run the application as a desktop app by executing the app.py file with the Python interpreter. To do this, open a command prompt or terminal window and navigate to the directory where the app.py file is located. Then, enter the following command:


> `python app.py`

This will start the Flask web server and launch the application in your default web browser. You can now use the application as usual.

> Note that when running the application as a desktop app, you will not be able to access it from other devices on your network. If you want to run the application on a network, you will need to run it as a web app using the app.run(...) method.

### Building Desktop App with cx_freeze
To build the application using cx_Freeze and setup.py file, follow the steps below:

1. Activate the virtual environment.

2. Install the requirements by running `pip install -r requirements.txt.`

3. Navigate to the src folder in your command prompt or terminal.

4. Run `python setup.py build` to build the application. The built application will be located in the build folder inside the src folder.

> Note that you may need to fine-tune the setup.py file to add additional dependencies or exclude some files depending on your needs.

## How to run in Docker and Docker Compose
To run the application using Docker, follow these steps:

1. Make sure Docker is installed on your machine.
2. Clone the project repository and navigate to the project directory.
3. Create a file called `.env` in the project root directory and add the required environment variables.
4. Build the Docker image using the following command: 
   
   `docker build -t abuad-hms .`
5. Run the Docker container using the following command: `docker run --env-file .env -p 3000:3000 abuad-hms`


To run the application using Docker Compose, follow these steps:

1. Make sure Docker and Docker Compose are installed on your machine.
2. Clone the project repository and navigate to the project directory.
3. Create a file called .env in the project root directory and add the required environment variables.
4. Build and start the Docker container using the following command: docker-compose up --build

These steps will start the application in a Docker container, which can be accessed by visiting http://localhost:3000 in a web browser.


# Deployment
To deploy the application using the Railway or Render button, follow these steps:

<div align="center">

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/Fr7c3B?referralCode=ZYOf2M)
[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
</div>

1. Click on the Railway or Render button in the repository to open the deployment platform.



1. Sign up or log in to the deployment platform.
2. Connect your GitHub account to the deployment platform.
3. Choose the repository where the application code is located.
4. Configure the deployment settings, such as the name of the application, the deployment region, and the deployment type (e.g., Docker container or static site).
5. Deploy the application by clicking on the "Deploy" button.
6. Wait for the deployment process to finish. Once it's done, the application will be available at the URL provided by the deployment platform.

> Note that the specific steps and options may vary depending on the deployment platform used. It's recommended to check the documentation and tutorials provided by the platform for more detailed instructions on how to deploy the application.
# References
References:

1. Ultralytics. (2021). YOLOv5. https://github.com/ultralytics/yolov5
2. Jocher, G. (2021). YOLOv5. GitHub repository. https://github.com/ultralytics/yolov5
3. Nariani, D. (2022). Violence&not_violence Dataset. Roboflow Universe. https://universe.roboflow.com/dinesh-nariani-rmnpr/violence-not_violence-ziv7b
4. Yi. (2023). smoke Dataset. Roboflow Universe. https://universe.roboflow.com/yi-emjui/smoke-qkxhl
# License
[MIT](./LICENSE.md)


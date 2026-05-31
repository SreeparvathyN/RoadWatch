#  RoadWatch – Smart Road Monitoring Platform

RoadWatch is a web-based application developed to help identify road damages such as potholes and cracks from uploaded road images. The project aims to support faster reporting and monitoring of road conditions using image processing and AI-assisted detection techniques.

##  Project Overview

Poor road conditions can lead to accidents, vehicle damage, and increased maintenance costs. RoadWatch provides a simple platform where users can upload road images and receive a basic analysis of visible road damage.

The system processes uploaded images, highlights damaged regions, estimates severity levels, and stores records for future reference.

##  Features

* Upload road images through a user-friendly web interface
* Detect road cracks and potholes from images
* Display processed output images with marked damage regions
* Generate severity levels based on detected damage
* Store uploaded image records using SQLite
* Dashboard for viewing reports and statistics
* Responsive and modern user interface

##  Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI & Image Processing

* OpenCV
* NumPy

### Database

* SQLite

### Development Tools

* Visual Studio Code
* GitHub

##  Project Structure

RoadWatch/
│
├── app.py
├── detection.py
├── roadwatch.db
├── requirements.txt
│
├── templates/
│ ├── index.html
│ ├── dashboard.html
│ ├── about.html
│ └── result.html
│
├── static/
│ ├── uploads/
│ └── results/

##  How to Run

1. Clone the repository

git clone 

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open the browser and visit

http://127.0.0.1:5000

##  Future Improvements

* YOLO-based object detection for higher accuracy
* GPS-based location tagging
* Automatic complaint generation
* Mobile application integration
* Real-time road monitoring system

##  Developed By

RoadWatch was developed as a student project to explore the practical applications of computer vision, web development, and intelligent transportation systems.

The project reflects our effort to combine technology with public infrastructure monitoring and road safety improvement.

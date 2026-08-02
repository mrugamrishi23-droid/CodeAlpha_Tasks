\# 👁️ Real-Time Object Detection \& Tracking



> \*\*An advanced computer vision application using YOLOv8.\*\*

> Developed as Task 4 for the CodeAlpha Artificial Intelligence Internship.



\## 📖 Overview

This project implements a real-time object detection and tracking system using a webcam feed. By leveraging the state-of-the-art YOLOv8 model alongside the BoT-SORT tracking algorithm, the application can accurately identify multiple objects, draw bounding boxes, and assign persistent tracking IDs across consecutive video frames.



\## ✨ Features

\* \*\*Real-Time Processing:\*\* Analyzes live video feeds directly from the user's webcam with minimal latency.

\* \*\*High-Accuracy Detection:\*\* Utilizes the YOLOv8 nano model (`yolov8n`) for efficient and precise object recognition.

\* \*\*Persistent Object Tracking:\*\* Integrates BoT-SORT tracking to assign and maintain unique IDs for objects as they move across the screen.

\* \*\*Dynamic Annotation:\*\* Automatically draws customized bounding boxes, confidence scores, and tracking IDs on the video stream.



\## 🛠️ Technologies Used

\* \*\*Core Language:\*\* Python

\* \*\*Computer Vision:\*\* OpenCV (`cv2`)

\* \*\*Deep Learning Framework:\*\* Ultralytics (YOLOv8)



\## 🚀 Getting Started



\### Prerequisites

\* \[Python 3.8+](https://www.python.org/downloads/)

\* A functioning webcam connected to your machine.



\### Installation \& Execution



\*\*1. Clone the repository:\*\*

```bash

git clone \[https://github.com/YOUR\_USERNAME/CodeAlpha\_Object\_Detection\_Tracking.git](https://github.com/YOUR\_USERNAME/CodeAlpha\_Object\_Detection\_Tracking.git)

cd CodeAlpha\_Object\_Detection\_Tracking



2\. Create and activate a virtual environment (Recommended):



Bash

\# Windows

python -m venv venv

.\\venv\\Scripts\\activate



3\. Install the required dependencies:



Bash

pip install -r requirements.txt



4\. Run the application:



Bash

python object\_tracker.py

Note: Upon the first execution, the script will automatically download the yolov8n.pt model weights (approx. 6MB).



Developed by \[Mrugam Rishikesh] for the CodeAlpha AI Internship Program.


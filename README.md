Automated Attendance System using Face Recognition
Overview

Our project is an Automated Attendance System using Face Recognition. Instead of the traditional manual roll call, our system automatically detects and recognizes faces and marks attendance digitally.

The core idea is simple:

Register people by collecting their face images.
Train a lightweight classifier on top of a deep learning face model.
Detect and recognize faces during runtime.
Automatically record attendance in an Excel file.
Problem Statement

Traditional attendance systems are often time-consuming and error-prone. Teachers need to call names manually, and sometimes proxy attendance or mistakes can occur.

To solve this, we built an automated system that uses face recognition to mark attendance automatically.

System Architecture

Our system follows a two-stage pipeline.

Stage 1 — Face Embedding using FaceNet

We use a deep neural network based on FaceNet to convert every face image into a fixed-length numerical vector called an embedding.

Each face → converted into a 512-dimensional embedding
Faces of the same person appear closer in vector space
Faces of different people appear farther apart

This embedding captures the identity of a person.

Stage 2 — Classification using SVM

On top of the embeddings, we train a Linear SVM classifier.

The SVM learns how to separate embeddings belonging to different identities.

Advantages of this approach:

Training is very fast
The deep model does not need retraining
Works efficiently even on normal laptops
Workflow

The application follows a simple pipeline:

CREATE → TRAIN → TEST → RUN → EXPORT ATTENDANCE
Step 1 — Creating the Dataset

The process begins with the CREATE option in the desktop application.

Steps
The user selects an output folder.
The user enters the name of the person (example: Kamal).
The webcam or video stream opens.
The system detects faces using MTCNN (TensorFlow implementation).
When the user presses S, the detected face is cropped and saved.

````
Example Dataset Structure
output/
│
├── kamal/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│
├── hasan/
│   ├── img1.jpg
│   ├── img2.jpg
````

Each person has:

One folder
Multiple face images

This improves recognition accuracy.

Step 2 — Training the Model

Next comes the TRAIN step.

The user selects the parent dataset folder (e.g. output/).

Training Pipeline
All images are loaded.
Each image is resized to 160 × 160 pixels.
The image is passed to FaceNet.
FaceNet generates 512-dimensional embeddings.
These embeddings are used to train a Linear SVM classifier.
Files Generated

After training, the system saves:

classifier.pkl   → trained SVM classifier
class_names.pkl  → list of registered identities

Important point:

We do not retrain the deep neural network.
We only train a lightweight classifier on top of embeddings.

This makes the system fast and efficient.

Step 3 — Testing the Model

After training, we evaluate the model using the TEST stage.

Evaluation Process
Faces are converted into embeddings using FaceNet.
The trained SVM classifier predicts identities.
The system reports:
Prediction accuracy
Confidence scores

This step provides quantitative evaluation of the model performance.

Step 4 — Live Face Recognition

The RUN stage represents the real-world usage of the system.

The user loads:

FaceNet model (.pb file)
Trained classifier (.pkl)

The system can process:

Webcam input
Video files
Images
Recognition Pipeline

For each frame:

Faces are detected
Faces are cropped and preprocessed
FaceNet generates embeddings
The SVM classifier predicts the identity

If the confidence score crosses a predefined threshold, the person is considered recognized.

Step 5 — Saving Attendance to Excel

Attendance is automatically saved in an Excel file.

If the file does not exist, the system creates:

attendance/SAMPLE.xlsx
Attendance Format
Name	Session 1	Session 2	Timestamp
Kamal	P	A	10:32 AM
Rahul	A	P	10:33 AM

Where:

P → Present
A → Absent

This allows easy storage, review, and auditing of attendance records.

Technologies Used
Python
TensorFlow
FaceNet
MTCNN
Scikit-learn (SVM)
OpenCV
NumPy
Pandas
Excel Export

````
Project Pipeline Summary
CREATE
   ↓
Capture face images

TRAIN
   ↓
Generate embeddings + train SVM

TEST
   ↓
Evaluate model accuracy

RUN
   ↓
Real-time face recognition

EXPORT
   ↓
Attendance saved to Excel
````

Applications

This system can be used in:

Classrooms
Universities
Offices
Events
Conferences
Employee attendance systems
Conclusion

By combining deep learning for face representation (FaceNet) and classical machine learning for classification (SVM), our system provides a fast, practical, and scalable attendance solution.

It eliminates manual attendance, reduces errors, and automates record management.

Thank you.

# Automated Attendance System using Face Recognition

Instead of the traditional manual roll call, our system automatically detects and recognizes faces and marks attendance digitally.

**The core idea is simple.**
First, we register people by collecting their face images. Then we train a lightweight classifier on top of a deep learning face model. And finally, during runtime, the system detects faces from a webcam or video, identifies who they are, and automatically records attendance in an Excel file for proper records and auditing.

---

## Problem and Our Approach

Traditional attendance systems are often time-consuming and error-prone. Teachers have to call out names manually, and sometimes proxies or mistakes happen.

To solve this, we designed a **two-stage pipeline**.

- **Stage 1 — FaceNet:** A deep neural network that converts every face image into a fixed-length numerical vector called an *embedding*. These embeddings capture the identity of a person, meaning that faces of the same person appear close to each other in vector space.

- **Stage 2 — Linear SVM Classifier:** Trained on top of these embeddings. The SVM learns how to separate the embeddings based on different person identities. This approach keeps training fast and lightweight, since the heavy work is already handled by the pretrained FaceNet model.

---

## Workflow

```
CREATE  →  TRAIN  →  TEST  →  RUN  →  Excel Export
```

---

## Step 1 — Creating the Dataset

The process starts with the **CREATE** option in our desktop application.

- The user selects an output folder and enters the name of the person — for example, `Kamal`
- The system opens the webcam or a video stream
- We use an **MTCNN-based** face detection system implemented in TensorFlow to detect faces in real time
- Whenever the user presses **`S`**, the system crops the detected face and saves it as an image

Images are stored inside a separate folder for each person:

```
output/
└── kamal/
    ├── img1.jpg
    ├── img2.jpg
    └── ...
└── Hasan/
    ├── img1.jpg
    ├── img2.jpg
    └── ...

```

By repeating this process, we collect multiple face samples for each individual, which helps improve the accuracy of the classifier later.

**Dataset structure:**
- One folder per person
- Multiple face images inside each folder

---

## Step 2 — Training the Model

Next comes the **TRAIN** step.

- The user selects the parent dataset folder (e.g., `output/`)
- The application loads every image, resizes it to **160×160 pixels**, and feeds it into the FaceNet model
- FaceNet generates **512-dimensional embeddings** for each image
- These embeddings are used to train a **linear SVM classifier** with probability estimation

After training, the system saves:

| File | Description |
|------|-------------|
| `classifier.pkl` | The trained SVM model |
| `class names list` | Identities of all registered people |

> **Note:** We do not retrain the deep neural network itself. We only train a lightweight classifier on the embeddings, which makes the system fast and practical even on a laptop.

---

## Step 3 — Testing the Model

After training, we move to the **TEST** stage.

- The system evaluates the trained classifier using a separate dataset or a train–test split
- Faces are embedded again using FaceNet and predictions are made using the SVM

The system reports:
- Prediction accuracy
- Confidence scores for each prediction

This step gives us quantitative proof that the system works reliably, not just visually.

---

## Step 4 — Live Face Recognition

Now comes the **RUN** stage, which represents real-world usage of the system.

**The user loads:**
- The FaceNet model (`.pb` file)
- The trained classifier (`.pkl`)

**The system can process:**
- Webcam input
- Video files
- Images

**For each frame:**
1. Faces are detected
2. The faces are cropped and processed
3. FaceNet generates embeddings
4. The SVM predicts the identity

If the prediction confidence crosses a threshold, the person is considered recognized and their name is added to the attendance list for that session.

---

## Step 5 — Saving Attendance to Excel

Attendance is automatically saved in an Excel file:

```
attendance/SAMPLE.xlsx
```

Each registered person appears as a row, based on the folders in the dataset.

| Person | Session 1 | Session 2 |
|--------|-----------|-----------|
| Kamal  | P         | A         |

- **P** → Present
- **A** → Absent
- A **timestamp** is added for every session

This makes the attendance easy to store, review, and audit later.

---

## Summary

| Step | Action |
|------|--------|
| **CREATE** | Builds the labeled face dataset |
| **TRAIN** | Generates embeddings and trains the SVM classifier |
| **TEST** | Evaluates the model accuracy |
| **RUN** | Performs live face recognition |
| **Excel Export** | Records attendance automatically |

By combining deep learning for face representation and classical machine learning for classification, our system achieves a fast, practical, and scalable attendance solution suitable for classrooms, events, or institutions.

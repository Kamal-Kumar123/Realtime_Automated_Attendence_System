# 🎓 Automated Attendance System using Face Recognition

An intelligent attendance management system that uses **deep learning face recognition** to automatically detect, identify, and record attendance — eliminating manual roll calls entirely.

---

## 📌 Overview

Traditional attendance systems are time-consuming and error-prone. Teachers manually call out names, and issues like proxy attendance or human error are common.

This system solves that with a **two-stage deep learning pipeline**:

1. **FaceNet** — A deep neural network that converts face images into 512-dimensional numerical vectors called *embeddings*, which capture a person's identity.
2. **Linear SVM Classifier** — Trained on top of FaceNet embeddings to distinguish between different individuals. Fast and lightweight, since the heavy lifting is done by the pretrained FaceNet model.

---

## ✨ Features

- 📷 Real-time face detection using **MTCNN** (TensorFlow)
- 🧠 Face embedding via pretrained **FaceNet** model
- ⚡ Fast classification using **Linear SVM**
- 📊 Attendance exported to **Excel (.xlsx)** with timestamps
- 🖥️ Desktop GUI with CREATE / TRAIN / TEST / RUN workflow

---

## 🔄 Workflow

```
CREATE → TRAIN → TEST → RUN → Excel Export
```

---

## 🚀 Step-by-Step Guide

### Step 1 — 📁 Create Dataset

Use the **CREATE** option in the desktop application.

- Enter the person's name (e.g., `Kamal`)
- Select an output folder
- The webcam opens — press **`S`** to capture and save face images

Captured images are saved in a structured format:

```
output/
├── kamal/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
├── sara/
│   └── ...
```

> Collect multiple images per person to improve classifier accuracy.

---

### Step 2 — 🏋️ Train the Model

Use the **TRAIN** option.

- Select the parent dataset folder (e.g., `output/`)
- Each image is resized to **160×160 pixels** and fed into FaceNet
- FaceNet generates **512-dimensional embeddings** per image
- A **Linear SVM** is trained on these embeddings

**Output files saved:**

| File | Description |
|------|-------------|
| `classifier.pkl` | Trained SVM model |
| `class_names.pkl` | List of registered person identities |

> ℹ️ The FaceNet model is **not retrained** — only the SVM classifier is trained, keeping the process fast and practical.

---

### Step 3 — 🧪 Test the Model

Use the **TEST** option to evaluate performance.

- Faces are re-embedded using FaceNet
- The SVM makes predictions on a test split or separate dataset
- Reports generated:
  - ✅ Prediction accuracy
  - 📈 Confidence scores per prediction

---

### Step 4 — 🎥 Run Live Face Recognition

Use the **RUN** option for real-world deployment.

**Load:**
- FaceNet model (`.pb` file)
- Trained classifier (`.pkl` file)

**Supports:**
- 📹 Webcam input
- 🎞️ Video files
- 🖼️ Static images

**For each frame:**
1. Faces are detected using MTCNN
2. Detected faces are cropped and preprocessed
3. FaceNet generates embeddings
4. SVM predicts the identity

> If prediction **confidence exceeds the threshold**, the person is marked as recognized and added to the attendance list.

---

### Step 5 — 📊 Export Attendance to Excel

Attendance is automatically saved to:

```
attendance/SAMPLE.xlsx
```

| Person | Session 1 | Session 2 | ... |
|--------|-----------|-----------|-----|
| Kamal  | P         | A         | ... |
| Sara   | P         | P         | ... |

- **P** = Present
- **A** = Absent
- Timestamp is added for every session

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Face Detection | MTCNN (TensorFlow) |
| Face Embedding | FaceNet (pretrained) |
| Classification | Linear SVM (scikit-learn) |
| Attendance Export | OpenPyXL / Excel |
| GUI | Desktop Application (Python) |

---

## 📂 Project Structure

```
project/
├── output/                  # Dataset folder (one subfolder per person)
├── attendance/
│   └── SAMPLE.xlsx          # Auto-generated attendance file
├── models/
│   ├── facenet_model.pb     # Pretrained FaceNet model
│   └── classifier.pkl       # Trained SVM classifier
├── src/
│   ├── create_dataset.py
│   ├── train.py
│   ├── test.py
│   └── run.py
└── README.md
```

---

## 📸 How to Use

```bash
# 1. Clone the repository
git clone https://github.com/your-username/attendance-face-recognition.git
cd attendance-face-recognition

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

> Built with ❤️ using deep learning for face representation and classical ML for classification — fast, practical, and scalable for classrooms, events, and institutions.

# 🧠 ReMind

## 📖 Overview

ReMind is a fun and interactive Python learning app designed to help users retain knowledge through active recall - one of the most effective techniques for memory improvement.

Users type in what they want to learn, take a moment to study it, and then try to recall what they can remember.
ReMind compares the two texts, gives a recall accuracy score, and encourages users to keep improving until they master it.

> 💬 "Learn. Recall. Repeat. ReMind helps you make learning stick."

## 🎯 Features

- Simple and Friendly Interface – Built with Tkinter for a beginner-friendly experience.
- Real-Time Feedback – Compares what you learned with what you recalled.
- Recall Scoring System – Get a similarity score (in %) for every attempt.
- Instant Motivation – Visual feedback to encourage improvement.
- Expandable Design – Ready for future AI upgrades (semantic similarity, NLP, etc.).

## 🛠️ Technologies Used

- Python 3
- Tkinter – for the graphical user interface (GUI)
- difflib – for comparing text similarity
- (Future Enhancements)
  - nltk / spaCy for Natural Language Processing
  - sentence-transformers for semantic similarity (AI-based scoring)
 
## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.8+ installed.
Tkinter is included with Python by default, so no extra installations are needed.

### 📦 Installation

#### 1. Clone this repository:
```bash
git clone https://github.com/yourusername/ReMind.git
```
#### 2. Navigate into the folder:
```bash
cd ReMind
```
#### 3. Run the app:
```bash
python remind.py
```

## 💻 How It Works

1. Type or paste something you want to learn in the first text box.
2. Read and understand it for a few seconds.
3. Type what you can recall in the second text box.
4. Click “Check Recall” to see your recall score.
5. Keep trying until you reach your target score!

## 🧩 Example

| Step   | Input                                             | Output |
| ------ | ------------------------------------------------- | ------ |
| Learn  | “The mitochondria is the powerhouse of the cell.” |        |
| Recall | “Mitochondria produces energy for the cell.”      |        |
| Result | ✅ *Your Recall Score: 78%*                        |        |


## 🌟 Future Improvements

1. Highlight missed or extra words.
2. Add progress tracking and user profiles.
3. Introduce semantic similarity using AI/NLP.
4. Include voice input/output for accessibility.
5. Deploy a web-based version using Streamlit.

## 👩‍💻 Project Structure

```bash
ReMind/
│
├── remind.py          # Main Python script (Tkinter app)
├── README.md          # Project documentation
└── assets/            # (optional) images, icons, or logo files
```

## 💡 Educational Purpose

1. ReMind is designed as a learning project for young Python coders, combining:
2. GUI programming with Tkinter
3. String and text processing
4. Logical thinking through active recall
5. An introduction to AI and machine learning concepts

## 🧑‍🏫 Created For

A coding education initiative that encourages young learners to build practical apps using Python and AI concepts.

## 🪄 Author & Mentorship

Project Mentor: Juliet Nkwor
Guiding young coders to build creative, purposeful, and intelligent Python applications.


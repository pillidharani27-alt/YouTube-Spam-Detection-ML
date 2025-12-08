# Machine Learning-Based Spam Comments Detection On You Tube
YouTube Spam Comment Detection using Machine Learning

A complete Machine Learning & NLP-based system to automatically detect spam comments on YouTube, using advanced text preprocessing, multiple ML algorithms, and a Flask web app for real-time prediction.

This project demonstrates data preprocessing, model training, evaluation, deployment, UI integration, and MySQL connectivity, making it a full end-to-end ML application.

🚀 Project Overview

YouTube receives millions of comments daily, many of which are spam, scam, promotional, or harmful.
This project uses Machine Learning + NLP to classify comments as:

Spam

[!image alt](https://github.com/pillidharani27-alt/YouTube-Spam-Detection-ML/blob/main/Screenshots/not%20spam.png?raw=true)

Not Spam

The system is trained using multiple ML algorithms and deployed using a Flask Web Application, where users can input any comment and instantly see prediction results.

🧠 Features

✔ Cleaned & preprocessed YouTube comments dataset
✔ NLP-based text vectorization
✔ Trained multiple ML models
✔ Achieved high accuracy using AdaBoost
✔ Built a prediction UI using Flask
✔ Integrated MySQL login/register system
✔ Saved ML models for reuse (.sav & .h5 files)
✔ Professional documentation & UML diagrams included# YouTube-Spam-Detection
🤖 Machine Learning Models Used

The following algorithms were trained and evaluated:

Model	Status	Purpose
Naive Bayes	✔	Baseline text classification
Decision Tree	✔	Pattern-based classification
AdaBoost	⭐ Best Model	Highest accuracy & best performance
MLP Classifier	✔	Neural network approach
KNN	✔	Similarity-based classification
SVM	✔	Margin-based classifier
FFNN (TensorFlow)	✔	Deep learning model

📌 Best performing model:

⭐ AdaBoost Classifier — Highest Accuracy
🏗️ System Architecture

This project includes:

Backend ML logic → /models, /app.py, .sav files

Frontend UI → /templates, /static

Dataset handling → /Data set

Documentation → PDF + PPT

MySQL database integration (db.sql)

Tech Stack
🧠 Machine Learning

Python

pandas, numpy

scikit-learn

TensorFlow

joblib

🌐 Web Framework

Flask

HTML, CSS, JS

🗄 Database

MySQL (mysql-connector-python)

Dataset Information

Dataset includes YouTube comments with labels:

spam

ham / not spam

Text is preprocessed using:

Lowercasing

Stopword removal

Tokenization

Vectorization

📝 Conclusion

This project successfully demonstrates an end-to-end Machine Learning system for detecting spam comments on YouTube.
Using models like AdaBoost and Deep Learning (FFNN), the system achieves high accuracy and provides fast real-time predictions through a Flask-based user interface.

It can be extended to:

Multilingual comment detection

Deep learning (LSTM/BERT)

Real-time deployment on cloud platforms

🙌 Author

P.V. Dharani – MCA 4th Semester
Machine Learning & Data Science Enthusiast

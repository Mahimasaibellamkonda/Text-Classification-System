# Text Classification System

A web-based Natural Language Processing application that automatically classifies text messages into different categories using machine learning.

This project demonstrates a basic Spam and Normal message classification system using TF-IDF and the Multinomial Naive Bayes algorithm.

## Features

* Classifies text messages automatically
* Detects Spam and Normal messages
* Uses TF-IDF for text feature extraction
* Uses Multinomial Naive Bayes for classification
* Displays prediction confidence
* Simple web-based interface
* Responsive design

## Technologies Used

* Python
* Flask
* Scikit-learn
* HTML5
* CSS3
* TF-IDF
* Multinomial Naive Bayes

## Project Structure

```text id="k4xq2m"
Text-Classification-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

Open a terminal inside the project folder and run:

```bash id="y2e7p1"
pip install -r requirements.txt
```

## Running the Application

Run the following command:

```bash id="h6zq9a"
python app.py
```

The application will start at:

```text id="f8n2kw"
http://127.0.0.1:5000
```

Open the address in your browser.

## How It Works

1. A small labeled dataset of Spam and Normal messages is created.
2. TF-IDF converts the text into numerical features.
3. A Multinomial Naive Bayes classifier is trained using these features.
4. The user enters a new message through the web interface.
5. The message is transformed using the same TF-IDF vectorizer.
6. The trained model predicts the message category.
7. The prediction and confidence score are displayed.

## Example 1

### Input

```text id="k2w5hm"
Congratulations! You have won a free prize.
```

### Output

```text id="2q7vra"
Classification: Spam
```

## Example 2

### Input

```text id="r9t3cx"
Please submit the project report tomorrow.
```

### Output

```text id="3xq8pn"
Classification: Normal
```

## Applications

Text classification can be used in:

* Spam detection
* Email filtering
* Sentiment classification
* News categorization
* Customer feedback analysis
* Social media monitoring
* Document classification
* Content filtering

## Advantages

* Fast classification
* Simple implementation
* Easy-to-use interface
* Demonstrates a real machine-learning NLP workflow
* Can be extended with larger datasets

## Limitations

The application uses a small demonstration dataset. For real-world classification, a much larger and more diverse labeled dataset should be used to improve accuracy.

## Purpose

This project demonstrates the application of Natural Language Processing and machine learning techniques for automatically classifying textual data.

## Author

B.E. CSE Student

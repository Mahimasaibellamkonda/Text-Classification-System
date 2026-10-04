from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)


# Training dataset
training_texts = [
    "Congratulations you have won a free prize",
    "You won a free lottery ticket",
    "Claim your free reward now",
    "Win a cash prize by clicking this link",
    "You have been selected for a free gift",
    "Get your free bonus today",
    "Congratulations claim your reward",
    "You are the lucky winner of a prize",

    "Can you send me the project report",
    "The meeting is scheduled for tomorrow",
    "Please submit the assignment today",
    "I will call you after the class",
    "The project presentation is next week",
    "Please bring your notes to class",
    "Can we discuss the project tomorrow",
    "The exam timetable has been released"
]

training_labels = [
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",

    "Normal",
    "Normal",
    "Normal",
    "Normal",
    "Normal",
    "Normal",
    "Normal",
    "Normal"
]


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_texts)

model = MultinomialNB()
model.fit(X, training_labels)


def classify_text(text):
    transformed_text = vectorizer.transform([text])

    prediction = model.predict(transformed_text)[0]

    probabilities = model.predict_proba(transformed_text)[0]
    confidence = round(max(probabilities) * 100, 2)

    return prediction, confidence


@app.route("/", methods=["GET", "POST"])
def index():

    text = ""
    prediction = None
    confidence = None

    if request.method == "POST":

        text = request.form.get("text", "").strip()

        if text:
            prediction, confidence = classify_text(text)

    return render_template(
        "index.html",
        text=text,
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)

# AI Spam Email Checker

A beginner-friendly BCA college project that uses Machine Learning to classify email/message text as **Spam** or **Not Spam**.

## Technologies

- Python
- Flask
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS
- JavaScript

## Machine Learning

The project uses:

1. **TF-IDF Vectorizer** - converts text into numerical features.
2. **Multinomial Naive Bayes** - learns from the training data and classifies messages.

## Project Structure

```text
AI-Spam-Email-Checker/
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation

```bash
pip install -r requirements.txt
```

## Train the model

```bash
python train_model.py
```

This creates `model.pkl`.

## Run the website

```bash
python app.py
```

Open:

```text
https://ai-spam-email-checker.onrender.com
```

## Dataset

The included `spam.csv` is a tiny demo dataset so that the project runs immediately. For a meaningful Machine Learning evaluation, replace it with a larger spam/ham dataset containing:

```text
label,message
ham,Normal message
spam,Spam message
```

For a college report, mention the real dataset source if you replace the demo data.

## Features

- AI/ML spam classification
- Spam probability
- Word and character count
- Link count
- Simple suspicious-term count
- Example messages
- Mobile responsive UI
- No login
- No email account access
- No permanent message storage

## Future Scope

- Larger training dataset
- Phishing URL detection
- Attachment analysis
- Gmail/Outlook integration
- User accounts and history
- Deep learning/transformer models
- Cloud deployment

## Disclaimer

This is an educational project. The prediction is not a guarantee that a real-world email is safe or malicious.

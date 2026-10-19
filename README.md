# Predictive Model for Detecting Fraudulent Social Media Profiles

A machine learning-based web application designed to predict potentially fraudulent social media profiles using profile-related features and predictive analysis.

## 📌 About the Project

Social media platforms are increasingly affected by fake and fraudulent profiles that may be used for spam, impersonation, scams, and other deceptive activities.

This project aims to develop a predictive model that helps identify potentially fraudulent social media profiles by analyzing relevant profile characteristics. The application uses a web interface to accept input and display prediction results.

Built using Python, Flask, and HTML, the project demonstrates how machine learning concepts can be integrated into a web application.

## 🎯 Objectives

- Develop a predictive approach for identifying potentially fraudulent social media profiles.
- Analyze relevant profile characteristics for fraud detection.
- Integrate prediction functionality into a web application.
- Provide a simple and user-friendly interface for submitting profile information.
- Explore the application of machine learning in social media fraud detection.

## ✨ Features

- **Web-Based Interface:** Interact with the application through HTML pages.
- **Prediction Functionality:** Generate a prediction using the application's implemented logic.
- **Results Page:** Display the output through a dedicated results page.
- **Flask Integration:** Connect the frontend interface with Python application logic.
- **Extensible Design:** Provides a foundation for future improvements in model development and evaluation.

## 🛠️ Technologies Used

- **Python** — application logic and prediction functionality
- **Flask** — web application framework
- **HTML5** — frontend structure
- **Git and GitHub** — version control and project hosting

*Add other libraries or machine learning frameworks here if your implementation uses them.*

## 📂 Project Structure

```text
fraud_github/
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
│
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

- Python 3 installed
- pip package manager
- A web browser

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Aaditi297/fraudulent-social-media-profile-detection.git
```

**2. Navigate to the project directory**

```bash
cd fraudulent-social-media-profile-detection
```

**3. Create a virtual environment**

Windows:

```bash
python -m venv venv
```

**4. Activate the virtual environment**

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
venv\Scripts\activate.bat
```

**5. Install Flask**

```bash
python -m pip install flask
```

If your project uses additional libraries, install those as well.

**6. Run the application**

```bash
python app.py
```

**7. Open the application**

Visit the local address shown in your terminal, commonly:

http://127.0.0.1:5000

## 🔍 How It Works

1. Open the application's home page.
2. Enter the profile information requested by the interface.
3. Submit the information for processing.
4. The application executes its implemented prediction logic.
5. View the resulting output on the results page.

The exact prediction process depends on the model and logic implemented in `app.py`.

## 📊 Future Improvements

- Integrate and validate a trained machine learning classification model.
- Add suitable data preprocessing and feature engineering.
- Evaluate model performance using precision, recall, F1-score, and a confusion matrix.
- Improve input validation and error handling.
- Enhance the interface and user experience.
- Add appropriate testing and documentation.

## ⚠️ Disclaimer

Predictions produced by this project should be treated as estimates, not definitive proof that a social media profile is fraudulent. The reliability of the output depends on the data, features, and prediction method used.

## 👩‍💻 Author

**Aaditi Sachdeva**

GitHub: [@Aaditi297](https://github.com/Aaditi297)

## 📄 License

No license has been specified for this project yet.

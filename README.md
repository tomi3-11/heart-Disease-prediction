# Heart Disease Prediction System

A software engineering and machine learning project for building a heart disease prediction system.

## Overview

The goal of this project is to develop a machine learning model that predicts the likelihood of heart disease from patient clinical data and integrate it into a software application.

The project follows a structured development process, beginning with understanding the dataset and ending with a complete application.

## Objectives

- Understand the dataset and problem domain.
- Perform exploratory data analysis (EDA).
- Clean and preprocess the data.
- Train and compare multiple machine learning algorithms.
- Evaluate model performance.
- Save the selected model.
- Integrate the model into a backend API.
- Build a complete software application.

---

## Repository Structure

```text
.
├── Backend
│   └── docs.md
├── datasets
│   └── heart_cleaned.csv
├── documentation
├── Documentation
│   └── docs.md
├── Frontend
│   └── docs.md
├── notebooks
│   ├── heart_disease_annotated.ipynb
│   └── random_forest_model.joblib
├── README.md
└── requirements.txt

7 directories, 8 files

```

### Directories

#### `datasets/`

Contains datasets used during development.

#### `documentation/`

Contains project documentation, research notes, design decisions, and reports.

#### `notebooks/`

Contains Jupyter notebooks for:

- Data exploration
- Data preprocessing
- Model training
- Model evaluation
- Experiments

Saved development models may also be stored here.

---

# Development Stages

## Stage 1 — Data Understanding

Tasks

- Read the dataset documentation.
- Understand every feature.
- Load the dataset.
- Inspect data types.
- Check missing values.
- Explore target distribution.
- Perform exploratory data analysis.

Deliverables

- Dataset summary
- Feature descriptions
- Initial visualizations

---

## Stage 2 — Data Preprocessing

Tasks

- Handle missing values.
- Convert data types where necessary.
- Encode categorical features.
- Scale features when required.
- Split the dataset into training and testing sets.

Deliverables

- Clean dataset
- Preprocessing pipeline

---

## Stage 3 — Model Development

Algorithms to Use

- Random Forest Classifier via ensemble

Evaluation metrics

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Deliverables

- Selected model

---

## Stage 4 — Model Persistence

Tasks

- Save the trained model.
- Save preprocessing objects if required.
- Verify model loading.

Deliverables

- Trained model
- Prediction pipeline

---

## Stage 5 — Backend Integration

Possible frameworks

- FastAPI
- Flask
- Django
- Nodejs (Express)
- Nextjs (frontend)

Tasks

- Create prediction endpoints.
- Load the trained model.
- Validate user input.
- Return predictions.

---

## Stage 6 — Software Development

Planned features

- User authentication
- Patient management
- Prediction history
- Dashboard
- Reports
- Explainable predictions
- Database integration

---

# Technologies

Current

- Python
- Jupyter Notebook
- pandas
- NumPy
- scikit-learn
- joblib

Planned

- FastAPI or Django
- PostgreSQL
- Docker
- pytest
- SHAP

---

## Getting Started

## Clone the repository

```bash
# SSH
git clone git@github.com:tomi3-11/heart-Disease-prediction.git

# HTTPS
git clone https://github.com/tomi3-11/heart-Disease-prediction.git

cd heart-Disease-prediction
```

> **Note:** Anaconda Navigator is recommended for the machine learning notebooks. It is not required for the backend application.

---

## Repository Components

| Component | Description |
|-----------|-------------|
| `notebooks/` | Machine learning development, experimentation, and model training |
| `Backend/` | FastAPI backend API |
| `Frontend/` | Frontend application |
| `datasets/` | Datasets used during development |
| `documentation/` | Project documentation |

---

# Backend Setup

The backend can be run using either Docker or a local Python environment.

## Option 1 — Docker (Recommended)

```bash
cd Backend

docker compose up --build
```

The backend will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

For additional backend documentation, see:

```
Backend/README.md
```

---

## Option 2 — Local Installation

Navigate to the backend directory.

```bash
cd Backend
```

Create a virtual environment.

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Copy the example environment file.

Linux/macOS

```bash
cp .env.example .env
```

Windows

```cmd
copy .env.example .env
```

Update the values in `.env` as required.

Run the application.

```bash
uvicorn app.main:app --reload
```

---

# Machine Learning Environment

Install the project dependencies.

```bash
pip install -r requirements.txt
```

Open the notebook.

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

The notebook used for model development is located at:

```
notebooks/heart_disease_annotated.ipynb
```

---

# Documentation

Additional documentation is available in the following directories.

```
Backend/
    README.md
    API.md
    ARCHITECTURE.md

documentation/

Frontend/
```
---

# Contributing

Before submitting changes:

- Create a new branch.
- Keep commits focused.
- Write clear commit messages.
- Update documentation if necessary.
- Test your changes before opening a pull request.

Example

```bash
git checkout -b feature/feature-name
```

Example commit messages

```text
feat: add data preprocessing pipeline
fix: handle missing values
docs: update README
refactor: simplify model training
```

---

# License

No license has been added yet.


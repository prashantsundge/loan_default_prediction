# Loan Default Prediction Project 🚀

A Machine Learning pipeline designed to predict loan defaults using structured data.  
This project is organized and implemented following software engineering best practices (OOPs) in Python.

---

## 🗂️ Project Index

1. **Project Setup**
    - Created project folder structure using `setup_project_structure.py`.
    - Initialized Git repository and pushed to GitHub.
    - Set up Python `venv` virtual environment.
    - Installed all dependencies via `requirements.txt`.

2. **Data Handling**
    - Collected dataset from Kaggle: [Loan Default Dataset](https://www.kaggle.com/datasets/hemanthsai7/loandefault).
    - Created a `data_loader.py` module to load CSV files with error handling and logging.
    - Loaded and verified data through `main.py` and Jupyter Notebook.

3. **Logging & Exception Handling**
    - Created `logger.py` for centralized log tracking.
    - Created `exception.py` for structured exception handling.
    - Integrated both in all Python scripts.

4. **Exploratory Data Analysis (EDA)**
    - Performed deep data profiling and missing value analysis.
    - Created informative visualizations:
        - Distribution plots
        - Correlation heatmap
        - Count plots and categorical vs target analysis.
    - Identified **class imbalance** in the `Default` target column.

5. **Data Balancing**
    - Explored data balancing techniques:
        - Undersampling ✅ (Applied)
        - Oversampling (SMOTE, ADASYN) — [Considered for future]
    - Exported balanced dataset for further processing.

6. **Feature Exploration & Insights**
    - Derived observations from EDA:
        - Education, Employment Type, Marital Status, Mortgage, Dependents, Loan Purpose, and Co-signer significantly affect default chances.
    - Continuous variables like Age, Income, Loan Amount were studied.
    - Class imbalance visualizations noted for documentation.

7. **Dimensionality Reduction**
    - Applied `PCA` for exploratory feature-space visualization.
    - Applied `t-SNE` for non-linear dimensionality reduction to understand class separation.

8. **Next Steps (Upcoming)**
    - Feature Engineering.
    - Data Preprocessing: Encoding, Scaling, Normalization.
    - ML Model Building: Logistic Regression, RandomForest, XGBoost, etc.
    - Evaluation: Accuracy, Precision, Recall, ROC AUC.
    - Model Deployment (optional): Streamlit / Flask.

---

✅ **Status:**  
EDA Completed. Balanced data prepared. Moving to Preprocessing & Modeling phase.



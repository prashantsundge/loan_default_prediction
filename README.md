
# 💡 Loan Default Prediction Project

> Predict loan defaulters using structured data and a full machine learning pipeline.

This project aims to build a predictive system that classifies whether a borrower is likely to default on a loan based on various financial and personal features. The focus is on EDA, data balancing, model building, and scalable code structure.

---

## 🚀 Project Overview

This project covers an end-to-end machine learning pipeline, designed to predict loan defaults using historical loan applicant data.  
From raw data ingestion to EDA, class balancing, feature analysis, and future deployment, this project uses clean and modular code, ready for both research and production.

---

## 🧰 Technologies Used

- 🐍 **Python 3.x**
- 💻 **Jupyter Notebook** for EDA
- 📊 **Pandas, Numpy, Matplotlib, Seaborn** for data manipulation & visualization
- 📦 **Scikit-Learn** for machine learning models and preprocessing
- 🧠 **TSNE, PCA** for dimensionality reduction
- 🌳 **RandomForest** for feature importance analysis
- ⚙️ **OOPs Design** for modular and reusable code
- 💾 **Git & GitHub** for version control

---

## 🎯 Badges

![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-ff69b4)

---




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
---


8. 💡 Data Preprocessing  
   - Applied Encoding for Categorical Features.  
   - Applied Scaling and Standardization for Numerical Features.  
   - Validated data types and consistency post-processing.  
   - Exported the preprocessed dataset for model training.

---

9. 🤖 Model Training  
   - Selected **RandomForest Classifier** as the baseline model.  
   - Trained the model on the balanced and preprocessed dataset.  
   - Achieved initial baseline **Accuracy: 68%**.  
   - Saved the trained model in the `artifacts/` directory.  

---

10. 📊 Model Evaluation  
    - Created a dedicated `model_evaluator.py` for:  
      - Accuracy  
      - Precision  
      - Recall  
      - F1-Score  
      - ROC-AUC curve insights.  
    - Compared the model predictions vs actuals.  
    - Logged all evaluation metrics for reproducibility.  

---

11. 💡 Observations  
    - RandomForest performed decently with an accuracy of ~68%.  
    - Some features required additional engineering for future improvements.  
    - Large model files were compressed (due to GitHub’s file size restrictions) for repository management.

---

12. 🏁 Next Steps  
    - [ ] Hyperparameter Tuning for RandomForest & other models.  
    - [ ] Model Comparison: Logistic Regression, XGBoost, LightGBM.  
    - [ ] Model Deployment (Optional): Streamlit or Flask.  
    - [ ] Write unit tests for modules.  
    - [ ] Finalize Documentation and Flow Diagram.

---

✨ _The project is now transitioning from development to model optimization & deployment phase!_ 🚀


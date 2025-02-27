# Deployment :
---
Huggingface url : `https://huggingface.co/spaces/Radenaz/study_classprob_lol`

# League of Legends Win Prediction

## 📌 Project Overview
This project aims to **predict the winner** of a League of Legends game based on the first 10 minutes of gameplay. Using **machine learning models**, we analyze in-game features like gold difference, kills, and vision control to determine if the **blue team** will win.

## 🛠️ Technologies Used
- **Python** (pandas, numpy, scikit-learn, XGBoost)
- **Machine Learning Models**
  - Logistic Regression
  - KNN, SVM, Decision Tree
  - Random Forest
  - Gradient Boosting (Best Model - 84.1% Accuracy)
  - XGBoost (Work in progress)
- **Streamlit** (for app deployment)
- **Seaborn & Matplotlib** (for data visualization)

## 🏆 Best Performing Model
- **Gradient Boosting Classifier**
- **Accuracy**: 84.1%
- **Key Features**: Gold difference, kills, vision control

## 📊 Exploratory Data Analysis (EDA)
- Analyzed 40+ features from the dataset.
- Key insights:
  - **Gold difference** and **kills** have the strongest correlation with winning.
  - **Vision control** (wards placed/destroyed) plays a significant role.
  - Early-game **objective control** (dragons/heralds) is an indicator of success.

## 🚀 Model Deployment
This project is deployed using **Streamlit**, allowing users to:
1. **Explore Data** 📊 (`eda.py`): Visualize distributions, correlations, and key features.
2. **Make Predictions** 🤖 (`prediction.py`): Enter match statistics to predict win/loss.
3. **Run the Full App** (`app.py`): Combined EDA + Prediction in one interface.

### 🔧 Running the App Locally
```bash
# Clone the repository
git clone https://github.com/yourusername/lol-win-prediction.git
cd lol-win-prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## 🔮 Future Improvements
- **Fine-tune XGBoost** for potentially better accuracy.
- **Add time-series features** for game progression analysis.
- **Improve data pipeline** for live match predictions.


# ForecastForge

**Hybrid Time Series Forecasting Framework**

ForecastForge is a modular and extensible framework designed to tackle complex time series forecasting challenges across diverse domains such as energy consumption, stock prices, traffic flow, and weather patterns. By integrating classical machine learning models, deep learning architectures, and ensemble methods, ForecastForge aims to deliver robust and accurate forecasts.

---

## 🚀 Project Overview

Time series forecasting is pivotal in numerous industries, yet it poses challenges due to data volatility, seasonality, and noise. ForecastForge addresses these challenges by:

- Implementing a variety of forecasting models including LSTM, Transformer, XGBoost, and LiquidML.
- Exploring ensemble techniques to combine predictions from multiple models for improved accuracy.
- Providing a structured approach to model evaluation and comparison across different datasets.

---

## 🧠 Models Implemented

### 1. LSTM (Long Short-Term Memory)
- Captures temporal dependencies in sequential data.
- Applied to energy, stock, traffic, and weather datasets.

### 2. Transformer
- Utilizes self-attention mechanisms for sequence modeling.
- Adapted for time series forecasting tasks.

### 3. XGBoost
- Gradient boosting framework optimized for speed and performance.
- Effective for structured data and time series regression.

### 4. LiquidML
- Custom ensemble approach integrating multiple model predictions.
- Enhances robustness and generalization.

### 5. Ensemble Methods
- Explored various techniques including:
  - Bayesian Model Averaging
  - Blending
  - Median Ensemble
  - Stacked Ensemble
  - Stacked Weighted Voting
  - Voting
  - Weighted Averaging
  - Weighted Voting
  - ✅ **Caruana’s Ensemble Selection** *(Best Performer – used in final evaluation)*

> **Note**: All ensemble methods except Caruana’s are archived under `Deprecated Ensembles`.

---

## 📊 Datasets

- `AEP_hourly_processed.xlsx`: Hourly energy consumption data.
- `Tesla_Stock.xlsx`: Historical stock prices of Tesla.
- `jena_climate.xlsx`: Weather data from the Jena Climate dataset.
- `traffic.xlsx`: Traffic flow data.

*All datasets are preprocessed and stored in the `datasets/` directory.*

---

## 📈 Evaluation Metrics

Model performance is evaluated using **Root Mean Square Error (RMSE)**. Results are stored in respective `RMSE_*.json` files within each model's directory.

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/NamanKr24/ForecastForge.git
   cd ForecastForge
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Jupyter Notebooks**
   ```bash
   jupyter notebook
   ```

Make sure Jupyter Notebook is installed in your environment.

---

## 📌 Key Features

- Modular design facilitating easy addition and evaluation of new models.

- Comprehensive exploration of ensemble methods.

- Organized directory structure for clarity and ease of navigation.

- Preprocessed datasets ready for immediate use.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```

3. Commit your changes:
   ```bash
   git commit -m "Add YourFeature"
   ```

4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```

5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Naman Kumar

📧 Email: namankr24@gmail.com

🔗 GitHub: NamanKr24

---

Crafted with dedication to advance time series forecasting methodologies.

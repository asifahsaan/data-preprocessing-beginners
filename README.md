# Beginner-Friendly Tabular Data Preprocessing

Welcome! This repository is designed to help **beginners** learn how to clean and preprocess tabular data using Python and pandas.

👶 No prior experience required  
📊 Covers both numeric and categorical data  
🔁 Teaches missing value handling, scaling, encoding  
⚙️ Ends with building a reusable sklearn pipeline  

---

## 🔍 What’s Inside

| Notebook                   | Description                                 |
|---------------------------|---------------------------------------------|
| 01_intro_to_dataset       | Load and explore the dataset                |
| 02_missing_values         | Handle missing data in numeric & categorical|
| 03_numeric_features       | Normalize and transform numeric data        |
| 04_categorical_features   | Encode categorical variables                |
| 05_building_pipeline      | Create a reusable pipeline using sklearn    |

---

## 📚 Covered Techniques

This repository demonstrates the following common preprocessing techniques, step by step:

### Handling Missing Values
- Fill missing data using `SimpleImputer` (mean, median, most frequent, constant)

### Scaling and Normalization
- Standardization with `StandardScaler`
- Min-Max scaling with `MinMaxScaler`

### Encoding Categorical Variables
- One-hot encoding with `OneHotEncoder`
- Ordinal encoding with `OrdinalEncoder`

### Binning Numerical Variables
- Discretization using `KBinsDiscretizer` (uniform, quantile, k-means)

### Feature Transformation
- Generate polynomial & interaction features using `PolynomialFeatures`
- Apply custom logic with `FunctionTransformer` or custom classes

### Dimensionality Reduction
- Reduce dimensions using `PCA`
- Visualize clusters with `TSNE`

### Feature Selection
- **Filter Methods**: `SelectKBest` with chi-square or f-tests
- **Wrapper Methods**: Recursive Feature Elimination (RFE)
- **Embedded Methods**: Feature importance via Random Forests, XGBoost, or Lasso (L1)

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/data-preprocessing-beginners.git
cd data-preprocessing-beginners

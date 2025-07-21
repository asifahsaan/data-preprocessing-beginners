# Beginner-Friendly Tabular Data Preprocessing

Welcome! This repository is designed to help **beginners** learn how to clean and preprocess tabular data using Python and pandas.

👶 No prior experience required  
📊 Covers both numeric and categorical data  
🔁 Teaches missing value handling, scaling, encoding  
⚙️ Ends with building a reusable sklearn pipeline  

---

## 🔍 What’s Inside

| Notebook                            | Description                                  |
|------------------------------------|----------------------------------------------|
| 01_intro_to_dataset                | Load and explore the dataset                 |
| 02_handling_missing_values         | Use SimpleImputer and handle missing data    |
| 03_scaling_features                | Standardize and normalize numeric columns    |
| 04_encoding_categorical_variables | One-hot and ordinal encode categorical data  |
| 05_binning_numerical_features      | Discretize numeric data using KBinsDiscretizer |
| 06_polynomial_features             | Create interaction and polynomial terms      |
| 07_custom_transformations          | Apply custom logic via FunctionTransformer   |
| 08_dimensionality_reduction        | Reduce features with PCA and TSNE            |
| 09_feature_selection_filter_methods | Use SelectKBest, chi2, etc.                 |
| 10_feature_selection_wrapper_methods| Use RFE and similar methods                 |
| 11_feature_selection_embedded_methods| Feature importance from tree/L1 models    |
| 12_combining_with_pipeline         | Build full sklearn pipelines                 |

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

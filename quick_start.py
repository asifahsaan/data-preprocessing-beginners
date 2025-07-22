#!/usr/bin/env python3
"""
Quick Start Demo: Complete Data Preprocessing Pipeline
=====================================================

This script demonstrates a complete preprocessing pipeline using the sample dataset.
Run this to see all techniques in action!

Usage: python quick_start.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

def main():
    print("🚀 Data Preprocessing Quick Start Demo")
    print("=" * 50)
    
    # 1. Load Data
    print("\n📊 1. Loading Data...")
    df = pd.read_csv('data/sample_data.csv')
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    
    # 2. Basic Exploration
    print("\n🔍 2. Data Overview...")
    print("\nData Types:")
    print(df.dtypes)
    print(f"\nMissing values per column:")
    print(df.isnull().sum())
    
    # 3. Prepare for ML (predict department based on other features)
    print("\n🎯 3. Preparing for Machine Learning...")
    
    # Separate features and target
    X = df.drop(['id', 'department'], axis=1)
    y = df['department']
    
    # Identify column types
    numeric_features = ['age', 'salary', 'experience', 'performance_score', 
                       'satisfaction_rating', 'num_dependents', 'work_hours_per_week']
    categorical_features = ['education', 'city', 'has_certification', 'gender', 'marital_status']
    date_features = ['join_date']
    
    # 4. Create Preprocessing Pipeline
    print("\n⚙️ 4. Building Preprocessing Pipeline...")
    
    # Numeric pipeline
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Categorical pipeline
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Combine transformers
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        remainder='drop'  # Drop date column for this demo
    )
    
    # 5. Create Complete ML Pipeline
    print("\n🤖 5. Creating Complete ML Pipeline...")
    
    # Encode target variable
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # Create full pipeline
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    # 6. Train and Evaluate
    print("\n📈 6. Training and Evaluation...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
    )
    
    # Train model
    full_pipeline.fit(X_train, y_train)
    
    # Make predictions
    y_pred = full_pipeline.predict(X_test)
    
    # Show results
    print("\n🎯 Classification Results:")
    print(classification_report(y_test, y_pred, 
                               target_names=label_encoder.classes_))
    
    # 7. Feature Importance
    print("\n📊 7. Feature Importance (Top 10):")
    
    # Get feature names after preprocessing
    feature_names = []
    
    # Numeric features
    feature_names.extend(numeric_features)
    
    # Categorical features (one-hot encoded)
    cat_encoder = full_pipeline.named_steps['preprocessor'].named_transformers_['cat']
    cat_feature_names = cat_encoder.named_steps['onehot'].get_feature_names_out(categorical_features)
    feature_names.extend(cat_feature_names)
    
    # Get importance scores
    importances = full_pipeline.named_steps['classifier'].feature_importances_
    
    # Create importance DataFrame
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    print(importance_df.head(10))
    
    print("\n✅ Demo Complete!")
    print("\n📚 Next Steps:")
    print("- Explore individual notebooks for detailed explanations")
    print("- Try different preprocessing techniques")
    print("- Experiment with different algorithms")
    print("- Add your own features!")

if __name__ == "__main__":
    main()
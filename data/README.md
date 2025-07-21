# Dataset Documentation

## Sample Employee Data (`sample_data.csv`)

This dataset contains synthetic employee information designed to demonstrate common data preprocessing challenges.

### Dataset Overview
- **Rows**: 25 employees
- **Columns**: 15 features
- **Purpose**: Educational demonstration of preprocessing techniques

### Column Descriptions

| Column | Data Type | Description | Missing Values |
|--------|-----------|-------------|----------------|
| `id` | Integer | Unique employee identifier | No |
| `age` | Numeric | Employee age in years | Yes (3 missing) |
| `salary` | Numeric | Annual salary in USD | Yes (4 missing) |
| `education` | Categorical | Education level | Yes (3 missing) |
| `experience` | Numeric | Years of work experience | Yes (2 missing) |
| `department` | Categorical | Department name | No |
| `city` | Categorical | Work location | Yes (2 missing) |
| `has_certification` | Binary | Professional certification status | No |
| `performance_score` | Numeric | Performance rating (1-5) | Yes (2 missing) |
| `join_date` | Date | Date of joining company | No |
| `satisfaction_rating` | Ordinal | Job satisfaction (1-5) | Yes (2 missing) |
| `gender` | Categorical | Gender identity | Yes (2 missing) |
| `marital_status` | Categorical | Marital status | No |
| `num_dependents` | Numeric | Number of dependents | No |
| `work_hours_per_week` | Numeric | Average work hours per week | No |

### Data Quality Issues (Intentional for Learning)

1. **Missing Values**: ~12% of data points are missing across various columns
2. **Mixed Data Types**: Combination of numeric, categorical, ordinal, and date columns
3. **Realistic Distributions**: Salary and age follow realistic patterns
4. **Categorical Variety**: Multiple categories with different cardinalities

### Preprocessing Opportunities

This dataset allows you to practice:
- Missing value imputation strategies
- Categorical encoding techniques
- Feature scaling and normalization
- Date/time feature extraction
- Outlier detection and handling
- Feature selection methods
- Pipeline construction

### Data Ethics Note

This is completely synthetic data created for educational purposes. No real employee information is included.
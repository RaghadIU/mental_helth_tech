# Mental Health in Tech - Clustering Analysis

## Project Overview
This project analyzes mental health data in the tech industry to identify patterns among employees and cluster them based on multiple features. The aim is to provide insights for HR teams on work-life balance, stress levels, and mental health treatment tendencies.

## Dataset
- **Source:** Survey data on mental health in the tech workplace.
- **Number of records:** 1,433 employees
- **Number of features (after preprocessing):** 81 columns
- **Preprocessing performed:**
  - Handling missing values
  - Encoding categorical variables
  - Creating new features:
    - `work_life_balance_score`
    - `stress_index`

## Data Preprocessing
1. **Handling Missing Values:**  
   Missing values were either filled using median values for numerical columns or handled appropriately for categorical features.

2. **Encoding Categorical Features:**  
   Categorical responses such as 'Yes', 'No', 'Maybe', and 'Don't know' were encoded numerically (e.g., Yes = 1, No = 0).

3. **Feature Engineering:**  
   - `work_life_balance_score`: Average of responses related to employer support and work-life balance.  
   - `stress_index`: Combined metric from stress-related survey questions.

## Clustering
- **Method:** K-Means clustering
- **Number of clusters:** 4
- **Columns used:** All numeric features
- **Silhouette Score:** 0.29 (indicates moderate cluster separation)
- **Cluster Assignment:** Added as `Cluster` column in the processed dataset

### Example of Cluster Summary
| Cluster | Number of Employees | Key Insights |
|---------|------------------|--------------|
| 0       | 589              | Employees with moderate work-life balance, mostly younger age group |
| 1       | 381              | Employees with high employer support, moderate stress levels |
| 2       | 370              | Older employees, lower work-life balance score |
| 3       | 91               | Outlier group, extreme values in some features (e.g., very high/low age or company size) |

> Full detailed statistics are available in `reports/cluster_profiles.md`.

## Visualizations
- **Scatter Plots:** Age vs. Tech Company Employment & Mental Health Treatment
- **Heatmap:** Correlation among numeric features
- **Radar Charts:** Comparison of clusters on selected key features

*(Visualizations generated programmatically using the `src/viz` module.)*

## Results and Insights
- Identified 4 distinct clusters of employees based on mental health and workplace features.
- Work-life balance and stress levels vary significantly between clusters.
- Cluster profiles can help HR teams target interventions and mental health programs more effectively.

## How to Reproduce
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt 

3. Run preprocessing and feature engineering notebooks
4. Run clustering and visualization notebooks
5. Check outputs in data/processed/ and reports/

## File Structure
mental-health-tech/
│
├─ data/
│  ├─ raw/
│  ├─ processed/  # contains df_features and cluster CSV
│
├─ notebooks/     # Jupyter notebooks for preprocessing, analysis, and visualization
├─ reports/       # cluster_profiles.md and generated charts
├─ src/           # Python modules for preprocessing, feature engineering, clustering, visualization
├─ README.md

## Conclusion

This analysis provides a comprehensive overview of mental health trends among tech employees. By using clustering, HR teams can better understand employee needs and implement tailored mental health programs.
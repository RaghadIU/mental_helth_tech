
## Project Overview
This project analyzes mental health data in the technology sector to identify patterns among employees and cluster them based on demographic, work environment, and mental health-related features. The aim is to provide HR teams with actionable insights on work-life balance, stress levels, mental health treatment, and employee support needs.

## Dataset
- **Source:** OSMI Mental Health in Tech Survey (2016)
- **Number of records:** 1,433 employees
- **Number of features (after preprocessing):** 81 columns
- **Preprocessing performed:**
  - Handling missing values
  - Encoding categorical variables
  - Feature engineering:
    - `work_life_balance_score`: average of employer support and work-life balance responses
    - `stress_index`: combined score from stress-related questions

## Data Preprocessing Steps
1. **Handling Missing Values:**  
   - Numerical columns: filled using median values  
   - Categorical columns: imputed with "Not provided" or "No answer"

2. **Encoding Categorical Features:**  
   - Categorical responses such as 'Yes', 'No', 'Maybe', and 'Don't know' were encoded numerically  
   - Gender normalized into: Male, Female, Other, Not specified  
   - Country names standardized (e.g., US, USA, United States → United States)

3. **Feature Engineering:**  
   - `work_life_balance_score`: average of employer support and work-life balance-related survey items  
   - `stress_index`: combined metric from stress-related survey questions

4. **Scaling:**  
   - StandardScaler applied to all numeric features for uniform weighting

## Dimensionality Reduction
- **Method:** Principal Component Analysis (PCA)  
- **Purpose:** Reduce high-dimensional dataset into 2 principal components for visualization and clustering  
- **Variance explained:** ~31% (PC1: 17.6%, PC2: 13.6%)  
- **Visualization:** 2D scatter plots of the first two components

## Clustering Analysis
- **Method:** K-Means clustering  
- **Number of clusters:** 3 (based on Elbow Method)  
- **Columns used:** all scaled numeric features  
- **Cluster sizes:**
  - Cluster 0: 251 employees  
  - Cluster 1: 589 employees  
  - Cluster 2: 593 employees  
- **Silhouette Score:** 0.29 (moderate separation)  
- **Cluster Assignment:** Added as `Cluster` column in the processed dataset

## Cluster Profiling
| Cluster | Size | Demographics | Work Environment | Mental Health Perceptions | Behavioral Patterns / HR Implications |
|---------|------|--------------|-----------------|---------------------------|---------------------------------------|
| 0       | 251  | Ages 25–35, slightly more male | Moderate working hours (40–45 hrs/week), medium employer support | Comfortable discussing mental health with peers, less so with supervisors | Average stress, moderate openness to treatment; suitable for peer-support and awareness programs |
| 1       | 589  | Ages 28–40, balanced gender | Structured employer-provided mental health resources, clear communication | High comfort discussing mental health with peers and supervisors | Low stress, high engagement; HR programs effective and can be refined/expanded |
| 2       | 593  | Ages 35–50, senior or demanding roles | Longer weekly hours, lower perceived employer support | Lower openness to discuss mental health due to stigma and role pressure | Elevated stress, higher burnout risk; HR should provide flexible schedules, counseling, and targeted awareness |

## Visualizations
- **Scatter Plots:** PCA components, Age vs. Mental Health Treatment  
- **Heatmaps:** Correlation between numeric features  
- **Radar Charts:** Cluster comparison on key metrics (stress_index, work_life_balance_score, etc.)  

All visualizations are generated programmatically and saved in `reports/`.


## How to Reproduce
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt 

3. Run preprocessing and feature engineering notebooks
4. Run clustering and visualization notebooks
5. Check outputs in data/processed/ and reports/


## Conclusion

This analysis provides a comprehensive overview of mental health trends among tech employees. By using clustering, HR teams can better understand employee needs and implement tailored mental health programs.
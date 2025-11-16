---
title: "Classification of Obesity Levels using PCA and Random Forest"
excerpt: "In this project, we use PCA and Random Forest classifier to classify the obesity levels based on their physical measurements and lifestyle factor."
collection: portfolio
---

## Introduction

Obesity is a growing public health issue, particularly in developed countries where sedentary lifestyles and poor dietary habits are prevalent. According to the National Institute of Diabetes and Digestive and Kidney Diseases, 30.7% of adults are overweight, 42.4% have obesity, and 9.2% suffer from severe obesity. These statistics underline the urgency to develop robust predictive models that can help identify individuals at risk early on. In this study, we explore whether machine learning algorithms, specifically a Random Forest classifier enhanced with Principal Component Analysis (PCA), can accurately predict obesity levels based on a combination of physical measurements and lifestyle factors.

The dataset used for this study is the Estimation of Obesity Levels Based On Eating Habits and Physical Condition from the UCI Machine Learning Repository. The dataset provides features including demographic information, lifestyle habits, and physical measurements that have been shown to correlate with obesity. Our objective is to assess the effectiveness of PCA in reducing feature dimensionality and enhancing the predictive performance of the Random Forest classifier.

## Related Work

In the research of Kabongo et al. (2022), they used several machine learning algorithms, inclding k-nearest neighbors (KNN), support vector machine (SVM), ridge classifier, logistic regression, and random forest classifier, for this classification task. After comparison, they found that random forest classifier has the highest accuracy score, but they chose SVM as their final model because of other factors such as cost effectiveness.

Based on their research, our approach use random forest classifier, while integrating PCA to investigate if reducing the feature space can improve model generalization. We hypothesized that PCA might streamline the feature set and possibly uncover latent structures in the data that are beneficial for classification.

## Method

The dataset comprises 16 original features including demographic data (such as age and gender), physical measurements (height, weight), and lifestyle factors (e.g., physical activity, eating habits). Some of these features are inherently categorical, while others are continuous.

### Data Cleaning and Transformation

- Missing Value Analysis: A thorough inspection indicates that the dataset did not contain any missing values, which simplified our preprocessing pipeline.
- Normalization: Continuous features were normalized to ensure that each feature contributed equally to the analysis.
- Categorical Encoding: We applied one-hot encoding to categorical variables, expanding the feature space from 16 to 23 columns. Although this increased the number of features, it also ensured that the model could handle non-numeric data appropriately.
- Feature Correlation: A correlation matrix was generated to identify relationships between features. The only strong correlation was observed between height and weight, which is expected due to their physical correlation.

![PCA and Random Forest Workflow](/images/corr_matrix.png)

### Dimensionality Reduction with PCA

Given that high dimensionality can sometimes lead to overfitting and increased computational cost, PCA was applied to the dataset. Although the original feature set is relatively small, we anticipated that PCA might still reveal combinations of features that capture the most variance in the data. Cross-validation indicated that retaining 12 principal components was optimal for our Random Forest model.

![Performance of different number of Principal Component](/images/pca_accuracy.png)

### Random Forest Classifier

The Random Forest classifier was chosen due to its robustness and ability to handle non-linear relationships within the data. Two separate models were trained:

- Model without PCA: This model used the full set of 23 features.
- Model with PCA: This model used the 12 principal components extracted via PCA.

### Hyperparameter Tuning

GridSearchCV was employed to optimize key hyperparameters of the Random Forest classifier. The optimal settings were found to be:

- Maximum depth: 30
- Number of estimators: 300
- Minimum sample split: 2

## Result

The results for both models were as follows:

- Original Data (without PCA):
    - Train Accuracy: 1.0
    - Mean Validation Accuracy: 0.9425
    - Test Accuracy: 0.9479
![Original Classification Report](/images/original_class.png)
![Original Confusion Matrix](/images/original_matrix.png)

- PCA-Transformed Data:
    - Train Accuracy: 1.0
    - Mean Validation Accuracy: 0.8235
    - Test Accuracy: 0.8298

![PCA transformed Classification Report](/images/pca_class.png)
![PCA transformed Confusion Matrix](/images/pca_matrix.png)

The model using the original feature set outperformed the PCA-transformed model. These findings suggest that PCA may not be as beneficial when the original dataset has a limited number of features.

## Discussion

The comparison indicates that PCA did not enhance performance for this particular task. With only 16 original features, the dataset did not benefit substantially from dimensionality reduction. Moreover, PCA transformed features into linear combinations, which may lack interpretability and real-world meaning—an important consideration for medical and health-related applications.

### Limitation and Consideration

One of the limitation is that although PCA can sometimes reduce noise, the loss of feature interpretability poses challenges, especially in health-related research where understanding the influence of individual factors is crucial. In addition, while Random Forests are robust, the use of PCA in a dataset with already few features might oversimplify the model and eliminate valuable nuances in the data. Last but not least, given that the training accuracy for both models is perfect (1.0), there is a risk of overfitting. Even though cross-validation was applied, further work is needed to ensure the model generalizes well to completely unseen data.

### Future Work

Future work could involve exploring additional models like neural networks or ensemble methods to capture more complex patterns beyond what Random Forests can detect. Further feature engineering, including alternative encoding methods and interaction terms, may reveal hidden relationships that enhance performance. Moreover, validating the model on diverse external datasets and integrating explainability techniques such as SHAP would help ensure robustness and improve the interpretability of the predictions.

## Conclusion

In summary, our study demonstrates that while Random Forest classifiers can achieve high accuracy in predicting obesity levels based on lifestyle and physical factors, the application of PCA did not yield performance improvements for a dataset with limited original features. This insight emphasizes the importance of selecting appropriate preprocessing techniques tailored to the dataset's characteristics. Future research should focus on exploring alternative models, advanced feature engineering techniques, and methods for model interpretability to further enhance predictive performance and utility in real-world scenarios.

## Reference

1. Estimation of Obesity Levels Based On Eating Habits and Physical Condition  [Dataset]. (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5H31Z.
2. Kabongo, J., Clem’s, M. L., Manianfu, P., & Louison, D. K. (2022). Five machine learning supervised algorithms for the analysis and the prediction of obesity. In International Journal of Innovative Science and Research Technology (Vol. 7, Issue 12, pp. 1956–1957). https://ijisrt.com/assets/upload/files/IJISRT22DEC1619.pdf
3. Overweight & Obesity Statistics. (2024, October 18). National Institute of Diabetes and Digestive and Kidney Diseases. https://www.niddk.nih.gov/health-information/health-statistics/overweight-obesity
Palechor, F. M., & De La Hoz Manotas, A. (2019). Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico. Data in Brief, 25, 104344. https://doi.org/10.1016/j.dib.2019.104344

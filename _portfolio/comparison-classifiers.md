---
title: "Evaluating Classifier Performance Across Datasets and Partition Strategies"
excerpt: "Short description of portfolio item number 2 <br/><img src='/images/500x300.png'>"
collection: portfolio
---

## Abstract

This study evaluates the performance of Random Forest, Logistic Regression, and Support Vector Machine classifiers on UCI datasets (Adult, Wine Quality, and Breast Cancer) under varying train-test splits. Random Forest consistently achieved high accuracy, Logistic Regression excelled with smaller training sizes, and Support Vector Machine performed best with sufficient data. Partition size influenced results, benefiting larger datasets like Wine Quality but causing overfitting in the small Breast Cancer dataset. These findings highlight the importance of aligning models and data strategies with dataset characteristics for optimal performance.

## 1 Introduction

Machine learning classification is integral to applications such as medical diagnosis and financial forecasting. Among its tasks, two-class classification is particularly foundational. The success of a classification model relies on its ability to generalize across diverse datasets and perform effectively under varying hyperparameter configurations and training data proportions.

This study investigates the performance of three widely used classifiers—Random Forest, Logistic Regression, and Support Vector Machine—on datasets with varying characteristics from the UCI Machine Learning Repository: Adult, Wine Quality, and Breast Cancer. Inspired by the work of Caruana and Niculescu-Mizil [1], each classifier was evaluated under multiple train-test partition schemes (20/80, 50/50, and 80/20) and fine-tuned using GridSearchCV to optimize hyperparameters. Performance metrics, including training, validation, and test accuracy, were analyzed to compare classifier strengths and weaknesses.

By systematically examining the effects of partition size, dataset characteristics, and model tuning, this research provides insights into the behavior of different classifiers and highlights practical strategies for optimizing their performance. The findings aim to guide model selection and deployment in diverse real-world scenarios while reinforcing the importance of systematic experimentation in machine learning.

## 2 Methods

### 2.1 Datasets

This project uses three datasets from UCI Machine Learning Repository:

**Adult**: The Adult dataset is sourced from the 1994 U.S. Census and comprises 48,842 instances, each described by 14 demographic or economic attributes [2]. The primary objective is to predict whether an individual's annual income exceeds \$50,000 based on these demographic and economic factors.

**Wine Quality**: The Wine Quality dataset comprises two datasets related to red and white variants of Portuguese "Vinho Verde" wine [3]. The dataset includes 6,497 instances and 11 physicochemical attributes. The primary objective is to model wine quality based on these physicochemical tests. Original labels (quality) range from 3 to 9 (integer), but for convenience, labels were transformed into 1 (quality > 5; good) and 0 (quality <= 5; bad).

**Breast Cancer**: The Breast Cancer dataset comprises 286 instances, each characterized by 9 attributes, including age, menopause status, tumor size, and degree of malignancy [4]. The primary objective is to classify cases into 'no-recurrence-events' or 'recurrence-events' based on these attributes. Notably, the dataset contains missing values in certain fields.

### 2.2 Data Preprocessing and Feature Engineering

Preprocessing and feature transformations were tailored to the requirements of each dataset to ensure compatibility with the selected classifiers.

#### Adult

- Rows with missing values were removed.
- The variable *education* was dropped as it is redundant with *education-num*.
- Categorical variables were transformed using one-hot encoding.

#### Wine Quality

- Labels were simplified into binary categories to represent "good" (1; quality > 5) and "bad" (0; quality <= 5) wine quality.
- item No missing values or categorical data were reported, reducing preprocessing overhead.

#### Breast Cancer

- Rows with missing values were excluded from the analysis.
- Binary features and labels were converted into numerical representations (0 and 1).
- Ordinal encoding was applied to attributes like *age*, *tumor-size, and *inv-nodes*.
- Categorical variables such as *menopause*, *breast*, and *breast-quad* were transformed using one-hot encoding.

### 2.3 Classifiers

The project evaluates three machine learning models implemented using the Scikit-learn library:

**Random Forest Classifier (RF)**: A robust ensemble method that constructs multiple decision trees during training and outputs the mode of their predictions for classification tasks. The parameter of max_features was fine-tuned using cross-validation.

**Logistic Regression Classifier (LR)**: A linear model that predicts probabilities and classifies data by applying a logistic function to a linear combination of input characteristics. The L2 penalty regularization technique was employed to mitigate overfitting. The C parameter was chosen among the factors of 10 from 0.001 to 1000 using cross-validation.

**Support Vector Machine (SVM)**: A powerful algorithm that seeks an optimal hyperplane to separate data points in feature space. It uses the RBF kernel, and the C parameter was chosen among 0.01, 0.1, 1, 10, 100 using cross-validation.

### 2.4 Hyperparameters Tuning

Hyperparameter optimization was performed using **GridSearchCV**, a method provided by Scikit-learn that systematically tests multiple combinations of hyperparameters to identify the best configuration for each classifier. This ensures that each model operates at its optimal settings for the given dataset.

For each classifier, a range of hyperparameter values was defined based on common practices and the specific needs of the datasets. GridSearchCV used k-fold cross-validation (with k=5) to evaluate each parameter combination. The metric used for selecting the best model primarily focused on accuracy.

### 2.5 Performance Metric

The primary performance metric for this project was accuracy, which measures the proportion of correctly classified instances. Accuracy was chosen for its simplicity and effectiveness, especially since the datasets were either balanced or preprocessed to minimize class imbalances. It provided a straightforward way to compare model performance across datasets and classifiers.

## 3 Experiment

### 3.1 Experimental Setup

The experiment involved training three classifiers on three datasets using three train-test data partitions: 20/80, 50/50, and 80/20. Hyperparameters for each combination were tuned beforehand and stored in a JSON file to avoid redundant computations during training. (See Table \ref{tab:hyperparameters} in Appendix for the hyperparameters of each combination and their corresponding mean validation scores)

For each combination of classifier, dataset, and data partition, the model was trained three times using the corresponding pre-tuned hyperparameters. This repetition ensured that results were not influenced by extreme performance variations. The train accuracy, test accuracy, and mean cross-validation accuracy from these three trials were averaged and recorded in a result dataframe.

The final result dataframe contained 81 rows, representing the 3 classifiers × 3 datasets × 3 data partitions (20/80, 50/50, 80/20) × 3 accuracy metrics. This comprehensive dataset enabled grouped analyses to compare performance across classifiers, training data sizes, and datasets, providing detailed insights into the strengths and weaknesses of each model.

### 3.2 Results

The following results focus on the test accuracy. The full table of train, validation, and test accuracy are presented in the Table \ref{tab:full-scores} in Appendix.

#### 3.2.1 Comparison for different algorithms

After training, the performance of the classifiers varied across datasets. For the Wine Quality and Adult datasets, the Random Forest Classifier consistently achieved the highest accuracy regardless of the partition size. However, for the Breast Cancer dataset, the performance of each classifier was more influenced by the partition size:

- In the 20/80 split, the Support Vector Machine (SVM) slightly outperformed the other classifiers.
- In the 50/50 split, the Random Forest Classifier demonstrated the best accuracy.
- In the 80/20 split, the SVM showed a significant improvement, outperforming the other two classifiers.

These results suggest that the Random Forest Classifier is generally robust across different datasets, while Logistic Regression and SVM are more sensitive to the characteristics of the dataset and the size of the training set. The trends are visualized in Figure \ref{fig:algorithm-comparison}.
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{image_1.png}
    \caption{Accuracy comparison across classifiers for different datasets and partition sizes.}
    \label{fig:algorithm-comparison}
\end{figure}

#### 3.2.2 Comparison on different partitions

The effect of train-test partition size on classifier performance varied by dataset:

- For the Wine Quality dataset, Random Forest Classifier and SVM show steady improvement in accuracy as the training size increases, leveraging the additional data effectively, while Logistic Regression maintains stable accuracy across all training sizes.
- For the Adult dataset, the accuracy of the classifiers remained relatively stable across all partition sizes, indicating that the classifiers quickly reached their maximum performance even with smaller training sets.
- For the Breast Cancer dataset, the accuracy of Logistic Regression model shows a slight decrease in accuracy with larger training sizes. The accuracy of random forest increases a little at 50/50 split but decreases a lot at 80/80 split. Random Forest Classifier performs best at the 50/50 split but drops significantly at the 80/20 split, and SVM improves consistently with more training data, achieving its highest accuracy at the 80/20 split.

The relationship between partition sizes and accuracy is summarized in Figure \ref{fig:partition-comparison}.

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{image_2.png}
    \caption{Accuracy trends across partition sizes for different datasets.}
    \label{fig:partition-comparison}
\end{figure}

\subsection{Analysis}
The results highlight key patterns in classifier performance across datasets and partition sizes, providing insights into the strengths and limitations of each algorithm and how dataset characteristics impact model behavior.

\subsubsection{Performance Across Algorithms}
The \textbf{Random Forest Classifier} consistently achieved high accuracy for the \textbf{Wine Quality} and \textbf{Adult} datasets across all partition sizes. This result demonstrates its robustness and ability to capture complex patterns in the data. The ensemble nature of Random Forest likely allows it to generalize well, even with varying training set sizes.

In contrast, \textbf{Logistic Regression} exhibited relatively stable performance for all dataset across all partition sizes, emphasizing its simplicity and effectiveness in datasets with straightforward features. For the Breast Cancer dataset, accuracy slightly declined with larger training sizes, likely due to its reliance on linear decision boundaries and susceptibility to overfitting in small datasets.

\textbf{Support Vector Machine (SVM)} showed consistent improvements in accuracy with increased training sizes for the Wine Quality and Breast Cancer datasets. It achieved its best performance in the \textbf{Breast Cancer} dataset at the largest training size \textbf{(80/20 split)}, underscoring its need for sufficient data to optimize the hyperplane effectively. For the Adult dataset, SVM performance remained stable, comparable to Random Forest and Logistic Regression.

\subsubsection{Impact of Partition Size}
Partition size had a varied effect on classifier performance depending on the dataset:
\begin{itemize}
    \item For the \textbf{Wine Quality} dataset, the \textbf{Random Forest Classifier} and \textbf{SVM} demonstrated consistent accuracy improvements with larger training sizes, suggesting the dataset's complexity benefits from additional training data. Logistic Regression maintained stable accuracy across partitions, indicating limited gains from more training data due to its linear nature.
    \item For the \textbf{Adult} dataset, accuracy remained stable regardless of the partition size. This indicates that the dataset may already provide sufficient information in smaller training sets for the classifiers to reach their optimal performance. It also suggests that the features in the dataset are straightforward and not overly complex.
    \item For the \textbf{Breast Cancer} dataset, the Logistic Regression model's accuracy slightly decreased with larger training sizes, potentially due to overfitting caused by the small dataset size. \textbf{Random Forest} achieved a peak accuracy at the 50/50 split but saw a notable decline at the 80/20 split, likely due to reduced test data and overfitting. \textbf{SVM} showed consistent improvement, achieving the highest accuracy at the largest training size (80/20 split), demonstrating its capacity to handle smaller, high-dimensional datasets effectively when enough training data is available.
\end{itemize}

\subsubsection{Comparative Insights}

The \textbf{Adult} dataset showed that stable performance can be achieved even with smaller training sizes, making it ideal for tasks with limited data. The \textbf{Breast Cancer} dataset highlighted the challenges of working with small datasets, where overfitting and sampling issues can obscure model performance. For the \textbf{Wine Quality} dataset, Random Forest and SVM demonstrated the benefit of additional training data, while Logistic Regression reached its performance ceiling early, reflecting the varying capacities of these classifiers to leverage complex datasets.

## Conclusion

This study evaluated the performance of three machine learning classifiers—Random Forest, Logistic Regression, and Support Vector Machine—across three datasets (Adult, Wine Quality, and Breast Cancer) under varying train-test splits. The results demonstrate that Random Forest consistently achieved the highest accuracy for most datasets, showcasing its robustness and ability to handle complex patterns effectively. Logistic Regression, while stable, showed limitations in leveraging additional training data, particularly for more complex datasets. Support Vector Machine performed best when provided with sufficient training data, particularly excelling in smaller, high-dimensional datasets like Breast Cancer.

Partition size significantly influenced classifier performance, with Random Forest and SVM benefiting from larger training sizes in the Wine Quality dataset, while Logistic Regression exhibited minimal variation. For the Adult dataset, all classifiers achieved stable accuracy regardless of partition size, reflecting its simplicity. However, the Breast Cancer dataset revealed the challenges of small datasets, with overfitting affecting Random Forest and Logistic Regression, while SVM excelled with larger training sizes.

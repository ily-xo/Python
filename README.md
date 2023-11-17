# Python Portfolio
- Welcome to my Python Repository, including some highlights from my [Data 8](http://www.data8.org/) course, Computational Models of Cognition [CogSci 131](https://classes.berkeley.edu/content/2020-spring-cogsci-131-001-lec-001) course, and more projects. I am looking forward to expanding my breadth of knowledge within the data science space. 

Some project highlights:
- Implemented a binary classification model to predict "Crime Severity" using Python and machine learning libraries, achieving a final accuracy of ~94%. 
- Conducted data preprocessing tasks, including dataset cleaning, scaling of numeric values using MinMaxScaler, and encoding of categorical variables for effective model training.
- Applied feature engineering techniques to enhance model performance, such as renaming columns, handling missing data, and dropping irrelevant features.
- Addressed class imbalance using the Synthetic Minority Over-sampling Technique (SMOTE) to improve model generalization on minority classes.
- Explored and trained two popular classification algorithms, Logistic Regression and XGBoost, on both the original and resampled datasets.
Utilized feature selection techniques, including SelectKBest with chi2, to reduce the dimensionality of the dataset and enhance model efficiency.
- Developed a streamlined workflow for hyperparameter tuning using RandomizedSearchCV, achieving optimal parameters for Logistic Regression (C=0.37, penalty='l2', solver='sag') and XGBoost (subsample=0.075, n_estimators=200, max_depth=10, learning_rate=0.087, colsample_bytree=0.971).
- Implemented RandomizedSearchCV, a randomized search cross-validation technique, to explore various hyperparameter combinations efficiently.

Optimized Parameters for Logistic Regression:

Applied RandomizedSearchCV to the Logistic Regression model, systematically exploring different combinations of hyperparameters.
Successfully identified the optimal hyperparameters for Logistic Regression, resulting in improved model accuracy and generalization.

Optimized Parameters for XGBoost Classifier:

Utilized RandomizedSearchCV to fine-tune the hyperparameters of the XGBoost classification model.
Conducted a thorough search across the hyperparameter space, considering factors such as subsample, number of estimators, maximum depth, learning rate, and colsample_bytree.

- Created visualizations, including bar plots and confusion matrices, to interpret and communicate model performance effectively.
- Collaborated with cross-functional teams to integrate machine learning models into the decision-making process, providing actionable insights.
- Documented and presented findings, methodologies, and results in a clear and concise manner, facilitating team understanding and decision-making.

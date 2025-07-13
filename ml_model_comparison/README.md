# Machine Learning Model Comparison

This project implements three different machine learning models to compare their accuracy scores and classification reports on a dataset related to air quality index (AQI) prediction.

## Project Structure

```
ml-model-comparison
├── src
│   ├── data_preprocessing.py        # Functions for loading and preprocessing the dataset
│   ├── model_random_forest.py       # Implementation of the Random Forest model
│   ├── model_svm.py                 # Implementation of the Support Vector Machine model
│   ├── model_logistic_regression.py  # Implementation of the Logistic Regression model
│   ├── evaluate_models.py            # Functions to evaluate the models
│   └── utils.py                      # Utility functions for visualization and formatting
├── requirements.txt                  # List of dependencies
└── README.md                         # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ml-model-comparison
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preprocessing**: Use the `load_and_preprocess_data()` function from `data_preprocessing.py` to load and preprocess the dataset.

2. **Model Training**: 
   - For Random Forest, use the `RandomForestModel` class from `model_random_forest.py`.
   - For Support Vector Machine, use the `SVMModel` class from `model_svm.py`.
   - For Logistic Regression, use the `LogisticRegressionModel` class from `model_logistic_regression.py`.

3. **Model Evaluation**: Use the `evaluate_model()` function from `evaluate_models.py` to get accuracy scores and classification reports for each model.

4. **Visualization**: Use the `plot_results(results)` function from `utils.py` to visualize the performance of the models.

## Models Implemented

- **Random Forest**: An ensemble learning method that constructs multiple decision trees and outputs the mode of their predictions.
- **Support Vector Machine (SVM)**: A supervised learning model that finds the hyperplane that best separates the classes in the feature space.
- **Logistic Regression**: A statistical model that uses a logistic function to model a binary dependent variable.

## License

This project is licensed under the MIT License.
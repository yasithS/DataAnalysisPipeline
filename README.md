creating a virtual en
# ML Data Processing Pipeline

A streamlined machine learning pipeline for data loading, cleaning, feature engineering, and model evaluation.

## Project Overview

This project implements a modular machine learning pipeline designed to:
1. Load data from CSV files
2. Clean and preprocess the data
3. Engineer features for model training
4. Train and evaluate a RandomForest classifier

## Project Structure

```
├── data/               # Directory for your dataset files
├── src/
│   ├── data_loader.py      # Loading data from CSV
│   ├── data_cleaner.py     # Handling missing values and outliers
│   ├── feature_engineer.py # Feature creation and preprocessing
│   ├── model_evaluator.py  # Model training and evaluation
│   └── main.py             # Main application logic
├── .gitignore          # Git ignore file
├── .gitattributes      # Git attributes file
├── LICENSE             # MIT License
├── README.md           # This readme file
└── requirements.txt    # Project dependencies
```

## Installation

### Setting up a virtual environment

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Installing dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Place your CSV dataset in the `data/` directory
2. Update the `file_path` and `target_column` variables in `main.py` to match your dataset
3. Run the pipeline:

```bash
python -m src.main
```

## Features

- **Data Loading**: Flexible CSV data loading with error handling
- **Data Cleaning**: 
  - Missing value imputation
  - Outlier removal using z-score method
- **Feature Engineering**:
  - Automated feature scaling
  - Train/test splitting
- **Model Evaluation**: RandomForest classifier with accuracy reporting

## Customization

- To use a different model, modify the `ModelEvaluator` class in `model_evaluator.py`
- To add additional preprocessing steps, extend the `DataCleaner` class
- To create more complex features, enhance the `FeatureEngineer` class

## Dependencies

- pandas 2.0.3
- scikit-learn 1.3.0
- numpy 1.25.2

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Yasith Gunawardhana
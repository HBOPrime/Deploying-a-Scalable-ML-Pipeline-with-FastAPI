# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model created by John Gilmore. The model type is Random Forest from scikit-learn.

## Intended Use
The intended use for the model is to predict salary information from US Census data.

## Training Data
The dataset is US Census data.

## Evaluation Data
The evaluation data is 20% of the whole data set randomly segmented.

## Metrics
The metrics used to evalute the data. The results for the tests are:
Precision: 0.7633 | Recall: 0.6404 | F1: 0.6964

## Ethical Considerations
The data comes from population data which may have personal information. 

## Caveats and Recommendations
Recommenation: 
    - Retrain data upon new census information being released (yearly).
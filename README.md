## Binary Classification

### Membres :

- Alexandre GIRAUD
- Clément ANDRÉ
- Patrick NJEUKMAN

### Data :

Data : https://archive.ics.uci.edu/ml/datasets/banknote+authentication

Data : https://www.kaggle.com/mansoordaku/ckdisease


### Consignes :

1. Import the dataset
2. Clean the data, perform pre-processing
    I Replace missing values by average or median values
    I Center and normalize the data
3. Split the dataset
    I Split between training set and test set
    I Split the training set for cross-validation
4. Train the model (including feature selection)
5. Validate the model

### Indications


1. You should first clean the dataset (handle missing values and categorical values)

2. You may implement feature selection: bruteforce, by looking at correlations, from an ACP (for classification), by using Ridge regression (for linear regression), etc.

3. Do not forget to save a part of your dataset as your test set. It will not be used for training, but only to assess the quality of your method.
    
4. You may also use cross-validation to adjust the method (choice of the kernel, feature selection, etc.)

5. You should automate your process as much as possible

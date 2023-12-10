# LHL_final_project


## Target Audience

Operations department of the Food Delivery Company (India). 
My intent is to provide a technical framework and references that a Data scientist would know, but to contextualize them in a business context, so the organization can leverage the information and implement productive changes.


## Deliverable: Proof of Concept for future modelling

1. A Model of the given data as a proof of the model.

2. A Production framework to:
    1. Observe more data features to provide "better data" for the model (Research)
    2. Improve existing data features (Analysis)
    3. Ingest, Clean, and Weighted Feature importance into the model to help its predicting power (Visualization)

3. What things need to change in operations, such as procedures and guidelines, to improve the delivery time.


### This is what I am trying to figure out (, so what? How does this affec the business)

1. Which features are most important in determining the delivery time of the given model
    1. So that the business can focus on improving or accounting for those features. 
2. What an end-to-end production could be using tools.
    1. So that there is a cost efficient method (free - financial impact) to produce further results
    2. So that there is a historical reference based on the date where it can be 
3. What things can be changed physically to help the delivery time, such as method of transportation, 
    1. 


### This is what I hope to determine

1. These features must be emphasized, weighted, or changed to support the model, and to allow for confirmation stages 
2. The Production line to:
    1. Ingestation parameters, 
    2. automated cleaning techniques, 
    3. automated visualizations to confirm insights
    4. automated hypertuning (grid search), 
    5. automated feature selection (importance)
3. To see if further insights regarding the reporting can be gained from more data, and if the recommended guidelines and procedures can be validated once more data is ingested into the model (monitoring change)


## Process

### Staging the Data

#### Data Transformation

1. Transformations to the proper data types
2. Categorical features to Ordinal or "One-Hot encoding" features

#### Data Partitioning
1. Based on the city of delivery, create multiple dataframes where each will modelled seperately (assuming there is enough data for each).
2. Creating a dataframe with each city as one-hot encoding, so all data is together for a model.

#### Data Cleaning
1. Automated cleaning of outliers for quantitative variables
2. Rationally determining the reliability of the feature and its ability to support (include) or skew (ommit) the model

#### Feature Engineering
1. Through Data Visualization, determine the relationship (linear, exponential, etc.) between the dependent feature (time taken in minutes) to the independent feautres and create new features as needed.
2. Try to combine features logically to ingest into the model.

#### Determine a Model
1. Exploring linear regression, Support Vector Machines, Decision Trees, Random Forest, etc.  
2. Using different types of hypertuining and Ensemble Techniques


### Model the Data


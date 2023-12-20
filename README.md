# LHL_final_project

Does not have to be big, just has to have a good scope. - only 5-6 slides.  Title - agenda - background, overall solution intended, thried these, this is what I did and here is the result - talk about "why" you made changes improve the predictatbility (in support of the business need/commanders intent), here's what is needeed for the production level, in the future, questions.  You have all the stuff, just get the slide deck together.  Completeness and Accuracy - this what you are looking for - the cleaner the data... trying to create models that are more finite.  Using multiple models to pin point the data.  They care how you think - how does Kieran think, how can he solve our business problems.  80% solution.

## Target Audience

Operations department of the Food Delivery Company (India). 
My intent is to provide a technical framework and references that a Data scientist would know, but to contextualize them in a business context, so the organization can leverage the information and implement productive changes.


## Deliverable: Proof of Concept for future modelling

1. A Model of the given data as a proof of a predictive model.

2. A Production framework to:
    1. Observe more data features to provide "better data" for the model (Research) - preventative maintenance on older vehicle.  
    2. Improve existing data features (Analysis) *KPI* Analysis 
    3. Ingest, Clean, and Weighted KPI importance into the model to help its predicting power (Visualization)

3. What things need to change in operations, such as procedures and guidelines, to improve the delivery time.  Using a truck that has a battery that can charge vehicle.  Chatbot to communicate with the customer, only 1 phone number, the customer gets all of the information - timing.  Text ratings and quick response.  Measuring clicking the link to see where the delivery is.  Measureing the customer's experience.  Adding texting as measuring customer experience.  Telling when the food will be delivered via text - delays and when they are close.  This is not a skip the dishes.  Assumptions that something could also be repeat busienss.


### This is what I am trying to figure out (, so what? How does this affec the business)

1. Which features are most important in determining the delivery time of the given model.  What KPIs do I want to see and measure
    1. So that the business can focus on improving or accounting for those KPI. Delivery Experience is the key, setting customer expectations.
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


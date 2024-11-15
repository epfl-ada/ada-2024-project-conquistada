# What makes for a successful movie?

## Abstract
This project investigates the factors that contribute to a movie's success. Is it as simple as casting the most popular actors ?

To do so, two key dimensions will be examined: financial performance (e.g., box office value, net revenue, revenue/budget ratio) and audience reception (e.g., TMDb ratings). By analyzing features such as cast, budget, runtime, and production company, we aim to identify the elements that are most strongly associated with success in each dimension.

Furthermore, we will conduct a comparative analysis in order to explore the differences between financially successful movies and highly rated ones. The goal is to determine whether it is possible to combine these elements to create a movie that excels both critically and commercially. This analysis will provide data-driven insights into the film industry and inform strategies for optimizing movie production and distribution.


## Research Questions

#### What makes a movie successful?

We will focus on 2 variables to determine success: revenue and TMDb score (see Additional Datasets for more information)

__Revenue__: 

We can study the box office value (gross revenue) the net revenue. 
The revenue/budget ratio is also interesting to study, as the box office does not take into account the costs of the movie.
These can be found in the CMU movie corpus dataset and in the TMDb dataset.
Inflation is also a parameter that should not be neglected. All the cost/revenue data should be scaled according to the inflation between the year of production of a given movie and today. The history of US inflation dataset will be very useful for this.

__TMDb ratings__:

Reviews and rating from viewers.
This score leaves room for subjectivity, but can give us a sense of the artistic/technical merit of the film, in addition to the social and cultural relevance. 
It shows the appreciation of the viewers.
This is found in the TMDb dataset, named vote average. We need to remove movies that have zero votes because they are automatically given a rating of zero.

#### Questions:

+ Is there an ideal runtime to optimize revenue? Is it the same for optimizing viewers apreciation?
+ Does the movie's languages influence success? Are certain languages more popular? Is there an ideal number of different languages?
+ What countries have the most success in the movie industry? What production companies are the most successful? What factors inflence success in different countries?
+ How does budget affect TMDb score and revenue? What makes a movie successful on a low budget?
+ The choice of actors plays an important role in the revenue of a movie. Is it the same for TMDb scores? Which what characteristics should the cast have to ensure a successful movie?
+ What feature is the most important in determining revenue/TMDb score?

## Additional Datasets

The given CMU Movie Dataset Corpus, although being interesting, lacks data: for instance, many box-office revenues are missing. To complete them, [this TMDb Kaggle Dataset](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/data) seemed interesting for us. Note that the dataset used in `results.ipynb` is already processed in `src/data/dataprocessing.py` and includes both data from CMU and TMDb datasets.

Inflation is also a parameter that should not be neglected. All the cost/revenue data should be scaled according to the inflation between the year of production of a given movie and today. [This dataset containing the history of inflation rate in the US](https://www.macrotrends.net/global-metrics/countries/USA/united-states/inflation-rate-cpi) will be very useful for this. Knowing all the annual inflation rates, computing the cumulative rates for every year and applying them to the money-related values will be feasible.


## Methods

**1. Data pre-processing:**
  + Transforming the numerical columns to numbers
  + Transforming columns that list things to actual lists. This makes handling the data easier, such as for one hot encoding
  + One-hot encoding of categorical data (genre, language…)
  + Scaling of cost/revenue to take time into consideration. Transforming revenue to log revenue, to account for the skewed distribution of revenues (see notebook)
    
**2. Initial data analysis:**
  + plotting success vs different features
    + scatter plots for continuous features (runtime, budget, year…)
    + bar plots for categorical data (languages, actors…)
  + Computation of Pearson/Spearman correlation coefficients
  + Regression analysis, and Random Forest for feature importance
  + Analysis of movie summaries, sentiment analysis, readability...
    
**3. Comparative study between financially successful and highly rated movies:**
  + Clustering: Establish clusters of movies according to their genre, budget, country of production...
  + Tree based models to determine feature importance for both financial success and high ratings
  + Supervised ML models to predict both economical and critical successes
  + Analysis of relevant features amongst highly rated movies and financially successful movies
  + Research of a feature combination that can lead to an excellent movie both financially and critically



## Proposed timeline

Deadline: December 20th => 5 weeks left for the project

**Week 1** (-> 22 Nov): Finish the initial data analysis: we already have plots for financial success, need to do the same for TMDb ratings.

**Week 2** (-> 29 Nov): Homework 2, regression analysis and random forest for TMDb ratings

**Week 3** (-> 6 Dec): Supervised machine learning models for predicting TMDb score, clustering of similar movies

**Week 4** (-> 13 Dec): Comparison of feature importance, identification of (dis)similarities between both types of success

**Week 5** (-> 20 Dec): Data story

## Team organisation

Data analysis/visualisation for TMDb ratings: Omar and Erik

Regression analysis + Random Forest: Youssef

Further analysis of summaries, NLP: Liess and Omar

Defining movie clusters, further data transformation: Anna and Youssef

ML models: Erik and Anna

Comparative analysis: Omar and Youssef

Data Story : Everyone

## Questions for TAs 

Are we able to slightly redirect the project during the milestone 3 or are we required to execute what we presented ?

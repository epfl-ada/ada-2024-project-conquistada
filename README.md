# ADA Project: What makes for a successful movie?

## Abstract
For this project, our goal is to find the recipe for a successful movie. Is it as simple as casting the most popular actors?
To do so, we will differentiate between success in terms of revenue (box office value, net revenue, and revenue/budget ratio) and success in terms of viewers’ appreciation (TMDb ratings).
First, we will try to identify relationships between features such as cast, budget, runtime, production company… and the success of a movie. We will therefore be able to identify which features have the most importance in determining success.
We can then do a comparative analysis to better understand the differences between a financially successful movie and a highly rated movie. Doing so, we can study if it is possible to combine both and make the greatest movie of all time.

## Research Questions

#### What makes a movie successful?

We will focus on 2 variables to determine success: revenue and TMDb score (see Additional Dataset for more information)

__Revenue__: 

We can study the box office value (gross revenue) the net revenue. 
The revenue/budget ratio is also interesting to study, as the box office does not take into account the costs of the movie.
These can be found in the CMU movie corpus dataset and in the TMDb dataset.
We need to take time into consideration (because events can affect movie revenue, such as war, pandemics…). To do so, we could normalize the data according to the average revenue of each year.

__TMDb ratings__:

Reviews and rating from viewers.
This score leaves room for subjectivity, but can give us a sense of the artistic/technical merit of the film, in addition to the social and cultural relevance. 
It shows the appreciation of the viewers.
This is found in the TMDb dataset, named vote average. We need to remove movies that have zero votes because they are automatically given a rating of zero.

#### Questions:

+ Is there an ideal runtime to optimize revenue?
+ Does the movie's languages influence success? Are certain languauges more popular? is there an ideal number of different languages?
+ What countries have the most success in the movie industry? What production companies are the most successful? What factors inflence success in different countries?
+ How does budget affect TMDb score and revenue? What makes a movie successful on a low budget?
+ The choice of actors plays an important role in the revenue of a movie. Is it the same for TMDb scores? Which what caracteristics should the cast have to ensure a successful movie?
+ What feature is the most important in determining revenue/TMDb score?

## Additional Dataset

The given CMU Movie Dataset Corpus, although being interesting, lacks data: for instance, many box-office revenues are missing. To complete them, this TMDb Kaggle Dataset seemed interesting for us.

https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/data

In addition, this dataset allows us to increase the size of the sample in order to perform more precise data analysis.

## Methods

+ Data pre-processing:
  + Transforming the numerical columns to numbers
  + Transforming columns that list things to actual lists. This makes handling the data easier, such as for one hot encoding
  + One hot encoding of categorical data (genre, language…)
  + Transforming revenue to log revenue, to account for the skewed distribution of revenues (see notebook)
+ Initial data analysis: plotting success vs different features (for both financial success and viewer ratings)
  + scatter plots for continuous features (runtime, budget, year…)
  + bar plots for categorical data (languages, actors…)
revenue must be adjusted to take time (historical context) into account. To do so we normalize revenue according to the average of each year? or each 5 years? 
  + Regression analysis to identify most important features
  + Comparative study between features linked to financial success and those linked to viewers’ appreciation

## Proposed timeline

Deadline: December 20th => 5 weeks left for the project
Week 1
Week 2
Week 3
Week 4
Week 5


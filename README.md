# What makes for a successful movie?

The description of our project in the form of a data story can be found on [our website](https://epfl-ada.github.io/conquistada.github.io)

https://epfl-ada.github.io/conquistada.github.io

#### Quickstart
```bash
# clone project
git clone <project link>  # use https://github.com/epfl-ada/ada-2024-project-conquistada.git
cd <project repo>  # ada-2024-project-conquistada

# install requirements
pip install -r pip_requirements.txt
```

#### Project Structure
```
├── data                          <- Project data files
│   ├── cmu                           <- CMU Movie Summary Corpus
│   ├── tmdb                          <- TMDb Dataset
│
├── src                           <- Source code
│   ├── data                          <- Data processing
│       ├── dataprocessing.py
│   ├── scripts                       <- Loading and saving the data
│       ├── load_save.py                 
│   ├── utils                         <- Utility directory
│       ├── utils.py
│                      
│
├── README.md                             
├── pip_requirements.txt          <- File for installing python dependencies
└── results.ipynb                 <- Notebook with the results of our analysis
```

#### How to use the library

The datasets we used for our analysis can be found in the [cmu](data/cmu) and the [tmdb](data/tmdb) folders.
The results of our analysis can be found in the notebook [results.ipynb](results.ipynb). This notebook calls methods contained in external scripts for [loading the data](src/data/load_save.py) and [dataprocessing](src/data/dataprocessing.py).

After dowloading the required packages described in [pip_requirements.txt](pip_requirements.txt), you can excecute the notebook to obtain the desired results.

> [!WARNING]
> Please be aware that some cells of the notebook require ~15 min to run. Thank you for your patience :)

A detailed description of our project and the results can be found [here](https://epfl-ada.github.io/conquistada.github.io)

## Abstract
This project investigates the factors that contribute to a movie's success.

To do so, two key dimensions will be examined: financial performance (e.g., box office value, net revenue, revenue/budget ratio) and audience reception (e.g., TMDb ratings). By analyzing features such as runtime, cast, spoken languages, genre, plot summaries, release date... we aim to identify the elements that are most strongly associated with success in each dimension.

Furthermore, we will conduct a comparative analysis in order to explore the differences between financially successful movies and highly rated ones. The goal is to determine whether it is possible to combine these elements to create a movie that excels both critically and commercially. This analysis will provide data-driven insights into the film industry and inform strategies for optimizing movie production and distribution.


## Research Questions

#### What makes a movie successful?

We will focus on 2 variables to determine success: revenue and TMDb score (see [Additional Datasets](#additional-datasets) for more information).

__Revenue__: 

We can study the box office value (gross revenue) the net revenue. 
The revenue/budget ratio is also interesting to study, as the box office does not take into account the costs of the movie.
These can be found in the CMU movie corpus dataset and in the TMDb dataset.

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


## Methods

**1. Data pre-processing:**
  + Cleaning datasets (remove rows with missing values, dropping unnecessary columns) and merging them.
  + Transforming the numerical columns to numbers
  + Transforming columns that list things to arrays. This makes handling the data easier, such as for one hot encoding
  + One-hot encoding of categorical data (genre, language…)
  + Transforming revenue to log revenue, to account for the skewed distribution of revenues
    
**2. Initial data analysis:**
  + plotting movie success vs different features
    + scatter plots for continuous features (runtime, budget, year…)
    + bar plots for categorical data (languages, actors…)
  + Computation of Pearson/Spearman correlation coefficients
  + Analysis of movie summaries: novelty, sentiment analysis, readability...
  + Regression analysis, and Random Forest for feature importance
    
**3. Comparative study between financially successful and highly rated movies:**
  + Clustering: Establish clusters of movies according to their genre, budget, country of production...
  + Tree based models to determine feature importance for both financial success and high ratings
  + Analysis of relevant features amongst highly rated movies and financially successful ones
    + Research of a feature combination that can lead to an excellent movie both financially and critically


## Team organisation

Data analysis + visualisation for revenue: Omar and Eirikur

Data analysis + visualisation for TMDb ratings: Liess and Anna

Regression analysis + Random Forest: Youssef and Eirikur

Analysis of summaries, NLP: Liess and Omar

Comparative analysis: Omar, Youssef Liess

Problem formulation, project description: Anna and Eirikur

Running tests, final touches: Youssef and Anna

Data Story: everyone :)

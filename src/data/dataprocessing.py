import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import json
import spacy

from sklearn.preprocessing import StandardScaler


def clean_tmdb(tmdb):
    """This function cleans the tmdb dataset by removing rows with missing values and dropping unnecessary columns.

    Args:
        tmdb (pd.DataFrame): The tmdb dataset.

    Returns:
        tmdb (pd.DataFrame): The cleaned tmdb dataset.
    """
    tmdb = tmdb.copy()
    tmdb = tmdb.dropna()  # Drop rows with NaN values
    tmdb = tmdb.drop(
        columns=["id", "backdrop_path", "homepage", "poster_path", "imdb_id", "title"]
    )  # Drop columns that are not needed
    tmdb = tmdb.rename(
        columns={"original_title": "Movie name"}
    )  # Rename column to match other datasets
    
    tmdb = tmdb.drop_duplicates(subset='Movie name', keep='first') # Drop duplicates
    return tmdb


def set_up_unique_classes(dataset, column):
    dataset = dataset.copy()
    unique_classes = dataset[column].unique()
    unique_classes_dict = {}
    for i, unique_class in enumerate(unique_classes):
        unique_classes_dict[unique_class] = i
    dataset[column + "_unique"] = dataset[column].map(lambda x: unique_classes_dict[x])
    return dataset


def enrich_dataset(tmdb, movies):
    """This function enriches the cmu dataset with the TMDB dataset, adding information about the movies that are in both datasets. and adding other movies that are not in the cmu movie dataset.

    Args:
        tmdb (pd.DataFrame): The TMDB dataset
        movies (pd.DataFrame): The CMU movie dataset

    Returns:
        pd.DataFrame: The enriched dataset
    """
    df1 = tmdb.copy()
    df1["Movie name"] = df1["Movie name"].str.lower()
    df2 = movies["Movie name"].str.lower()
    # Our original dataset has 2821 movies with enriched data from TMDB
    inclueded = df1[df1["Movie name"].isin(df2)]
    # We add other movies to enrich the dataset
    not_inclueded = df1[~df1["Movie name"].isin(df2)]
    # Concatenate both datasets
    res = pd.concat([inclueded, not_inclueded])
    res["net_revenue"] = tmdb["revenue"] - tmdb["budget"]
    n_budget = tmdb["budget"].apply(lambda x: 1 if x == 0 else x)
    res["revenue/budget"] = tmdb["revenue"] / n_budget

    # Set up a list of ordered languages
    res = set_up_unique_classes(res, "original_language")
    # Get the release year
    res["release_date"] = res["release_date"].apply(lambda x: int(x[:4]))
    # Separate the spoken languages into an array
    res["spoken_languages"] = res["spoken_languages"].apply(
        lambda x: [y.strip() for y in x.split(",")]
    )
    # Add the number of languages
    res["n_languages"] = res["spoken_languages"].apply(lambda x: len(x))
    # Separate the genres into an array
    res["genres"] = res["genres"].apply(lambda x: [y.strip() for y in x.split(",")])
    # Separate the production companies into an array
    res["production_companies"] = res["production_companies"].apply(
        lambda x: [y.strip() for y in x.split(",")]
    )
    # Separate the production countries into an array
    res["production_countries"] = res["production_countries"].apply(
        lambda x: [y.strip() for y in x.split(",")]
    )
    # Separate the keywords into an array
    res["keywords"] = res["keywords"].apply(lambda x: [y.strip() for y in x.split(",")])
    # Explode the dataset
    exploded = res.copy()
    langugaes_exploded = exploded.explode(column="spoken_languages") # Explode the dataset to have one row per language in the spoken languages column
    langugaes_exploded = set_up_unique_classes(langugaes_exploded, "spoken_languages") # Set up unique classes for languages to be able to use them in a model
    genres_exploded = exploded.explode(column="genres") # Explode the dataset to have one row per genre in the genres column
    genres_exploded = set_up_unique_classes(genres_exploded, "genres") # Set up unique classes for genres to be able to use them in a model
    production_companies_exploded = exploded.explode(column="production_companies") # Explode the dataset to have one row per production company in the production companies column
    production_companies_exploded = set_up_unique_classes(production_companies_exploded, "production_companies") # Set up unique classes for production companies to be able to use them in a model    
    production_countries_exploded = exploded.explode(column="production_countries") # Explode the dataset to have one row per production country in the production countries column
    production_countries_exploded = set_up_unique_classes(production_countries_exploded, "production_countries") # Set up unique classes for production countries to be able to use them in a model
    keywords_exploded = exploded.explode(column="keywords")

    return (
        res, # The enriched dataset
        langugaes_exploded, # The exploded dataset with one row per language in the spoken languages column
        genres_exploded, # The exploded dataset with one row per genre in the genres column
        production_companies_exploded, # The exploded dataset with one row per production company in the production companies column
        production_countries_exploded, # The exploded dataset with one row per production country in the production countries column
        keywords_exploded, # The exploded dataset with one row per keyword in the keywords column
    )

# Function to extract named entities from a given text using a natural language processing (NLP) model
def extract_entities(text, nlp):
    """
    Extracts named entities (characters, locations, and other entities) from the provided text.

    Args:
        text (str): The input text from which named entities are to be extracted.
        nlp: The NLP model (e.g., spaCy's language model) used for named entity recognition (NER).

    Returns:
        dict: A dictionary containing lists of identified entities categorized as:
            - 'characters': Names of people (labeled as "PERSON").
            - 'locations': Geopolitical entities like countries, cities, etc. (labeled as "GPE").
            - 'other_entities': Other types of named entities, returned as tuples (entity text, entity label).
    """
    # Process the input text using the provided NLP model
    doc = nlp(text)
    
    # Initialize a dictionary to store extracted entities by category
    entities = {'characters': [], 'locations': [], 'other_entities': []}
    
    # Iterate through all identified named entities in the processed text
    for ent in doc.ents:
        # If the entity is labeled as "PERSON", add it to the 'characters' list
        if ent.label_ == "PERSON":
            entities['characters'].append(ent.text)
        # If the entity is labeled as "GPE" (Geopolitical Entity), add it to the 'locations' list
        elif ent.label_ == "GPE":
            entities['locations'].append(ent.text)
        # For all other entity types, add them to the 'other_entities' list as tuples
        else:
            entities['other_entities'].append((ent.text, ent.label_))
    
    # Return the dictionary of categorized entities
    return entities


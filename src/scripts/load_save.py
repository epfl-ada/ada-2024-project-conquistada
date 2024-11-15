import pandas as pd
from ast import literal_eval

def dict_to_list(dict_str):
    """
    Parses a json dictionary into a list
    """
    try:
        genre_dict = literal_eval(dict_str)
        return list(genre_dict.values())
    except (ValueError, SyntaxError):
        return None

def load_datasets(PATH):
    """This function loads the raw datasets from the CMU Movie dataset and returns them as pandas dataframes.

    Args:
        PATH (str): The path to the directory of the raw datasets.

    Returns:
        pd.DataFrame: The movies dataframe.
        pd.DataFrame: The characters dataframe.
        pd.DataFrame: The names dataframe.
        pd.DataFrame: The plot summaries dataframe.
        pd.DataFrame: The tvtropes dataframe
    """
    movies = pd.read_csv(PATH + 'movie.metadata.tsv', sep='\t', header=None)
    movies.columns = ['Wikipedia movie ID', 'Freebase movie ID', 'Movie name', 'Movie release date', 'Movie box office revenue', 'Movie runtime', 'Movie languages', 'Movie countries', 'Movie genres']
    movies['Extracted Genres'] = movies['Movie genres'].apply(dict_to_list)
    movies['Extracted Languages'] = movies['Movie languages'].apply(dict_to_list)
    movies['Movie box office revenue'] = pd.to_numeric(movies['Movie box office revenue'], errors='coerce')
    movies = movies.dropna(subset=['Movie name', 'Movie box office revenue', 'Extracted Genres'])

    characters = pd.read_csv(PATH + 'character.metadata.tsv', sep='\t', header=None)
    characters.columns = ['Wikipedia movie ID', 'Freebase movie ID','Movie release date', 'Character Name', 'Actor DOB', 'Actor gender', 'Actor height', 'Actor ethnicity', 'Actor Name', 'Actor age at movie release', 'Freebase character map', 'Freebase character ID', 'Freebase actor ID']

    names = pd.read_csv(PATH + 'name.clusters.txt', sep='\t', header=None)
    names.columns = ['Character Name', 'Freebase actor ID']

    plot_summaries = pd.read_csv(PATH + 'plot_summaries.txt', sep='\t', header=None)
    plot_summaries.columns = ['Wikipedia movie ID', 'Plot']

    tvtropes = pd.read_csv(PATH + 'tvtropes.clusters.txt', sep='\t', header=None)
    tvtropes.columns = ['Trope', 'Info']
    return movies, characters, names, plot_summaries, tvtropes


def load_tmdb_raw(PATH):
    """This function loads the raw tmdb dataset and returns it as a pandas dataframe.

    Args:
        PATH (str): The path to the directory of the raw tmdb dataset.

    Returns:
        pd.DataFrame: The tmdb dataframe.
    """
    
    tmdb_dataset = pd.read_csv(PATH + 'TMDB_movie_dataset_v11.csv', sep=',', header=0)   # Load the raw TMDB dataset
    return tmdb_dataset


def load_tmdb(PATH):
    """This function loads the cleaned tmdb dataset and returns it as a pandas dataframe.

    Args:
        PATH (str): The path to the directory of the cleaned tmdb dataset.

    Returns:
        pd.DataFrame: The tmdb dataframe.
    """
    
    tmdb_dataset = pd.read_csv(PATH + 'TMDB.csv', sep=',', header=0)   # Load the cleaned TMDB dataset
    return tmdb_dataset


def save_tmdb(tmdb_dataset, PATH):
    """This function saves the cleaned tmdb dataset as a csv file.

    Args:
        tmdb_dataset (pd.DataFrame): The tmdb dataframe.
        PATH (str): The path to the directory of the cleaned tmdb dataset.
    """
    
    tmdb_dataset.to_csv(PATH + 'TMDB.csv', index=False)   # Save the cleaned TMDB dataset
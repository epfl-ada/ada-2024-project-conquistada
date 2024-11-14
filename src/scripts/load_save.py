import pandas as pd


def load_datasets(PATH):
    """This function loads the raw datasets from the CMU Movie dataset and returns them as pandas dataframes.

    Args:
        PATH (str): The path to the directory of the raw datasets.

    Returns:
        pd.DataFrame: The movies dataframe.
        pd.DataFrame: The characters dataframe.
        pd.DataFrame: The names dataframe.
        pd.DataFrame: The tvtropes dataframe
    """
    movies = pd.read_csv(PATH + 'movie.metadata.tsv', sep='\t', header=None) # Load the raw cmu movie dataset
    movies.columns = ['Wikipedia movie ID', 'Freebase movie ID', 'Movie name', 'Movie release date', 'Movie box office revenue', 'Movie runtime', 'Movie languages', 'Movie countries', 'Movie genres']
    movies = movies.dropna(subset=['Movie name'])
    movies['Movie name'] = movies['Movie name'].str.lower()

    characters = pd.read_csv(PATH + 'character.metadata.tsv', sep='\t', header=None) # Load the raw cmu character dataset
    characters.columns = ['Wikipedia movie ID', 'Freebase movie ID','Movie release date', 'Character Name', 'Actor DOB', 'Actor gender', 'Actor height', 'Actor ethnicity', 'Actor Name', 'Actor age at movie release', 'Freebase character map', 'Freebase character ID', 'Freebase actor ID']

    names = pd.read_csv(PATH + 'name.clusters.txt', sep='\t', header=None) # Load the raw cmu name dataset
    names.columns = ['Character Name', 'Freebase actor ID']

    tvtropes = pd.read_csv(PATH + 'tvtropes.clusters.txt', sep='\t', header=None) # Load the raw cmu tvtropes dataset
    tvtropes.columns = ['Trope', 'Movie name']
    return movies, characters, names, tvtropes


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
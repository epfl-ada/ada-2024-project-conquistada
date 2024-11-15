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
    
def str_to_list(str):
    """
    Parses a string which includes values seperated by commas and returns a list
    """
    try:
        return str.split(", ")
    except AttributeError:
        return None

def get_capitalized_first_letter(text):
    """
    Splits the string into words by ' '. Capitalizes the first
    letter of every word.
    """
    return ' '.join(word.capitalize() for word in text.split())
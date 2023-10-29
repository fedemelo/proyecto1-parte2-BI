from unicodedata import normalize
from joblib import load
from re import sub
import pandas as pd
from nltk.stem import SnowballStemmer
from num2words import num2words
from nltk.corpus import stopwords
from nltk import word_tokenize

def remove_non_ascii(words):
    new_words = []
    for word in words:
        new_word = normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def to_lowercase(words):
    new_words = []
    for word in words:
        new_words.append(word.lower())
    return new_words


def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def replace_numbers(words):
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = num2words(word, lang='es')
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words


def remove_stopwords(words):
    stop_words = set(stopwords.words('spanish'))
    new_words = [word for word in words if word not in stop_words]
    return new_words


def preprocessing(text: str) -> str:
    words = text.split()  # Tokeniza el texto en palabras
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = replace_numbers(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    # Une las palabras procesadas en un texto
    return ' '.join([SnowballStemmer('spanish').stem(word) for word in words])


def classify_multiple_texts(texts_df: pd.DataFrame) -> pd.DataFrame:
    df_columns = texts_df.columns

    if len(df_columns) > 1:
        raise Exception("The dataframe must have only one column")
    elif len(df_columns) < 1:
        raise Exception("The dataframe must have at least one column")
    
    column_name = df_columns[0]
    texts_df[column_name] = texts_df[column_name].apply(word_tokenize)
    new_X = [preprocessing(texto) for texto in texts_df[column_name]]
    pipeline = load('ods_classifier.pkl')
    sdg_column = pipeline.predict(new_X)
    texts_df["sdg"] = sdg_column
    return texts_df


def classify_single_text(text: str) -> int:
    pipeline = load('ods_classifier.pkl')
    return pipeline.predict([preprocessing(text)])[0]

from joblib import load
import pandas as pd
from nltk.stem import SnowballStemmer


def stem_text(text: str) -> str:
    return " ".join([SnowballStemmer('spanish').stem(word) for word in text.split(" ")])


def classify_multiple_texts(texts_df: pd.DataFrame) -> pd.DataFrame:
    df_columns = texts_df.columns

    if len(df_columns) > 1:
        raise Exception("The dataframe must have only one column")
    elif len(df_columns) < 1:
        raise Exception("The dataframe must have at least one column")
    
    column_name = df_columns[0]
    new_X = [stem_text(texto) for texto in texts_df[column_name]]
    pipeline = load('ods_classifier.pkl')
    sdg_column = pipeline.predict(new_X)
    texts_df["sdg"] = sdg_column
    return texts_df


def classify_single_text(text: str) -> int:
    pipeline = load('ods_classifier.pkl')
    return pipeline.predict([stem_text(text)])[0]

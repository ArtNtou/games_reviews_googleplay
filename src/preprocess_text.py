import re
import pandas as pd
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from bertopic import BERTopic


def read_preprocess_data(path):
    # read Excel
    df = pd.read_excel(path)

    # Assuming 'reviews' is a list of customer review texts
    preprocessed_reviews = []

    # break word to its roots
    lemmatizer = WordNetLemmatizer()

    # add to stopwords certain words and game titles
    stop_words = (stopwords.words('english') + ["game", "free", "early", "access", "review", "king", "solitaire","i'm",""])
    titles = [word_tokenize(x.lower()) for x in df['title'].unique()]

    # Concatenate all the lists into one list using list comprehension
    concatenated_titles = list(set([token for sublist in titles for token in sublist]))  # if token != 'crush'
    stop_words += set(concatenated_titles)
    stop_words = [re.sub(r'[^a-zA-Z\s]', '', x) for x in stop_words]

    for review in tqdm(df['content']):
        # Lowercasing
        review2 = review.lower()

        # Removing URLs, special characters, etc.
        review2 = re.sub(r'http\S+', '', review2)
        review2 = re.sub(r'[^a-zA-Z\s]', '', review2)

        # Tokenization
        tokens = word_tokenize(review2)

        # Lemmatization and stop word removal
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]

        # Join negations
        tokens = ["_".join([tokens[i], tokens[i + 1]]) if token == "not" and i < len(tokens) - 1 else token for i, token
                  in enumerate(tokens)]

        preprocessed_reviews.append(' '.join(tokens))

    # Now, 'preprocessed_reviews' can be fed into BERTopic
    df['content_process'] = preprocessed_reviews

    return df

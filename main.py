import pandas as pd
from tqdm import tqdm
from bertopic import BERTopic

from src.preprocess_text import read_preprocess_data

# Initialize variables
path = 'data/game_reviews.xlsx'
game_names = 'title'

# Define parameters for BertTopic
parameters = {'embedding_model': "all-mpnet-base-v2",
              'n_gram_range': (1, 3),
              'min_topic_size': 10,
              'top_n_words': 10,
              'zeroshot_min_similarity': .5}


# read and preprocess data in order to remove stopwords
df = read_preprocess_data(path)

# Initialize dataframes
result_group = pd.DataFrame()
result_review = pd.DataFrame()


# Clusters for each game
for game in tqdm(df['title'].unique()):

    # Use bertopic and we keep unigrams, bigrams and trigrams and each topic has to have 10 comments
    topic_model_process = BERTopic(**parameters)

    # Cluster Data for each game separately
    df_game = df[df['title'] == game]
    df_game['topics'], df_game['probabilities'] = topic_model_process.fit_transform(df_game['content_process'])


    analytical_topics = topic_model_process.get_topic_info()
    analytical_topics['title'] = game

    result_review = pd.concat([result_review, df_game])
    result_group = pd.concat([result_group,analytical_topics])

    del topic_model_process

result_group.to_excel("result_group.xlsx")
result_review.to_excel("result_review.xlsx")
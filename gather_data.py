# pip install google-play-scraper
import pandas as pd
from tqdm import tqdm
from src.get_data import take_game_information, get_game_reviews

tqdm.pandas()

# list of game ids
game_ids = ['com.gamedevltd.modernstrike', 'com.tencent.ig', 'com.king.candycrushsaga', 'com.kiloo.subwaysurf', 'com.dts.freefireth', 'com.dreamgames.royalmatch', 'net.supertreat.solitaire','com.pixonic.wwr','com.actionfit.atlantis','bubbleshooter.orig']

# save game description
game_desc_json = []

df_game_rev = pd.DataFrame()

for id in tqdm(game_ids):

    # get game information
    game_info = take_game_information(id)[0]
    game_desc_json.append(game_info)

    # add all reviews together
    customer_reviews, token = get_game_reviews(id, 0)
    temp = pd.DataFrame(customer_reviews)
    temp['title'] = game_info['title']
    df_game_rev = pd.concat([df_game_rev,temp])

df_game_desc = pd.DataFrame(game_desc_json)

# drop non-relevant columns for description
df_game_desc = df_game_desc.drop(columns=['screenshots','price','currency','video', 'videoImage','descriptionHTML',])

# drop non-relevant columns for reviews
df_game_rev = df_game_rev.drop(columns=['userImage', 'appVersion','repliedAt', 'replyContent'])

# export dataframes to excel
df_game_desc.to_excel("data/game_description.xlsx")
df_game_rev.to_excel("data/game_reviews.xlsx")



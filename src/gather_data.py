# pip install google-play-scraper
from google_play_scraper import search
from google_play_scraper import Sort, reviews
from tqdm import tqdm

tqdm.pandas()


def get_game_reviews(game_id: str, sort_id: int, token: str = '') -> tuple:
    """
    Retrieve reviews for a specific game from the Google Play Store.

    :param game_id: The ID of the game to fetch reviews for.
    :param sort_id: The sorting method for reviews (0 for 'MOST_RELEVANT', 1 for 'RATING', 2 for 'NEWEST').
    :param token: Continuation token for fetching additional reviews (optional).
    :return: A tuple containing reviews data and continuation token.
    """

    if sort_id == 0:
        sort_choice = Sort.MOST_RELEVANT
    elif sort_id == 1:  # Corrected condition
        sort_choice = Sort.RATING
    else:
        sort_choice = Sort.NEWEST

    result, continuation_token = reviews(
        game_id,
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        sort=sort_choice,  # defaults to Sort.NEWEST, Sort.MOST_RELEVANT
        count=1000,  # defaults to 100
        filter_score_with=None  # defaults to None (means all scores)
    )

    if token != '':
        result1, continuation_token = reviews(
            game_id,
            lang='en',  # defaults to 'en'
            country='us',  # defaults to 'us'
            sort=sort_choice,  # defaults to Sort.NEWEST, Sort.MOST_RELEVANT
            count=1000,  # defaults to 100
            continuation_token=token,
        )

    return result, continuation_token


def take_game_information(game_id: str) -> list:
    """
    Retrieve information about a specific game from the Google Play Store.

    :param game_id: The ID of the game to fetch information for.
    :return: A list containing information about the game.
    """

    # You can also search "best pokemon game"
    game = search(
        game_id,
        lang="en",  # defaults to 'en'
        country="us",  # defaults to 'us'
        n_hits=2  # defaults to 30 (= Google's maximum)
    )

    return game

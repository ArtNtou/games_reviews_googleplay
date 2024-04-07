# Game Data Analysis

This repository contains Python scripts for gathering and analyzing game data from the Google Play Store. Two main scripts are provided, each serving a distinct purpose:

## Gathering Game Data

The script `gather_game_data.py` is responsible for collecting information and reviews for a list of specified game IDs using [google-play-scraper](https://github.com/facundoolano/google-play-scraper). Here's how it works:

1. **Import Libraries**: Import the required libraries including `pandas`, `tqdm`, and the custom functions `take_game_information` and `get_game_reviews` from `gather_data` file.

2. **Define Game IDs**: Define a list of game IDs for which you want to collect data. In order to find the ids you can search the game by its name using `take_game_information` in `gather_data` and checking the results

3. **Retrieve Data**: The script retrieves game information and reviews for each game ID. It saves the game descriptions and reviews into Excel files.

## Analyzing Game Reviews

The script `analyze_game_reviews.py` utilizes [BERTopic](https://maartengr.github.io/BERTopic/index.html) to perform topic modeling on game reviews. Here's an overview:

1. **Import Libraries**: Import necessary libraries including `pandas`, `tqdm`, and `BERTopic`.

2. **Preprocess Data**: Read and preprocess game review data, removing stopwords and special characters and preparing the data for analysis. The preprocessing steps include:

3. **Define Parameters**: Set parameters for BERTopic model, specifying embedding model, n-gram range, minimum topic size, top n words, and zero-shot minimum similarity.

4. **Perform Topic Modeling**: For each game, the script clusters the reviews using BERTopic. Analytical insights such as topic information and probabilities are extracted.

5. **Export Results**: The resulting grouped topics and reviews are saved into Excel files for further analysis.

## How to Use

To utilize these scripts:

- Ensure you have the required packages installed. You can install them using `pip install -r requirements.txt`.
- Run each script with appropriate inputs and configurations.

## Note

These scripts are designed for analyzing game data from the Google Play Store. You may need to modify them to suit your specific requirements or adapt them for other data sources. It is still a work in progress, as I will add a frontend in order to visualize results.

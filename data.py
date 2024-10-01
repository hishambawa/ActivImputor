from utils.logger import BasicLogger
import pandas as pd

MOVIES_PATH = "movies.csv"
RATINGS_PATH = "ratings.csv"

class Dataset:
    movies = pd.DataFrame()
    ratings = pd.DataFrame()

    rating_matrix = pd.DataFrame()

    def __init__(self, path, seperator, logger: BasicLogger):
        try:
            # load the dataset
            self.movies = pd.read_csv(path + MOVIES_PATH, sep=seperator)
            self.ratings = pd.read_csv(path + RATINGS_PATH, sep=seperator)

            logger.log_debug("Dataset loaded")

            # create the rating matrix
            self.rating_matrix = self.ratings.pivot(index='userId', columns='movieId', values='rating')

            logger.log_debug("Rating matrix created")

        except Exception as error:
            logger.log_fatal("Dataset loading failed", error)

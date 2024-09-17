import data
from utils.logger import Logger

dataset_path = "../datasets/movielens/ml-latest-small/"
dataset_seperator = ","

# initialize the logger
logger = Logger("debug")

# initialize the dataset
data = data.Dataset(dataset_path, dataset_seperator, logger)
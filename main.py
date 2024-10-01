import data
from utils.logger import BasicLogger

dataset_path = "../datasets/movielens/ml-latest-small/"
dataset_seperator = ","

# initialize the logger
logger = BasicLogger("debug")

logger.log_info("Starting the Data Imputor")

# initialize the dataset
data = data.Dataset(dataset_path, dataset_seperator, logger)
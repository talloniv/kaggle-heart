import json

with open('SETTINGS.json') as data_file:
    PATHS = json.load(data_file)

TRAIN_DATA_PATH = PATHS["TRAIN_DATA_PATH"]
MODEL_PATH = PATHS["MODEL_PATH"]
TEST_DATA_PATH = PATHS["TEST_DATA_PATH"]
SUBMISSION_PATH = PATHS["SUBMISSION_PATH"]
LOGS_PATH = PATHS["LOGS_PATH"]
INTERMEDIATE_PREDICTIONS_PATH = PATHS["INTERMEDIATE_PREDICTIONS_PATH"]
PKL_TRAIN_DATA_PATH = PATHS["PKL_TRAIN_DATA_PATH"]
PKL_TEST_DATA_PATH = PATHS["PKL_TEST_DATA_PATH"]

print TRAIN_DATA_PATH
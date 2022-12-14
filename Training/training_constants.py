from collections import namedtuple

from constants import *

# Data preparation
DATASETS_FOLDER = DATA_FOLDER / "Datasets"
RAW_DATASETS_FOLDER = DATASETS_FOLDER / "Raw"
CLEANED_DATASETS_FOLDER = DATASETS_FOLDER / "Cleaned"
SAMPLES_FOLDER = "Samples"
DATASET_SAMPLES_DF = "dataset_samples_df.csv"

RAW_DATASETS = namedtuple("RAW_DATASETS", "DIGI_FACE")
RAW_DATASETS.DIGI_FACE = RAW_DATASETS_FOLDER / "DigiFace"

DATASETS = namedtuple("DATASETS", "DIGI_FACE")  # Represents the cleaned datasets
DATASETS.DIGI_FACE = CLEANED_DATASETS_FOLDER / "DigiFace"

# Data preprocessing
PREPROCESSED_SAMPLES_FOLDER = DATA_FOLDER / "PreprocessedSamples"

TRAIN_TYPE = 0
TEST_TYPE = 1
VAL_TYPE = 2

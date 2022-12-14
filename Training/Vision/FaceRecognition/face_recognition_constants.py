from Training.Vision import vision_constants as vc

# Data preparation
DATA_FOLDER = vc.DATA_FOLDER / "FaceRecognition"


# Data preprocessing

# Evaluation
EVALUATION_FOLDER = DATA_FOLDER / "Evaluation"
EVALUATION_SAMPLES_DF = EVALUATION_FOLDER / "samples_17324809.csv"

# Training
USE_CACHE = False
MODELS_FOLDER = DATA_FOLDER / "Models"
MODEL_INFO_FILE = "model_info.txt"
MODEL_CHECKPOINTS_FOLDER = "checkpoints"
TOP_MODEL_NAME = "top_model"

# Analysis
WANDB_FOLDER = DATA_FOLDER / "WandB"
WANDB_PROJECT_NAME = "face-recognition"

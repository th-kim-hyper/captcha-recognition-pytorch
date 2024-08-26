import torch

DATA_DIR = "input/captcha_images_v2/"
BATCH_SIZE = 8
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 75
NUM_WORKERS = 8
EPOCHS = 200
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

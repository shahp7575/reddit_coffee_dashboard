import os
import kaggle
import shutil
from config import DATASET_SLUG, DOWNLOAD_PATH

def download_kaggle_dataset():
    """Downloads the dataset from Kaggle and extracts it, ensuring a fresh download."""
    if os.path.exists(DOWNLOAD_PATH):
        # Remove all existing files in the directory
        shutil.rmtree(DOWNLOAD_PATH)
    os.makedirs(DOWNLOAD_PATH)
    os.system(f'kaggle datasets download -d {DATASET_SLUG} -p {DOWNLOAD_PATH} --unzip')

if __name__ == "__main__":
    download_kaggle_dataset()
    print(f"Dataset downloaded and extracted to {DOWNLOAD_PATH}")

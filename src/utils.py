import json
import os

from pathlib import Path


def get_project_root() -> Path:
    # Get the directory of the current script
    current_dir = Path(__file__).resolve().parent

    # Traverse up the directory tree until you find a known file or directory
    while not (current_dir / 'README.md').exists():  # Change 'README.md' to a known file or directory
        if current_dir == current_dir.parent:  # Reached the root of the filesystem
            raise FileNotFoundError("Project root not found")
        current_dir = current_dir.parent

    return current_dir


def load_config():
    project_root = get_project_root()
    config_path = project_root / 'config.json'
    print(config_path)
    # config_path = os.path.join(os.path.dirname(__file__), config_path)
    config = {}
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config


# if __name__ == "__main__":
#     config = load_config()
#     raw_pdfs_path = config['data_paths']['raw_pdfs']
#     processed_texts_path = config['data_paths']['processed_texts']
    # ocr_language = config['ocr_settings']['language']
    # ocr_dpi = config['ocr_settings']['dpi']
    # num_topics = config['analysis_settings']['num_topics']
    # num_keywords = config['analysis_settings']['num_keywords']

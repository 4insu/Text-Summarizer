import os
import yaml
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its content as a ConfigBox object.

    Parameters:
    - path_to_yaml (Path): Path to the YAML file.

    Returns:
    - ConfigBox: ConfigBox object containing the YAML content.

    Raises:
    - ValueError: If the YAML file is not formatted correctly.
    - Exception: For other unexpected errors.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories specified in the list.

    Parameters:
    - path_to_directories (list): List of directory paths to be created.
    - verbose (bool): If True, log directory creation messages.

    Returns:
    - None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Parameters:
    - path (Path): Path to the file.

    Returns:
    - str: A string representing the file size in KB.

    Raises:
    - FileNotFoundError: If the file is not found.
    - Exception: For other unexpected errors.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        raise e
    
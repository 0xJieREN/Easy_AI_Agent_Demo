from typing import Any
from pathlib import Path
import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
base_dir = Path("./test")


def read_file(name: str) -> str:
    logging.info(f"Attempting to read file: {name}")
    try:
        with open(base_dir / name, "r") as f:
            content: str = f.read()
        return content
    except FileNotFoundError:
        logging.error(f"File not found: {name}")
        return f"Error: The file '{name}' was not found."
    except Exception as e:
        logging.error(f"An unexpected error occurred while reading {name}: {e}")
        return f"An error occurred: {e}"


def list_files() -> list[str]:
    print("(list_file)")
    file_list: list[Any] = []
    for item in base_dir.rglob("*"):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list


def rename_file(name: str, new_name: str) -> str:
    print(f"(rename_file{name}->{new_name})")
    try:
        new_path: Path = base_dir / new_name
        if not str(new_path).startswith(str(base_dir)):
            return "Error:new_name is outside base_dir"
        os.makedirs(new_path.parent, exist_ok=True)
        os.rename(base_dir / name, new_path)
        return f"File '{name}' successfully renamed to '{new_name}'."
    except Exception as e:
        return f"An error occured:{e}"


def write_file(name: str, content: str, overwrite: bool = False) -> str:
    """Writes content to a file. To prevent accidental data loss, it will not overwrite existing files by default."""
    print(f"(write_file to {name})")
    file_path = base_dir / name

    # 安全检查：确保写入路径在base_dir内
    if not str(file_path).startswith(str(base_dir)):
        return "Error: File path is outside the allowed directory."

    if file_path.exists() and not overwrite:
        return f"Error: File '{name}' already exists. Use overwrite=True to replace it."

    try:
        # 确保目标目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote to '{name}'."
    except Exception as e:
        return f"An error occurred: {e}"

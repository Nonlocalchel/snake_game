from pathlib import Path
from os import remove
import json


class FileMaster:
    suffix = '.txt'

    @classmethod
    def write_file(cls, path: str, row_data: any) -> None:
        file_path = cls.format_path(path, cls.suffix)
        if file_path.exists():
            return

        cls.create_file(file_path, row_data)

    @classmethod
    def read_file(cls, path: str) -> any:
        file_path = cls.format_path(path, cls.suffix)
        if not file_path.exists():
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            data = cls.load_data(file)
            return data

    @classmethod
    def delete_file(cls, path: str):
        file_path = cls.format_path(path, cls.suffix)
        if file_path.exists():
            cls.remove_file(file_path)

    @classmethod
    def update_file(cls, path: str, row_data: any):
        file_path = cls.format_path(path, cls.suffix)
        cls.remove_file(file_path)

        cls.create_file(file_path, row_data)

    @classmethod
    def create_file(cls, path: Path, row_data: any) -> None:
        data = cls.dump_data(row_data)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)

    @staticmethod
    def remove_file(file_path: Path) -> None:
        if file_path.exists():
            remove(file_path)

    @staticmethod
    def dump_data(data: any) -> any:
        return str(data)

    @staticmethod
    def load_data(data: any) -> any:
        return eval(data.read())

    @staticmethod
    def format_path(row_path: str, suffix: str) -> Path:
        f_path = Path(row_path)
        if f_path.name == f_path.stem:
            f_path = f_path.with_suffix(suffix)

        return f_path

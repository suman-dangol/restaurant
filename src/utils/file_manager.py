#file_manager.py
import os
from src.utils.exceptions import FileError

class FileManager:
    
    @staticmethod
    def read_file(file_path):
        """Reads all lines from a file and returns them as a list of strings."""
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
            return lines
        except FileNotFoundError:
            raise FileError(f"File not found: {file_path}")
        except Exception as e:
            raise FileError(f"Error reading file {file_path}: {e}")
    
    @staticmethod
    def write_file(file_path, lines):
        """Writes a list of strings to a file, overwriting the file if it exists."""
        try:
            with open(file_path, 'w') as file:
                for line in lines:
                    file.write(line + '\n')
        except Exception as e:
            raise FileError(f"Error writing to file {file_path}: {e}")
    
    @staticmethod
    def append_file(file_path, line):
        """Appends a line to a file."""
        try:
            with open(file_path, 'a') as file:
                file.write(line + '\n')
        except Exception as e:
            raise FileError(f"Error appending to file {file_path}: {e}")
    
    @staticmethod
    def clear_file(file_path):
        """Clears the content of a file."""
        try:
            with open(file_path, 'w') as file:
                file.write('')  # Truncate the file
        except Exception as e:
            raise FileError(f"Error clearing file {file_path}: {e}")

    @staticmethod
    def file_exists(file_path):
        """Checks if a file exists."""
        return os.path.exists(file_path)
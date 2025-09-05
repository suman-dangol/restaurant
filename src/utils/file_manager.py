#file_manager.py
from utils.exceptions import FileError

class FileManager:
    """Handles reading from and writing to text files."""
    
    @staticmethod
    def read_file(file_path):
        """Read data from a file and return as a list of lines."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]
        except FileNotFoundError:
            raise FileError(f"File not found: {file_path}")
        except IOError:
            raise IOError(f"Error reading file: {file_path}")

    @staticmethod
    def write_file(file_path, data):
        """Write data to a file."""
        try:
            with open(file_path, 'w') as file:
                file.writelines(data)
        except IOError:
            raise IOError(f"Error writing to file: {file_path}")
    
    @staticmethod
    def append_file(file_path, line):
        """Append a line to a file."""
        try:
            with open(file_path, "a") as f:
                f.write(f"{line}\n")
        except Exception as e:
            raise FileError(f"Error appending to {file_path}: {e}")
        
        
"""static method decorator is used to define methods that do not require access to the instance (self) or class (cls)"""""
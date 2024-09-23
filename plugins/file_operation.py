import os

def register():
    return "file_operation"

class FileHandler:
    @staticmethod
    def create_file(filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as f:
            return f.read()

    @staticmethod
    def update_file(filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    @staticmethod
    def delete_file(filename):
        os.remove(filename)

def run():
    return FileHandler()


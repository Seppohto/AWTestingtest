import os
from pathlib import Path


# def get_env(value):
#     env = os.getenv(value)
#     print(f'The environment variable value is {env}')
#     return env

def get_file_path():
    path = os.path.dirname(os.path.abspath(__file__)) 
    return path
# print (Path(__file__).parent.absolute()) 
# print(os.path.dirname(os.path.abspath(__file__)))
# print(Path(__file__).parent.resolve())
# print(Path().resolve())

def list_file_in_dir(directory):
    return
    
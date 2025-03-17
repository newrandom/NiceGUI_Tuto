from configparser import ConfigParser
import platform
from typing import Callable

def checkMyOS() -> str:
    OS_NAME = platform.system()

    if OS_NAME == "Windows":
        os_section = 'postgresql_win'
    elif OS_NAME == "Darwin":
        os_section = 'postgresql_mac'
    else:
        os_section = 'postgresql_linux'
    return os_section

def load_config(filename='../database.ini', section_func: Callable[[], str] = checkMyOS):
    section = section_func()
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return config

if __name__ == '__main__':
    config = load_config()
    print(config)
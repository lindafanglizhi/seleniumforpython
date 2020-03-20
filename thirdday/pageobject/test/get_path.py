import os


def get_parent_abspath():
    parent_abspath = os.path.abspath(os.path.dirname(os.getcwd()))
    return parent_abspath


print(get_parent_abspath())
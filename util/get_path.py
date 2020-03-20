import os


def get_par_path():
    root_path = os.path.abspath(os.path.dirname(__file__)).split('util')[0]
    # 返回的就是根路径
    return root_path


print(get_par_path())
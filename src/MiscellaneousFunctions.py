import os


def file_reading_gen(path, fields, sep=',', header=False):
    try:
        file = open(path, "r")
    except IOError:
        print("error in reading File")
    else:
        with file:
            res = []
            for index, line in enumerate(file):
                if header:
                    header = False
                    continue
                arr = line.strip("\n").split(sep)
                if len(arr) != fields:
                    raise ValueError(
                        f"'{path}' has {len(arr)} fields on line {index + 1} but expected {fields}")
                res.append(tuple(arr))
            return res


def is_path_valid(base_url):
    return os.path.exists(base_url) and os.path.isdir(base_url)

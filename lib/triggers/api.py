from os import path


def device(version, name):
    if name is None:
        return version

    return path.normpath(path.join(version, name))

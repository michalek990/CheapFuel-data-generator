import pkg_resources


def read_usernames():
    path = pkg_resources.resource_filename('Models.Datasets', 'usernames.txt')
    file = open(path, 'r')
    lines = [line.rstrip() for line in file]
    file.close()
    return lines
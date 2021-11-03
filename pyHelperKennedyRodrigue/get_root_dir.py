def get_root_dir():
    if sys.platform == 'darwin':
        root_dir = '/Volumes'
    elif sys.platform == 'linux':
        root_dir = '/raid/data'
    else
        raise Exception("could not determine root_dir")
        return
    return root_dir
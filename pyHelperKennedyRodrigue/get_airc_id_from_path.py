def get_airc_id_from_path(path):
    """
    get the AIRC ID from the path
    """
    idx=path.find('3tb')
    if idx != -1:
        return path[idx:idx+7]
    else:
        raise Exception('there is no airc id in the path: %s' % path)
def get_n_vols_from_task(task):
    """
    get the number of volumes for a specific task (i.e., dj or nback)
    """
    if task == 'dj':
        n_vols = 210
    elif task == 'nback':
        n_vols = 260
    return n_vols
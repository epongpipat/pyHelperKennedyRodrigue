import pandas as pd
import numpy as np

def get_airc_id_from_sub_ses(sub, ses):
    """
    get airc id from subject id and session/wave number
    """
    root_dir = '/raid/data'
    in_path = '%s/shared/incoming/ids_long-format.csv' % (root_dir)
    df = pd.read_csv(in_path)
    mri_id_list = list(df.loc[df.study_id == sub, 'mri_id'])
    mri_id_numbers = np.unique([float(x.replace('3tb', '').replace('a', '').replace('b', '')) for x in mri_id_list])
    if ses == 1:
        mri_id_number = int(mri_id_numbers[mri_id_numbers < 4188][0]) # probably needs a better system here
    elif ses == 2:
        mri_id_number = int(mri_id_numbers[mri_id_numbers > 4188][0])
    mri_id = '3tb%s' % (mri_id_number)
    return mri_id
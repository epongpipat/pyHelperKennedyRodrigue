import pandas as pd
import numpy as np
import . as get_root_dir

def get_airc_id_from_sub_ses(sub, ses):
    """
    get airc id from subject id and session/wave number
    """
    root_dir = get_root_dir("kenrod")
    in_path = f"{root_dir}/incoming/ids_long-format.csv"
    df = pd.read_csv(in_path)
    df_sub = df[df.study_id == sub]
    df_sub = df_sub[df_sub.wave == ses]
    mri_id = df_sub.mri_id.values

    if len(mri_id) == 0:
        raise Exception("airc id not found")
    elif len(mri_id) > 1:
        warnings.warn("multiple airc ids found")
        return mri_id
    else:
        mri_id = mri_id[0]

    return mri_id

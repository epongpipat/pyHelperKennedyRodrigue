import sys
import pandas as pd
import os
import socket
import pkg_resources


def get_root_dir(dir):
    """
    Get the root directory for a given directory.

    Parameters
    ----------
    dir : str
        The directory for which the root directory is desired. can be one of:
        "kmk", "kmr", or "kenrod"

    Returns
    -------
    root_dir : str
        The root directory for the given directory.
    """
    dir_list = ["kmk", "kmr", "kenrod"]
    if dir not in dir_list:
        raise Exception("dir must be one of: {}".format(dir_list))

    in_path = pkg_resources.resource_filename(__name__, "data/root_dir.csv")
    df = pd.read_csv(in_path)
    os = sys.platform
    os = os.title()
    hostname = socket.gethostname()
    df_sub = df[df["dir"] == dir]
    df_sub = df_sub[df_sub["os"] == os]
    if os == "linux":
        df_sub = df_sub[df_sub["hostname"] == hostname]
    root_dir = df_sub["path"].values[0]
    return root_dir

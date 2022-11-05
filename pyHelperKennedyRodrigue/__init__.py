import pkg_resources

__version__ = pkg_resources.require("pyHelperKennedyRodrigue")[0].version

from .get_airc_id_from_sub_ses import get_airc_id_from_sub_ses
from .get_n_vols_from_task import get_n_vols_from_task
from .get_root_dir import get_root_dir
from .get_airc_id_from_path import get_airc_id_from_path
from .print_header import print_header
from .print_footer import print_footer
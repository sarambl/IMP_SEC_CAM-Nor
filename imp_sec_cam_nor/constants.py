import os
import socket
from useful_scit.util.make_folders import make_folders
import pandas as pd
# %%
from imp_sec_cam_nor.project_root import get_project_base

TEST_MODE = False
LOCAL_DATA_MODE = False

project_name = 'IMP_SEC_CAM-Nor'
hostname = socket.gethostname()
# Raw data path:
nird_project_code = 'NS9066K'
_data_folder = 'model_output/archive/'

# root:
project_base_path = get_project_base(hostname, nird_project_code)


if not LOCAL_DATA_MODE:
    raw_data_path_NorESM = project_base_path + _data_folder
else:
    raw_data_path_NorESM = '/persistent01/model_output/archive/'

pathdic_raw_data = {'NorESM': raw_data_path_NorESM}  # [file_source]}


def get_input_datapath(model='NorESM'):
    return pathdic_raw_data[model]


# Plots path:
path_plots = project_base_path + '/Plots_' + project_name + '/'

paths_plotsave = dict(maps=path_plots + 'maps/',
                      comparison=path_plots + 'global_comparison/',
                      one_value=path_plots + 'one_value/',
                      lineprofiles=path_plots + 'lineprofiles/',
                      sizedist=path_plots + 'sizedistribution/',
                      sizedist_time=path_plots + 'sizedist_time/',
                      levlat=path_plots + 'levlat/',
                      eusaar=path_plots + 'eusaar/'
                      )


def get_plotpath(key):
    """

    :param key:
    :return:
    """
    if key in paths_plotsave:
        return paths_plotsave[key]
    else:
        return path_plots + '/' + key + '/'


path_eusaar_data = project_base_path + '/EUSAAR_data'

path_EBAS_data = project_base_path + '/EBAS_data'

# Output data:

path_outdata = project_base_path + '/Output_data_' + project_name + '/'

path_eusaar_outdata = path_eusaar_data + '/EUSAAR_data/'

latlon_path =path_outdata +'latlon.nc'

def get_outdata_base():
    return path_outdata


outpaths = dict(
    pressure_coords=path_outdata + '/Fields_pressure_coordinates',
    original_coords=path_outdata + '/computed_fields_ng',
    computed_fields_ng=path_outdata + '/computed_fields_ng',  # native grid computed fields
    pressure_coords_converstion_fields=path_outdata + '/Pressure_coordinates_conversion_fields',
    pressure_density_path=path_outdata + '/Pressure_density',
    masks=path_outdata + '/means/masks/',
    area_means=path_outdata + '/means/area_means/',
    map_means=path_outdata + '/means/map_means/',
    levlat_means=path_outdata + '/means/levlat_means/',
    profile_means=path_outdata + '/means/profile_means/',
    sizedistrib_files=path_outdata + '/sizedistrib_files',
    collocated=path_outdata + '/collocated_ds/',
    eusaar=path_outdata + '/eusaar/',
)


def get_outdata_path(key):
    if key in outpaths:
        return outpaths[key]
    else:
        print('WARNING: key not found in outpaths, constants.py')
        return path_outdata + '/' + key


make_folders(path_outdata)

# data info
proj_lc = project_name.lower().replace('-', '_')

path_data_info = project_base_path + f'{project_name}/{proj_lc}/data_info/'
# output locations:
path_locations_file = path_data_info + 'locations.csv'
if os.path.isfile(path_locations_file):
    collocate_locations = pd.read_csv(path_locations_file, index_col=0)
else:
    _dic = dict(Hyytiala={'lat': 61.51, 'lon': 24.17},
                Melpitz={'lat': 51.32, 'lon': 12.56},
                Amazonas={'lat': -3., 'lon': -63.},
                Beijing={'lat': 40, 'lon': 116})
    collocate_locations = pd.DataFrame.from_dict(_dic)
    collocate_locations.to_csv(path_locations_file)


## Sizedistribution:
sized_varListNorESM = {'NCONC': ['NCONC01', 'NCONC02', 'NCONC04', 'NCONC05', 'NCONC06', 'NCONC07', 'NCONC08',
                                 'NCONC09', 'NCONC10', 'NCONC12', 'NCONC14'],
                       'SIGMA': ['SIGMA01', 'SIGMA02', 'SIGMA04', 'SIGMA05', 'SIGMA06', 'SIGMA07', 'SIGMA08',
                                 'SIGMA09', 'SIGMA10', 'SIGMA12', 'SIGMA14'],
                       'NMR': ['NMR01', 'NMR02', 'NMR04', 'NMR05', 'NMR06', 'NMR07', 'NMR08',
                               'NMR09', 'NMR10', 'NMR12', 'NMR14']}

sized_varlist_SOA_SEC = ['nrSOA_SEC01', 'nrSOA_SEC02', 'nrSOA_SEC03', 'nrSOA_SEC04', 'nrSOA_SEC05']

sized_varlist_SO4_SEC = ['nrSO4_SEC01', 'nrSO4_SEC02', 'nrSO4_SEC03', 'nrSO4_SEC04', 'nrSO4_SEC05']

list_sized_vars_noresm = sized_varListNorESM['NCONC'] + \
                         sized_varListNorESM['SIGMA'] + \
                         sized_varListNorESM['NMR'] + \
                         sized_varlist_SOA_SEC + \
                         sized_varlist_SO4_SEC
list_sized_vars_nonsec = sized_varListNorESM['NCONC'] + sized_varListNorESM['SIGMA'] + sized_varListNorESM['NMR']


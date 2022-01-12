from imp_sec_cam_nor.constants import project_base_path,path_data_info
import pandas as pd
path_Nd_var_name = path_data_info + '/Nd_bins.csv'

diameter_obs_df = pd.read_csv(path_Nd_var_name, index_col=0)


# %%
diameters_observation ={'N30-50':[30,50], 'N50':[50,500],'N100':[100,500], 'N250':[250,500]}
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Check that cases are the same

# %%
from IPython import get_ipython
from useful_scit.imps import (plt)

from imp_sec_cam_nor.util.imports import get_averaged_fields
# %%
from imp_sec_cam_nor.util.plot.plot_maps import plot_map_abs_abs_diff

# noinspection PyBroadException
try:
    _ipython = get_ipython()
    _magic = _ipython.magic
    _magic('load_ext autoreload')
    _magic('autoreload 2')
except:
    pass


# %%

startyear = '2007-01'
endyear = '2007-02'
pmin = 850.  # minimum pressure level
avg_over_lev = True  #
pressure_adjust = True  # Can only be false if avg_over_lev false. Plots particular hybrid sigma lev
if avg_over_lev:
    pressure_adjust = True

# %% [markdown]
# ## Cases

# %%
to_case = 'NFHISTnorsecpddmsbcsdyn_f09_f09_mg17'
from_cases = ['NFHISTnorsecpddmsbcsdyn_f09_f09_mg17']
cases1 = [from_cases[0], to_case]

# %%
def load_and_plot(var, cases, startyear, endyear,
                  avg_over_lev=avg_over_lev,
                  pmin=pmin,
                  pressure_adjust=pressure_adjust, p_level=None, relative=False):
    maps_dic = get_averaged_fields.get_maps_cases(cases, [var], startyear, endyear,
                                                  avg_over_lev=avg_over_lev,
                                                  pmin=pmin,
                                                  pressure_adjust=pressure_adjust, p_level=p_level)
    return plot_map_abs_abs_diff(var, cases, maps_dic, relative=relative, figsize=[18, 3], cbar_equal=True,
                                 kwargs_abs={},
                                 kwargs_diff={}, axs=None, cmap_abs='Reds', cmap_diff='RdBu_r')

# %% [markdown]
# ## Define variables to plot: 

# %%
varl_aero1 = ['N_AER', 'NCONC01', 'NMR01', 'NCONC02', 'NMR02', 'NCONC04', 'NMR04', 'NCONC05',
              'NMR05', 'NCONC06', 'NMR06',
              'NCONC07', 'NMR07', 'NCONC08', 'NMR08', 'NCONC09', 'NMR09', 'NCONC10', 'NMR10',
              'NCONC12', 'NMR12', 'NCONC14', 'NMR14',
              ]

varl_aero2 = [
    'SO4_NA', 'SO4_A1', 'SO4_A2', 'SO4_AC', 'SO4_PR', 'BC_N', 'BC_AC', 'BC_AX', 'BC_NI', 'BC_A', 'BC_AI', 'OM_NI',
    'OM_AI', 'OM_AC', 'DST_A2', 'DST_A3', 'SS_A1', 'SS_A2', 'SS_A3', 'SOA_A1', 'SOA_NA',
    'cb_SO4_NA', 'cb_SO4_A1', 'cb_SO4_A2', 'cb_SO4_AC', 'cb_SO4_PR', 'cb_BC_N', 'cb_BC_AC', 'cb_BC_AX', 'cb_BC_NI',
    'cb_BC_A', 'cb_BC_AI', 'cb_OM_NI', 'cb_OM_AI', 'cb_OM_AC', 'cb_DST_A2', 'cb_DST_A3', 'cb_SS_A1', 'cb_SS_A2',
    'cb_SS_A3', 'cb_SOA_A1', 'cb_SOA_NA',
]

# %%
varl_aero_sec = ['nrSOA_SEC_tot', 'nrSO4_SEC_tot', 'nrSEC_tot',
                 'cb_SOA_SEC01', 'cb_SOA_SEC02', 'cb_SOA_SEC03',
                 'leaveSecH2SO4', 'leaveSecSOA',
                 ]

# %%

varl_rad = [
    'FLNTCLR', 'FLUTC', 'FSUTOA', 'FSNTC', 'FSNS', 'FSDSC',
    'FSNT', 'FLNT',
    'SWCF', 'LWCF',

]

# %% [markdown]
# ## Plots

# %%
for var in varl_aero1:
    load_and_plot(var, cases1, startyear, endyear, avg_over_lev, pmin=pmin, pressure_adjust=pressure_adjust,
                  relative=True)
    plt.show()

# %%
for var in varl_aero2:
    load_and_plot(var, cases1, startyear, endyear, avg_over_lev, pmin=pmin, pressure_adjust=pressure_adjust,
                  relative=True)
    plt.show()

# %%
for var in varl_aero_sec:
    load_and_plot(var, cases1, startyear, endyear, avg_over_lev, pmin=pmin, pressure_adjust=pressure_adjust,
                  relative=True)
    plt.show()

# %%
for var in varl_rad:
    load_and_plot(var, cases1, startyear, endyear, avg_over_lev, pmin=pmin, pressure_adjust=pressure_adjust,
                  relative=True)
    plt.show()

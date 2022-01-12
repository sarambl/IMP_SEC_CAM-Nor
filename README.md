## Documentation and development for implementation of sectional scheme as namelist option in CAM-Nor

This repository contains the analysis of a series of tests concerning the technical implementation of the sectional scheme (see Blichner et al (2021b)) as an option when running NorESM2 (Seland et al, 2020).

Firstly, notebook [imp_sec_cam_nor/notebooks/check_case.py](imp_sec_cam_nor/notebooks/check_case.ipynb) contains a series of very short tests for checking that inclusion of documentation and technical changes in the setup does not change the results. 

Secondly, a series of formal tests have been performed to check the setup:

1. Two runs with resolution f19_f19_mg17 were performed for 2 months, one with two runs straight (NFHISTnorsecpddmsbcsdyn_f19_f19_mg17) and one with 1+1 months and restarting it in between (NFHISTnorsecpddmsbcsdyn_f19_f19_mg17_1p1m). These are both hybrid runs with refcase spinup_freemet_from2000 (see Blichner et al 2020b, data). We then check that these yield the same results (see notebook [imp_sec_cam_nor/notebooks/checks/diff_f19_f19_1p1m.ipynb](imp_sec_cam_nor/notebooks/checks/diff_f19_f19_1p1m.ipynb)).
2. Two runs with resolution f09_f09_mg17 were performed for 2 months, one with two runs straight (NFHISTnorsecpddmsbcsdyn_f09_f09_mg17) and one with 1+1 months and restarting it in between (NFHISTnorsecpddmsbcsdyn_f09_f09_mg17_1p1m). These are both startup runs. We then check that these yield the same results (see notebook [imp_sec_cam_nor/notebooks/checks/diff_f09_f09_1p1m.ipynb](imp_sec_cam_nor/notebooks/checks/diff_f09_f09_1p1m.ipynb)).
3. Two runs with the default model with compset NFHISTnorpddmsbcsdyn are performed, one before (NFHISTnorpddmsbcsdyn_f19_f19_mg17_pre-merge) and one  after (NFHISTnorpddmsbcsdyn_f19_f19_mg17_post-merge) we merge the changes. This to check that the extra code does not interfer with the default model. See notebook [imp_sec_cam_nor/notebooks/checks/diff_f19_f19_pre_post_merge.ipynb](imp_sec_cam_nor/notebooks/checks/diff_f19_f19_pre_post_merge.ipynb) 
.


## References
- Blichner, S. M., Sporre, M. K., & Berntsen, T. K. (2021a). Reduced effective radiative forcing from cloud–aerosol interactions (ERFaci) with improved treatment of early aerosol growth in an Earth system model. Atmospheric Chemistry and Physics, 21(23), 17243–17265. https://doi.org/10.5194/acp-21-17243-2021
- Blichner, S. M., Sporre, M. K., Makkonen, R., & Berntsen, T. K. (2021b). Implementing a sectional scheme for early aerosol growth from new particle formation in the Norwegian Earth System Model v2: Comparison to observations and climate impacts. Geoscientific Model Development, 14(6), 3335–3359. https://doi.org/10.5194/gmd-14-3335-2021
- Seland, Ø., Bentsen, M., Olivié, D., Toniazzo, T., Gjermundsen, A., Graff, L. S., Debernard, J. B., Gupta, A. K., He, Y.-C., Kirkevåg, A., Schwinger, J., Tjiputra, J., Aas, K. S., Bethke, I., Fan, Y., Griesfeller, J., Grini, A., Guo, C., Ilicak, M., … Schulz, M. (2020). Overview of the Norwegian Earth System Model (NorESM2) and key climate response of CMIP6 DECK, historical, and scenario simulations. Geoscientific Model Development, 13(12), 6165–6200. https://doi.org/10.5194/gmd-13-6165-2020




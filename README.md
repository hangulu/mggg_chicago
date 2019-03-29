### MGGG Chicago Analysis

This repository stores the analyses done for the MGGG (mggg.org) Chicago project. The following are the relevant files/directories and their descriptions.

**Directories**

- [chicago_vote_history/](chicago_vote_history/): store of the election data from Chicago elections
- [rrps/](rrps/): store of the ranked-choice voting data for Oakland, Cambridge, and Minneapolis elections
- [rrps_results/](rrps_results/): store of the results of the Chicago RRPS models
- [run_results/](run_results/): store of the chain run results (pickled files)
- [shapefiles/](shapefiles/): Chicago shapefiles
- [projection/](projection/): The sensitivity analysis of the projection numbers used in the final report's model

**Notebooks**

_Chain Runs_

- [chicago_rrps.ipynb](chicago_rrps.ipynb): executes the workflow to derive the racially-reduced preference schedule of Chicago with the First-choice Distribution Model (FC) using frequency proportion
- [comareas4_runs.ipynb](comareas4_runs.ipynb): performs a chain run for wards of magnitude 4, out of community areas, using Metropolis-Hastings for acceptance
- [precinct10a_runs.ipynb](precinct10a_runs.ipynb): performs a chain run for 10 wards with 3% population deviation, out of precincts
- [precinct10b_runs.ipynb](precinct10a_runs.ipynb): performs a chain run for 10 wards with 4% population deviation, out of precincts
- [precinct50_runs.ipynb](precinct10a_runs.ipynb): performs a chain run for 50 wards with 5% population deviation, out of precincts

_RRPS_

- [rrps_vrpm.ipynb](match_data/rrps_vrpm.ipynb): finds the RRPS of Chicago with the Voter Race Distribution Model, using Precinct Matching by demographics
- [rrps_fcfp.ipynb](rrps_fcfp.ipynb): finds the RRPS of Chicago with the First-Choice Distribution Model, using Frequency Proportion
- [rrps_fcpm.ipynb](rrps_fcpm.ipynb): finds the RRPS of Chicago with the First-Choice Distribution Model, using Precinct Matching by voting patterns

_Sensitivity Analysis_

- [Sensitivity.ipynb](projection/Sensitivity.ipynb): performs sensitivity analysis of the projection numbers used in the report.

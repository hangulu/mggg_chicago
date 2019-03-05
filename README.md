### MGGG Chicago Analysis

This repository stores the analyses done for the MGGG (mggg.org) Chicago project. The following are the relevant files/directories and their descriptions.

**Directories**

- chicago_vote_history/: store of the election data from Chicago elections
- rrps/: store of the ranked-choice voting data for Oakland, Cambridge, and Minneapolis elections
- rrps_results/: store of the results of the Chicago RRPS model
- run_results/: store of the chain run results (pickled files)
- shapefiles/: Chicago shapefiles

**Notebooks**
- chicago_rrps.ipynb: executes the workflow to derive the racially-reduced preference schedule of Chicago with the First-choice Distribution Model (FC) using frequency proportion
- comareas4_runs.ipynb: performs a chain run for wards of magnitude 4, out of community areas, using Metropolis-Hastings for acceptance
- precinct10a_runs.ipynb: performs a chain run for 10 wards with 3% population deviation, out of precincts
- precinct10b_runs.ipynb: performs a chain run for 10 wards with 4% population deviation, out of precincts
- precinct50_runs.ipynb: performs a chain run for 50 wards with 5% population deviation, out of precincts

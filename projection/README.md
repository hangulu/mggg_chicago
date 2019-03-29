### MGGG Chicago Report Sensitivity Analysis

#### Contents

- `projection/`: Code and results of our demographic threshold model
  projections, as described in section 5 of the report.
  - This version differs from that at [the MGGG repo](https://github.com/mggg/chicago) in that this contains sensitivity analysis of the numbers used for the projection. This code lives in [Sensitivity.ipynb](https://github.com/hangulu/mggg_chicago/blob/master/projection/projection/Sensitivity.ipynb)
  - The results of the sensitivity analysis can be found in [sensitivity_analysis/](https://github.com/hangulu/mggg_chicago/tree/master/projection/projection/sensitivity_analysis).
- `ranked_choice/`:
  - Ranked-choice ballot data from Cambridge, Minneapolis, and Oakland.
  - Partial candidate demographic identifications
  - Cleaning scripts for the preference schedules
  - Code for running hypothetical single transferable vote elections using the
    real preference schedule data. This code uses the
    [rcv](https://github.com/gerrymandr/rcv) package, which was created by MGGG
    during this project.
- `shapefiles/`: Cleaned shapefiles with demographics and election data joined.
  See also
  [mggg-states/IL-shapefiles](https://github.com/mggg-states/IL-shapefiles).

#### Ensembles

The output of our MCMC runs is too large to store on GitHub. We have hosted
these files on MIT's storage instead:

- [50x1](http://people.csail.mit.edu/maxhully/chicago-ensembles/prec50.zip)
- [10xM](http://people.csail.mit.edu/maxhully/chicago-ensembles/prec10.zip)
- [10xM CA](http://people.csail.mit.edu/maxhully/chicago-ensembles/ca10.zip)

These `.zip` archives each contain:

- The tabular results of the run with the ward-level demographics of each
  districting plan in each of the ensembles, as well as
- The precinct-to-ward assignments for every districting plan in each ensemble.

You must download these files and put them in an `ensembles/` folder for the projection code to work.

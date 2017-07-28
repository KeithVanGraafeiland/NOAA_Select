# NOAA_Select
## Python processing for NOAA Select downloaded data.

* Download data from NOAA Select. [NOAA Select Download](https://www.nodc.noaa.gov/OC5/SELECT/dbsearch/dbsearch.html)
* Extract the TAR.GZ files to TAR files.
* Separate into TAR directory.
* Extract each TAR to seperate directory.
* Remove the "index" NetCDF File from each extracted directory.  This is generally the leading file and has a different name format from the other files in the directory.
* Place the "NOAA_Select_NetCDF_to_CSV.py" script file into the TAR directory.
* Modify the variable in the "NOAA_Select_NetCDF_to_CSV.py" script to the appropriate variable.
* Run the script using PyScripter.

[Panoply Webpage](https://www.giss.nasa.gov/tools/panoply/)
## Utilize Panopoly if needed to read the variable names from the NetCDF File.



#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      keit8223
#
# Created:     27/07/2017
# Copyright:   (c) keit8223 2017
# Licence:     <your licence>
#
#
#
#
# This file takes an input directory from the TAR NOAA Select Files in NetCDF
# Format and creates CSV delinated text files for the variable, lat, long,
# depth, and date.  File should live in the root of the TAR directory and
# varName needs to be defined before running.
#
#
#
#-------------------------------------------------------------------------------
import netCDF4
import os
import csv

directory = os.path.dirname(os.path.realpath(__file__))
##out_file = r'D:\~Share\WOA_NOAA_Select\Salinity\Salinity_DRB.txt'
varName = 'Oxygen'

def processItmesInMainDir(dirName):
    lastPartOfFolderName = dirName.split('.')[2]

    out_file = varName + "_" + lastPartOfFolderName + '.txt'
    out = open(out_file, 'wb')
    writer = csv.writer(out)
    writer.writerow(('date', 'lat', 'lon','z', varName))

    proceeItemsInSubDir(dirName, writer)

    out.close()
    print("Done Processing " + varName)


def proceeItemsInSubDir(dirName, writer):

    for filename in os.listdir(dirName):
        if filename.endswith('.nc'):
            filepath = os.path.join(dirName, filename)
            print(filepath)
            f = netCDF4.Dataset(filepath,'r')
            value_array = f.variables[varName][:]
            for i in xrange(0, len(value_array)):
                if f.variables[varName][i] > 0:
                    writer.writerow((f.variables['date'][0], f.variables['lat'][0], f.variables['lon'][0], f.variables['z'][i], '{:.20f}'.format(f.variables[varName][i])))
            f.close()
        else:
            continue


for name in os.listdir(directory):

    if os.path.isdir(os.path.join(directory, name)):
        processItmesInMainDir(name)



##out = open(out_file, 'wb')
##writer = csv.writer(out)
##writer.writerow(('date', 'lat', 'lon','z', varName))
##
##for filename in os.listdir(directory):
##    if filename.endswith('.nc'):
##        filepath = os.path.join(directory, filename)
##        print(filepath)
##        f = netCDF4.Dataset(filepath,'r')
##        value_array = f.variables[varName][:]
##        for i in xrange(0, len(value_array)):
##            if f.variables[varName][i] > 0:
##                writer.writerow((f.variables['date'][0], f.variables['lat'][0], f.variables['lon'][0], f.variables['z'][i], '{:.20f}'.format(f.variables[varName][i])))
##        f.close()
##    else:
##        continue
##
##out.close()
##print('Done')
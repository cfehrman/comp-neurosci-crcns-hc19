
# CRCNS HC-19 Pre-Processed Data

This repository contains the pre-processed data from the hc-19 dataset on CRCNS.org, and were provided by Davide Ciliberti, Frédéric Michon and Fabian Kloosterman.

## To get the data

The data can be accessed at https://crcns.org/data-sets/hc/hc-19/about-hc-19:

-The only files that are utilized in this repository are the nine pre-processed hdf5 data files.

-If downloading all files from CRCNS, these data will be found in data/PreprocessedDatasets folder.

-Each folder in the PreprocessedDatasets file will have a label beginning with dataset_2017_08_, and in each you will find the needed hdf5 file for that particular run or day.

-The hdf5 files of the same day, all have the same name (i.e. the prerun, sleep, and postrun hdf5 files for August 23rd are all named 2017-08-23_09-42-01.hdf5).

-The script to turn the data into a dict assume that these data files have been renamed with -prerun,-sleep,or -postrun added to the end of the name (e.g. 2017-08-23_09-42-01-postrun.hdf5).


## To process the data

To process the hdf5 files, first run the script in src/kloosterman_function.py:

-This function was developed by Fabian Kloosterman and is available on the bitbucket repository Ciliberti Elife2018 RealTimeReplay, with links and detailed description of location in the CRCNS hc-19 repository.
 
-This script will create the read_dataset function which reads the hdf5 files in python.

To put the desired data into a dictonary, use the function in the src/io.py folder. This function allows you to select a partition of the data to analyze:

- "all" puts all nine files into a dictionary ordered by day and level of run (i.e. pre, sleep, post)
- "day1" puts the three pre, sleep, post files of August 23rd in a dictionary
- "day2" puts the three pre, sleep, post files of August 24th in a dictionary
- "day3" puts the three pre, sleep, post files of August 25th in a dictionary
- "prerun" puts the three preruns files from August 23rd-25th in a dictionary
- "sleep" puts the three sleep files from August 23rd-25th in a dictionary
- "postrun" puts the three postrun files from August 23rd-25th in a dictionary

-The function also defaults to using the read_dataset function on all nine of the hdf5 files. Note to change the file path in the function.

## Spike Detection

-Run the script in the src/burstdetection.py folder. This script will run replicate our analyses for the final project, which examines the data from the second run (RUN 2) from the first tetrode on 08/23/2017. The script produces the following output: A plot of the waveform of the first electrode for RUN 2 on 08/23/2017, a raster plot of the spikes produced during the run (with a threshold rate of 60 microvolts, and the calculated number of spikes for that run.


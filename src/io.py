def read_data(partition, read=True):
    """This function takes a partition argument of: all, day 1, day 2, day 3, prerun, sleep, postrun"""
    """This function takes a read argument of TRUE or FALSE. If TRUE, the hdf5 files are read using read_dataset"""
    if(read==True):
    #Reads all of the hdf5 files, note to change the file path
        first_23=read_dataset('data/unzippedfiles/2017-08-23_09-42-01-prerun.hdf5')
        rest_23=read_dataset('data/unzippedfiles/2017-08-23_09-42-01-sleep.hdf5')
        second_23=read_dataset('data/unzippedfiles/2017-08-23_09-42-01-postrun.hdf5')
        first_24=read_dataset('data/unzippedfiles/2017-08-24_09-36-44-prerun.hdf5')
        rest_24=read_dataset('data/unzippedfiles/2017-08-24_09-36-44-sleep.hdf5')
        second_24=read_dataset('data/unzippedfiles/2017-08-24_09-36-44-postrun.hdf5')
        first_25=read_dataset('data/unzippedfiles/2017-08-25_09-50-43-prerun.hdf5')
        rest_25=read_dataset('data/unzippedfiles/2017-08-25_09-50-43-sleep.hdf5')
        second_25=read_dataset('data/unzippedfiles/2017-08-25_09-50-43-postrun.hdf5')
    #Creates a dict out according to partition argument
    partition=partition.lower()
    if (partition == "all"):
        Day1={'first run':first_23[1],
              'rest':rest_23[1],
              'second run':second_23[1]}
        Day2={'first run':first_24[1],
              'rest':rest_24[1],
              'second run':second_24[1]}
        Day3={'first run':first_25[1],
              'rest':rest_25[1],
              'second run':second_25[1]}
        neuron_dict_all={'Day':{'08/23/2017':Day1,
                                '08/24/2017':Day2,
                                '08/25/2017':Day3}}
        return(neuron_dict_all)
    elif (partition == "day1"):
        neuron_dict_day1={'first run':first_23[1],
                          'rest':rest_23[1],
                          'second run':second_23[1]}
        return(neuron_dict_day1)
    elif (partition == "day2"):
        neuron_dict_day2={'first run':first_24[1],
                          'rest':rest_24[1],
                          'second run':second_24[1]}
        return(neuron_dict_day2)
    elif (partition == "day3"):
        neuron_dict_day3={'first run':first_25[1],
                          'rest':rest_25[1],
                          'second run':second_25[1]}
        return(neuron_dict_day3)
    elif (partition == "prerun"):
        neuron_dict_prerun={'Day1':first_23[1],
                            'Day2':first_24[1],
                            'Day3':first_25[1]}
        return(neuron_dict_prerun)
    elif (partition == "sleep"):
        neuron_dict_rest={'Day1':rest_23[1],
                           'Day2':rest_24[1],
                           'Day3':rest_25[1]}
        return(neuron_dict_rest)
    elif (partition == "postrun"):
        neuron_dict_postrun={'Day1':second_23[1],
                             'Day2':second_24[1],
                             'Day3':second_25[1]}
        return(neuron_dict_postrun)
    else:
        print("Incorrect argument. Try: all, day1, day2, day3, prerun, sleep, postrun")
          
        
#Import Libraries
import pandas as pd
from pandas import Series
from matplotlib import pyplot as plt
import matplotlib.patches as mp
import numpy as np
import scipy as sp
import scipy.signal

#Read data into dictionary
data=read_data(partition="all",read=True)

#Get data for the first tetrode on the second run on 08/23/2017
time = data['Day']['08/23/2017']['second run']['TT1']['spike_times']
amp = data['Day']['08/23/2017']['second run']['TT1']['spike_amplitudes']
e1=[i[0] for i in amp] #Electrode 1
e2=[i[1] for i in amp] #Electrode 2
e3=[i[2] for i in amp] #Electrode 3
e4=[i[3] for i in amp] #Electrode 4
tet=[np.mean(i) for i in amp] #Mean Tetrode Activity

#Electrode 1 Waveform
plt.plot(time,e1)
plt.axhline(y=60, color='r',linestyle='-')
red_patch = mp.Patch(color='red', label='Spike Threshold of 60 $\mu$V')
plt.legend(handles=[red_patch])
plt.title('Waveform of Electrode 1')
plt.ylabel('$\mu$V')
plt.xlabel('Time (ms)')
plt.show()
                                            
#Spike Detection for Electrode 1

spikedict={'times':time,'amplitude':e1} 
spikedf=pd.DataFrame(spikedict,columns=["times","amplitude"])

peaks=scipy.signal.find_peaks(spikedf['amplitude'], height=60) #Gets peaks of data using a threshold of 60 uV
peaktimes=peaks[0]                                             #Gets indicies of when there was an action potential (AP)
peaktimes=peaktimes.tolist()                   
spikedata=spikedf.iloc[peaktimes]                              #Gets time and amplitude data for each AP

#Raster plot of Electrode 1
plt.eventplot(peaktimes)
plt.title('Raster Plot of Electrode 1')
plt.xlabel('Time (ms); Scaled to $t_0$ = 0ms')
plt.show()

#Burst Detection using the Mean Inter-Spike Interval Method
t=spikedata['times'].tolist() 
ISI=[]
for n in range(1,len(t)):
    ISI.append(t[n]-t[n-1])

mISI=np.mean(ISI) #Calculates the Mean Inter-Spike Interval

spikeISI=spikedata.drop(spikedata.index[0]) #Drops first spike since it is not used in calculation

spikeISI['ISI']=ISI #Creates a column of the interspike interval for each AP

spikeISI['L(n)'] = spikeISI['ISI'].apply(lambda x: 'less' if x <= mISI else 'greater') #Finds the ISIs less than the mean ISI

meanLn=np.mean(spikeISI[(spikeISI['L(n)'])=='less']['ISI']) #Calulates the mean of the L(n)s

spikeISI['Mean L(n)'] =  spikeISI['ISI'].apply(lambda x: 1 if x <= meanLn else 0) #Finds the ISIs less than the mean L(n)

#Count Bursts: Bursts are defined as two or more successive ISIs that are less than the mean L(n).

spikeI=spikeISI['Mean L(n)'].values #Makes a list of 1s (<= mean L(n)) and 0s (> mean L(n))

z =0 #Counter for sequentially appearing 1s.
arr=[] #Array for storing ISIs in a single burst
for i in range(0,len(spikeI)):
    if spikeI[i]==1:
        z=z+1
    if spikeI[i]==0:
        arr.append(z)
        z = 0
    if i==len(spikeI)-1:   
        arr.append(z)

bursts = 0 #Counter for number of bursts
for i in range(len(arr)):
    if arr[i]>1:
        bursts = bursts+1
print("Number of bursts detected:",bursts)





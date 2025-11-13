import h5py
import numpy as np
import pandas as pd
import csv


input_filename = "E:\\Education\\Work\\DEP\\C++\\20210504\\HDFread\\Input\\dset.h5"
output_filename= "E:\\Education\\Work\\DEP\\C++\\20210504\\HDFread\\Input\\dset.csv"


def reading_hdf5_file():
  if(input_filename!=None):
   inputfile = h5py.File(input_filename, 'r')
# List all groups
   a_group_key = list(inputfile.keys())[0] #[0] is encode value
# Get the data
   data = list(inputfile[a_group_key])
   outputfile=open(output_filename,'w',newline='')

   #splitting the data
   splitted_data = []
   col = []
   for i in range(0, len(data[0].dtype.names)):
       col.append(data[0].dtype.names[i])
   splitted_data.append(col)
   for i in range(0,len(data)):
       col = []
       for j in range(0, len(data[0].dtype.names)):
           if (data[i].dtype[j] == 'O') : 
               col.append(str(data[i][j], 'utf-8'))
           else : 
               col.append(data[i][j])
       splitted_data.append(col)
       
   with  outputfile:
    write = csv.writer(outputfile)
    write.writerows(splitted_data)
    print("convertion completed..")
  else:print("check the inputfile..")
#main function    
def main():
    reading_hdf5_file()
    
if __name__ == "__main__":
    main()



#splitdata = []
    #for i in range (0, len(outputdata)) : splitdata.append(outputdata[i].split())
    #print(splitdata)
  
#Keys: <KeysViewHDF5 ['dd48']>


'''
pd.concat(
pd.DataFrame(data = 

  data
  for i in range (0,len(data)):
      outputdata.append(data[i])

'''

#import pandas as pd
#df = pd.read_hdf("E:\\Education\\Work\\DEP\\Python\\HDF5\\test.h5")
#df.to_csv(sys.stdout, index=False)
import sys
import h5py
import numpy as np

input_filename = "E:\\Education\\Work\\DEP\\Python\\HDF5\\test.h5"
inputfile = h5py.File(input_filename, 'r')
a_group_key = list(inputfile.keys())[0]
np.savetxt(sys.stdout, h5py.File("E:\\Education\\Work\\DEP\\Python\\HDF5\\test.h5")['data', 'classes'], a_group_key, ',')

import numpy as np
import h5py

with h5py.File("E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2CSV\\test.h5",'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
### This lists arrays in the file [u'_self_key', u'chrms1', u'chrms2', u'cuts1', u'cuts2', u'misc', u'strands1', u'strands2']

r1 = h5py.File("E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2CSV\\test.h5",'r')
for rows in r1:
  table=np.array(rows)
#a = r1['chrms1'][:]
#b = r1['chrms2'][:]
#c = r1['cuts1'][:]
#d = r1['cuts2'][:]
#e = r1['strands1'][:]
#f = r1['strands2'][:]
r1.close()
#table=np.array([a,b,c,d,e,f])
#table2=table.transpose()
np.savetxt("E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2CSV\\test.csv",table,delimiter=',')

import pandas as pd
import h5py
def  hdf5_to_csv():
  with pd.HDFStore("E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2CSV\\test.h5",'r') as d:
   df = d.get('TheData')
df.to_csv("E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2CSV\\test.csv")
def main():
  hdf5_to_csv()
if __name__ == "__main__":
    main()

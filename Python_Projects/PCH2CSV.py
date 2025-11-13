import numpy as np
infilename="E:\\C\\WS\\Python_Projects\\TestCases\\Input\\example_1.pch"
outfilename="E:\C\WS\Python_Projects\TestCases\Output\example_1_output.csv"

#Header data
array=np.array(['Point ID', 'Frequency', 'X', 'Y', 'Z'], dtype='object')

#opening/creating csv file in append mode
outfile=open(outfilename, 'w')

#opening pch in read mode
infile=open(infilename, 'r')
#start reading the file
line=infile.readline()

while line:                                     #Loop-1: To loop the process till last line of file
    if line.find("$POINT ID") != -1:
        data = line.split()
        PID = data[3]
        line=infile.readline()
        while line.find("$TITLE") == -1 :        #Loop-2: To loop the process till next point reference ID
            if line.find("-CONT-") == -1 :
                if line!='' :                   #To check if line empty
                    data = line.split()
                    Freq = data[0]
                    x = data[2]
                    y = data[3]
                    z = data[4]
                    arr = np.array([PID, Freq, x, y, z], dtype='object')
                    print(arr)
                    array = np.vstack((array, arr))
                    outfile.write("\n")
                line=infile.readline()
                if not line : break             #To break the Loop-2 if reached the last line
            else : line=infile.readline()       #To skip continuation lines of a frequency
    else : line=infile.readline()               #To skip the titles above a point reference ID

#closing both input and output files
infile.close
outfile.close


if np.savetxt(outfilename, array, delimiter=",", fmt='%s', newline='\n') != 1:
    print("File conversion complete.")
else :
    print("Error converting the file.")

print("Program complete.")

'''
#clear contents of file if file already exists
if os.path.isfile(outfilename): 
    outfile.truncate(0)

arr=np.array(['Point ID', 'Frequency', 'X', 'Y', 'Z'], dtype='object')
arr.tofile(outfile, sep=',', format='%s')
outfile.write("\n")
#array=np.array(len(arr), dtype='object')
array = np.vstack((array, arr))

#arr.tofile(outfile, sep=',', format='%s')

path, filename = os.path.split(infilename)
output_path = os.path.dirname(path)
file_name, file_extension = os.path.splitext(filename)
outfilename = os.path.join(output_path, 'output/'+ file_name + "_conv" + "." + 'csv')

'''
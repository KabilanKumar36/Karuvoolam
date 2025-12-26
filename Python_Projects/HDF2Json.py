import json
import h5py
import numpy as np

def nptypeof(typeinfo, listdata):
    #dt_str = h5py.special_dtype(vlen=np.dtype('uint8'))   #vlen=str #np.dtype('uint8')
    if(typeinfo == type(None)): return type(None)
    elif(typeinfo == bool): return '?'
    elif(typeinfo == int): return 'i'
    elif(typeinfo == str): return 'S'
    elif(typeinfo == list):
        for i in range(0, len(listdata)):
            typetuple = (listdata[i], nptypeof(type(listdata[i]), listdata[i]))
        return typetuple[1]
    elif(typeinfo == dict):
        localkeys = ([key.split(',')[0] for key in listdata.keys()])
        line = []
        for i in range(0, len(localkeys)):
            line.append((localkeys[i], nptypeof(type(listdata[localkeys[i]]), listdata[localkeys[i]])))
        datasubtype = np.dtype([(localkeys[i], nptypeof(type(listdata[localkeys[i]]), listdata[localkeys[i]])) for i in range(0, len(localkeys))])
        return datasubtype

    
def list_to_hdf(string, hf, data):
    valuelist = []
    newcount = 0
    for array in data:
        newcount += 1
        keys, values = zip(*array.items())
        if(newcount <= 1):
            valuelist.append(keys)
        valuelist.append(values)
    if(len(valuelist) > 0):
        header = valuelist[0]
        col_count = len(header)
        row_count = 0
        for row in valuelist:
            if(row_count > 0):
                assert len(row) == col_count
                col_types = list(map(type, [value for value in row]))
            row_count += 1

    datatype = np.dtype([(valuelist[0][i], nptypeof(col_types[i], valuelist[1][i])) for i in range(0, col_count)])

    nplist = np.empty((row_count-1,), dtype=datatype)
   
    row_index = 0
    list_count = 0
    dict_count = 0
    for row in valuelist:
        if (row_index>0):
            for j in range(0, col_count):
                if(col_types[j] == str):
                    nplist[row_index-1][j] = row[j].encode('utf8')
                elif(col_types[j] == list):
                   local_list = list_to_hdf(header[j], hf, row[j])
                   if(local_list.size < 2):
                       nplist[row_index-1][j] = local_list
                   else:
                       nplist[row_index-1][j] = local_list[0]
                       #nplist[row_index-1][j] = np.concatenate([np.expand_dims(data, axis = -1)] for data in [nplist[row_index-1][j], local_list[1]])
                       #for k in range(1, local_list.size):
                           #nplist[row_index-1][j] = np.concatenate([np.expand_dims(local_list[k], axis = 0)])
                elif(col_types[j] == dict):
                    localkeys = ([key.split(',')[0] for key in row[j].keys()])
                    local_dict = localdict_to_hdf(hf, localkeys, row[j])
                    for k in range(0, len(list(local_dict))):
                        nplist[row_index-1][j][k] = list(local_dict)[k]
                else:
                    nplist[row_index-1][j] = row[j]
        row_index += 1
    x = 0
    return nplist

def localdict_to_hdf(data, title, hf):
    localkeys = ([key.split(',')[0] for key in data.keys()])
    localdict = np.empty([0,0])
    dataset_count = 0
    dt_str = h5py.special_dtype(vlen=str)
    for i in localkeys:
        if(isinstance(data[str(i)], int)):  localdict = np.append(localdict, data[str(i)])
        elif(isinstance(data[str(i)], str)):
            string = data[str(i)].encode('utf8') #utf8
            localdict = np.append(localdict, string)
        elif(isinstance(data[str(i)], list)):   #list_to_hdf(str(i), hf, data[str(i)])
            nparray = list_to_hdf(str(i), hf, data[str(i)])
            localdict = np.array(localdict, nparray)
        elif(isinstance(data[str(i)], dict)):
            localkeys = ([key.split(',')[0] for key in data[str(i)].keys()])
            dict = localdict_to_hdf(hf, localkeys, data[str(i)])
            localdict = np.array(localdict, dict)
        else: print("Data type of data set ", str(i)," is unknown.")
        dataset_count += 1
    if(dataset_count>0):
        print("Total ", dataset_count, " datasets were found in local dictionary '", title, "'.")
    return localdict


def dict_to_hdf(data, hf):
    majorkeys = ([key.split(',')[0] for key in data.keys()])
    dataset_count = 0
    for i in majorkeys:
        if(isinstance(data[str(i)], int)):      hdf5_table = hf.create_dataset(str(i), data=data[str(i)])
        elif(isinstance(data[str(i)], str)):    hdf5_table = hf.create_dataset(str(i), data=data[str(i)])
        elif(isinstance(data[str(i)], list)):   
            nplist = list_to_hdf(str(i), hf, data[str(i)])
            hdf5_table = hf.create_dataset(str(i), data=nplist)
        elif(isinstance(data[str(i)], dict)):
            #hdf5_grp = hf.create_group(str(i))
            #dict_to_hdf(data[str(i)], hdf5_grp)
            localdict = localdict_to_hdf(data[str(i)], str(i), hf)
            hdf5_table = hf.create_dataset(str(i), data=localdict)
        else: print("Data type of data set ", str(i)," is unknown.")
        dataset_count += 1

    print("Total ", dataset_count, " datasets were found in the parent dataset .")

def print_stat(stat):
    print(stat)

def json_to_hdf(input_file, output_file):
    input_json = open(input_file, encoding='utf-8')
    output_HDF = h5py.File(output_file, 'w')
    stat = []
    input_data = json.load(input_json)

    if(isinstance(input_data, int)):      hdf5_table = hf.create_dataset(str(i), data=data[str(i)])
    elif(isinstance(input_data, str)):    hdf5_table = hf.create_dataset(str(i), data=data[str(i)])
    elif(isinstance(input_data, dict)):   dict_to_hdf(input_data, output_HDF)
    elif(isinstance(input_data, list)):   list_to_hdf(input_data, output_HDF)

    output_HDF.close()
    if (len(stat)>0): print_stat(stat)
    print("Conversion complete...")

def main():
    input_file = "E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2Json\\Input\\Json\\jsonfilewithhierarchy-100.json"
    #jsonfilewithhierarchy-100
    #sample2
    #example_2
    output_file = "E:\\Education\\Work\\DEP\\Python\\HDF5\\HDF2Json\\Output\\HDF\\jsonfilewithhierarchy-100.h5"

    json_to_hdf(input_file, output_file)

if __name__ == "__main__":
    main()

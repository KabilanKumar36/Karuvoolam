import os
import meshio

input_vtk_file = "E:\\C\\WS\\Python_Projects\\TestCases\\Input\\maillage.vtu"
current_dir = "E:\\C\\WS\\Python_Projects\\TestCases\\Output"
solver_template = "Nastran"


mesh = meshio.read(input_vtk_file)

def writepointdatafile(filepath):    
    output_point_file_path = filepath
    output_points_file = open(output_point_file_path, 'w')
    count = 1
    for points in mesh.points:
        x_coordinate = str(points[0])
        y_coordinate = str(points[1])
        z_coordinate = str(points[2])
        output_points_file.write("GRID,"+str(count)+","+x_coordinate+","+y_coordinate+","+z_coordinate+"\n")
        count += 1
    output_points_file.close()
    
def writehexaelementdatafile(filepath):
    output_point_file_path = filepath
    output_points_file = open(output_point_file_path, 'w')
    count = 1

    for item in mesh.cells:
       if(item.type == "hexahedron"):
        for hexa in item.data:
            nodeID1 = str(hexa[0]+1)
            nodeID2 = str(hexa[1]+1)
            nodeID3 = str(hexa[2]+1)
            nodeID4 = str(hexa[3]+1)
            nodeID5 = str(hexa[4]+1)
            nodeID6 = str(hexa[5]+1)
            nodeID7 = str(hexa[6]+1)
            nodeID8 = str(hexa[7]+1)
            output_points_file.write("HEXA,"+str(count)+","+nodeID1+","+nodeID2+","+nodeID3+","+nodeID4+","+nodeID5+","+nodeID6+","+nodeID7+","+nodeID8+"\n")
            count = count+1
        
    output_points_file.close()

def deletefile(filepath):
    os.remove(filepath)

#Write point data
pt_data_path = current_dir+"\point.csv"
writepointdatafile(pt_data_path)
#write element data
elem_data_path = current_dir+"\hexa.csv"
writehexaelementdatafile(elem_data_path)
bdf_path = current_dir+"\output.bdf"
meshio.write(bdf_path, mesh);
#execute
#mwlib.Execute("command=read_csv,input_file="+pt_data_path+",entity_type=nodes,template="+solver_template+"")
#mwlib.Execute("command=read_csv,input_file="+elem_data_path+",entity_type=elements")




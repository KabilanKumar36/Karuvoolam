import csv
with open("E:\\C\\WS\\Python_Projects\\TestCases\\data - Original.csv", 'r') as f:
    reader = csv.reader(f)
    with open("E:\\C\\WS\\Python_Projects\\TestCases\\Output file.csv", 'w' , newline='\r\n') as l:
        Writer=csv.writer(l)
        for row in reader:
            Writer.writerows(row[0])
        #for row in reader:
       #print(row[0])


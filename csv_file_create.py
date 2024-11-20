
import csv
data = [
    ["Name", "Salary", "Designation", "Department", "Location"],
    ["Alice", 70000, "Software Engineer", "IT", "New York"],
    ["Bob", 85000, "Data Scientist", "Data", "San Francisco"],
    ["Charlie", 60000, "System Administrator", "IT", "Chicago"],
    ["David", 95000, "Product Manager", "Product", "Boston"],
    ["Eve", 72000, "UX Designer", "Design", "Los Angeles"]
]

with open("new_file.csv","w") as csvFile:
    csv_file = csv.reader(csvFile)
    csv_file.writerows(data)
    print("createed")



#csv file theke list convert

import csv
data=[]
with open ("new_file.csv","r")as file:
    content = csv.reader(file)
    for item in content:
        data.append(item)

print(data)        
    

import json
def write_file(main_json_dictionary):
    with open('employee_info.txt','w') as myfile:
        json.dump(main_json_dictionary,myfile)
def read_file():
    with open('employee_info.txt') as myfile1:
        empDataFile = json.load(myfile1)
    print(empDataFile)        
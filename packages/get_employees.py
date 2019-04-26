def get_employee(emp_ids,emp_info):
    get_emp_id = input("Enter the employee id or press 'a' to get all employees list")
    if get_emp_id == 'a':
        for ids,values in emp_info.items():
            print("Employee ",ids," details: ",values)
    else:
        if get_emp_id in emp_ids:
            print(emp_info[get_emp_id])
        else:
            print("No employee exist with that id.")             
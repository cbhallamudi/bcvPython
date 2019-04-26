def add_employee(emp_ids,emp_info):
    new_emp_id = input("Enter new employee id")
    if new_emp_id in emp_ids:
        print("Member already exists with the same id")
        # return False
    else:
        emp_ids.add(new_emp_id)
        new_emp_name = input("Enter new employee name")
        new_emp_designation = input("Enter new employee designation")
        emp_info[new_emp_id] = {'emp_name':new_emp_name,'emp_designation':new_emp_designation} 
        # return True       
import packages.add_employee as ae
import packages.get_employees as ge
import packages.add_to_game as atg
import packages.fetch_games_info as fgi
import json
emp_ids = {'e1','e2','e3'}
game_ids = {'ch','ca'}
emp_info = {
    'e1':{'name':'Chaitanya','emp_designation':'Junior Software Engineer'},
    'e2':{'name':'Rajeswari','emp_designation':'School Assistant'},
    'e3':{'name':'Bhavani','emp_designation':'Record Assistant'}
}
emp_games = {
    'chess':{'e1','e2'},
    'carroms':{'e3','e1'}
}

emp_games_dict = {}
for game in emp_games:
    emp_games_dict[game] = list(emp_games[game])

main_json_dictionary = {
    'emp_ids':list(emp_ids),
    'game_ids':list(game_ids),
    'emp_info':emp_info,
    'emp_games':emp_games_dict
}    


# while True:
#     get_action_id = input("Press 'addemp' to add employee \n Press 'getemp' to get employee \n Press 'add2game' to add employee to game \n Press 'fetgame' to fetch game info \n any 't' to terminate \n Enter your choice:  ")
#     if get_action_id == 'addemp':
#         ae.add_employee(emp_ids,emp_info)
#     elif get_action_id == 'getemp':
#         ge.get_employee(emp_ids,emp_info)
#     elif get_action_id == 'add2game':
#         atg.emp_game_subscription(emp_ids,emp_info,game_ids,emp_games)    
#     elif get_action_id == 'fetgame':
#         fgi.fet_game_info(emp_ids,emp_info,game_ids,emp_games)
#     elif get_action_id == 't':
#         break



# with open('employee_info.txt','w') as myfile:
#     json.dump(main_json_dictionary,myfile)
# with open('employee_info.txt') as myfile1:
#     empDataFile = json.load(myfile1)
# print(empDataFile)    

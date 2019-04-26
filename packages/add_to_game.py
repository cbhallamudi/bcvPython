def emp_game_subscription(emp_ids,emp_info,game_ids,emp_games):
    check_if_exists = input("Enter employee id to add to game: ")
    if check_if_exists in emp_ids:
        get_game_id = input("Enter the game the employee wants to subscribe: 'ch' for Chess or 'ca' for carroms -> ")
        if get_game_id in game_ids:
            if get_game_id == 'ch':
                if check_if_exists in emp_games['chess']:
                    print("Employee already exists in this group")
                else:
                    emp_games['chess'].add(check_if_exists)
                    print("Employee successfully subscribed to Chess")
            elif get_game_id == 'ca':
                if check_if_exists in emp_games['carroms']:
                    print("Employee already exists in this group")
                else:
                    emp_games['carroms'].add(check_if_exists)
                    print("Employee successfully subscribed to Carroms")
        else:
            print("The game you have selected doesn't exists")
    else:
        print("Employee doesn't exist")                            
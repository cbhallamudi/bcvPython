def fet_game_info(emp_ids,emp_info,game_ids,emp_games):
    get_game_id = input("Enter the game id: 'ch' for chess or 'ca' for carroms or 'a' for all games -> ")
    if get_game_id in game_ids:
        if get_game_id == 'ch':
            for game in emp_games['chess']:
                print(emp_info[game]['name'])
        elif get_game_id == 'ca':
            for game in emp_games['carroms']:
                print(emp_info[game]['name'])
    elif get_game_id == 'a':
        for myKey,games in emp_games.items():
            print(myKey,": \n")
            for gameDetails in games:    
                print(emp_info[gameDetails])
            print("--------------------")        
    else:
        print("We dont have that game")            
            
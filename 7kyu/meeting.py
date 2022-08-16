def meeting(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return 'None available!'


meeting(['X', 'X', 'O', 'X', 'X'])
meeting(['O', 'X', 'X', 'X', 'X'])
meeting(['X', 'O', 'X'])

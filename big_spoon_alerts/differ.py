def diff(current_menu, previous_menu):
    # compare and get new in current and removed from current
    dropped_flavors = []
    new_flavors = []
    for previous_flavor in previous_menu:
        present = False
        for current_flavor in current_menu:
            if(previous_flavor['name']==current_flavor['name']):
                present = True
        if(not present):
            dropped_flavors.append(previous_flavor)

    for current_flavor in current_menu:
        present = False
        for previous_flavor in previous_menu:
            if(previous_flavor['name']==current_flavor['name']):
                present = True
        if(not present):
            new_flavors.append(current_flavor)

    return {
        "new": new_flavors,
        "dropped": dropped_flavors
    }
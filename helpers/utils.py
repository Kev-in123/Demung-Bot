import json


async def get_users():
    with open('levels.json', 'r') as f:
        users = json.load(f)
    return users


async def start(user):
    users = await get_users()
    user = str(user)
    if user in users:
        return
    else:
        users[user] = {'xp': 0, 'lvl': 0, 'last_xp': 0, 'blacklisted': False}

    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)


async def add_xp(user, amt):
    user = str(user)
    await start(user)
    users = await get_users()
    users[user]['xp'] += amt
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)


async def remove_xp(user, amt):
    user = str(user)
    await start(user)
    users = await get_users()
    users[user]['xp'] -= amt
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)


async def lvl_inc(user, amt):
    user = str(user)
    await start(user)
    users = await get_users()
    users[user]['lvl'] += amt
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)


async def lvl_dinc(user, amt):
    user = str(user)
    await start(user)
    users = await get_users()
    users[user]['lvl'] -= amt
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)


async def lvl_up(user):
    user = str(user)
    await start(user)
    users = await get_users()
    user_lvl = users[user]['lvl']
    user_xp = users[user]['xp']
    last_xp = users[user]['last_xp']
    
    users[user]['last_xp'] = users[user]['xp']
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)
      
    if user_xp >= 5 * (user_lvl ** 2) + (50 * user_lvl) + 100 + last_xp:
        await lvl_inc(user, 1)
        return True
    return False


async def get_xp(user):
    user = str(user)
    await start(user)
    users = await get_users()
    return users[user]['xp']


async def get_lvl(user):
    user = str(user)
    await start(user)
    users = await get_users()
    return users[user]['lvl']


async def blacklist(user):
    user = str(user)
    await start(user)
    users = await get_users()
    users[user]['blacklisted'] = True
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)
    return True


async def unblacklist(user):
    user = str(user)
    await start(user)
    users = await get_users()
    users[user]['blacklisted'] = False
    with open('levels.json', 'w') as f:
        json.dump(users, f, sort_keys=True, indent=4)
    return True

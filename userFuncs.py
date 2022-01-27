import json
import random
import re


def showBal(userId):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    inList = False
    for i in json_object['users']:
        if i["id"] == userId:
            inList = True
            if i['balance'] == 0:
                return "Sorry bro.... your broke..."
            else:
                return f"You have ${i['balance']}"
    if inList == False:
        json_object['users'].append(
            {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        return "You have $100"


def showBank(userId):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    inList = False
    for i in json_object['users']:
        if i["id"] == userId:
            inList = True
            if i['bank'] == 0:
                return "Sorry bro.... your broke... or risking too much 😶"
            else:
                return f"You have ${i['bank']} in the bank"
    if inList == False:
        json_object['users'].append(
            {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        return "You have no money in the bank"


def showInventory(userId):
    val = "Your inventory contains:\n"
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    inList = False
    for i in json_object['users']:
        if i["id"] == userId:
            inList = True
            if len(i['inventory']) == 0:
                return "Sorry, your inventory is empty..."
            else:
                for j in i['inventory']:
                    val += f'{j[0]}:{j[1]}\n'
            break

    if inList == False:
        json_object['users'].append(
            {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        return "Sorry, your inventory is empty..."
    else:
        return val


def showVault(userId):
    val = "Your vault contains:\n"
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    inList = False
    for i in json_object['users']:
        if i["id"] == userId:
            inList = True
            if len(i['vault']) == 0:
                return "Sorry, your vault is empty..."
            else:
                for j in i['vault']:
                    val += f'{j[0]}:{j[1]}\n'
            val += f"And has a capacity of {i['vaultCap']}"
            break

    if inList == False:
        json_object['users'].append(
            {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        return "Sorry, your inventory is empty..."
    else:
        return val


def newItem(userId, item, count):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    inList = False
    for i in json_object['users']:
        if i["id"] == userId:
            inList = True
            break
    if inList == False:
        json_object['users'].append(
            {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
    for i in json_object['users']:
        if i["id"] == userId:
            hasItem = False
            for j in i['inventory']:
                if j[0] == item:
                    hasItem = True
                    j[1] += count
                    break
            if not hasItem:
                i["inventory"].append((item, count))
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def death(userId):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    inList = False
    for i in json_object['users']:
        if i["id"] == userId:
            inList = True
            break
    if inList == False:
        json_object["users"].append(
            {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})

    for i in json_object['users']:
        if i["id"] == userId:
            i["inventory"] = []
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def vault(userId, item, amount: str):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    if amount.isdigit():
        amount = int(amount)
        inList = False
        for i in json_object['users']:
            if i["id"] == userId:
                inList = True
                break
        if inList == False:
            json_object["users"].append(
                {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
            return "Sorry, your inventory is empty."
        else:
            hasItem = False
            for i in json_object['users']:
                if i['id'] == userId:
                    for j in i["inventory"]:
                        if j[0] == item:
                            hasItem = True
                            break
                    if hasItem == False:
                        return f"You don't have any {item} in your inventory."
                    elif amount > i['vaultCap']:
                        return f"You only have enough space for {i['vaultCap']} items in your vault."
                    else:
                        if hasItem:
                            for j in i["inventory"]:
                                if j[0] == item:
                                    if amount > j[1]:
                                        return f'You only have {j[1]} {j[0]}'
                                    elif amount == j[1]:
                                        inVault = False
                                        for x in i['vault']:
                                            if x[0] == item:
                                                x[1] += amount
                                                inVault = True
                                                break
                                        if inVault == False:
                                            i['vault'].append(j)
                                        i['inventory'].remove(j)
                                        i['vaultCap'] -= amount
                                    else:
                                        inVault = False
                                        for x in i['vault']:
                                            if x[0] == item:
                                                x[1] += amount
                                                inVault = True
                                                break
                                        if inVault == False:
                                            i['vault'].append([j[0], amount])
                                        j[1] -= amount
                                        i['vaultCap'] -= amount
                                    break
                    break

    else:
        if amount.lower() == 'all':
            hasItem = False
            for i in json_object['users']:
                if i['id'] == userId:
                    for j in i["inventory"]:
                        if j[0] == item:
                            hasItem = True
                            break
                    if hasItem == False:
                        return f"You don't have any {item} in your inventory."
                    else:
                        for j in i['inventory']:
                            if j[0] == item:
                                if j[1] > i['vaultCap']:
                                    return f"You only have enough space for {i['vaultCap']} items in your vault."
                                else:
                                    inVault = False
                                    for x in i['vault']:
                                        if x[0] == item:
                                            x[1] += j[1]
                                            inVault = True
                                            break
                                    if inVault == False:
                                        i['vault'].append(j)
                                    i['inventory'].remove(j)
                                    i['vaultCap'] -= j[1]
                                break
                    break

        else:
            return "Please specify a valid number of items to vault, or use the 'all' keyword to vault everythinig u have of a certain block."
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def unvault(userId, item, amount):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    if amount.isdigit():
        amount = int(amount)
        inList = False
        for i in json_object['users']:
            if i["id"] == userId:
                inList = True
                break
        if inList == False:
            json_object["users"].append(
                {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
            return "Sorry, your inventory is empty."
        else:
            for i in json_object['users']:
                if i['id'] == userId:
                    hasItem = False
                    for j in i['vault']:
                        if j[0] == item:
                            hasItem = True
                            break
                    if hasItem == False:
                        return f"You don't have any {item} in your vault"
                    else:
                        for j in i['vault']:
                            if j[0] == item:
                                if amount > j[1]:
                                    return f'You only have {j[1]} {item} in your vault'
                                else:
                                    inInv = False
                                    for x in i['inventory']:
                                        if x[0] == item:
                                            inInv = True
                                            x[1] += amount
                                            i['vaultCap'] += amount
                                            if amount == j[1]:
                                                i['vault'].remove(j)
                                            else:
                                                j[1] -= amount
                                            break
                                    if inInv == False:
                                        i['inventory'].append([j[0], amount])
                                        i['vaultCap'] += amount
                                        if amount == j[1]:
                                            i['vault'].remove(j)
                                        else:
                                            j[1] -= amount
                                break
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def sell(userId, item, amount):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    prices = {'diamond': 20, 'emerald': 20, 'gold': 15,
              'cobblestone': 0, 'gravel': 0, 'iron': 5, 'platinum': 10000}
    if item not in prices:
        return "That is not a sellable item"
    else:
        if amount.isdigit():
            amount = int(amount)
            inList = False
            for i in json_object['users']:
                if i["id"] == userId:
                    inList = True
                    break
            if inList == False:
                json_object["users"].append(
                    {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
                return "Sorry, your inventory is empty."
            else:
                hasItem = False
                for i in json_object['users']:
                    if i['id'] == userId:
                        for j in i['inventory']:
                            if j[0] == item:
                                hasItem = True
                                break
                        if hasItem == False:
                            return f'You dont have any {item} in your inventory.'
                        else:
                            for j in i['inventory']:
                                if j[0] == item:
                                    if amount > j[1]:
                                        return f'You only have {j[1]} {j[0]}'
                                    elif amount == j[1]:
                                        i['balance'] += amount * prices[item]
                                        i['inventory'].remove(j)
                                    else:
                                        i['balance'] += amount * prices[item]
                                        j[1] -= amount
                                    break
                        break
        else:
            return "Please enter a valid amount of items to sell"
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def coinFlip(userId, guess, amount):
    if guess not in ['heads', 'tails']:
        return ["Please gamble on either heads or tails", False]
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    if amount.isdigit():
        amount = int(amount)
        inList = False
        for i in json_object['users']:
            if i["id"] == userId:
                inList = True
                break
        if inList == False:
            json_object["users"].append(
                {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        for i in json_object['users']:
            if i["id"] == userId:
                if amount > i['balance']:
                    return [f"You only have ${i['balance']}", False]
                else:
                    ht = ['heads', 'tails']
                    correct = random.choice(ht)
                    print(f'guess: {guess}\n correct: {correct}')
                    if guess == correct:
                        i['balance'] += amount
                        a_file = open("users.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                        return [f"It landed on {correct}! You won {amount} and now have {i['balance']}", True]
                    else:
                        i['balance'] -= amount
                        a_file = open("users.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                        return [f"It landed on {correct}! You lost {amount} and now have {i['balance']}", True]

    else:
        return ["Please enter a valid whole value of to gamble", False]


def robbery(user1, user2):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    rand = random.uniform(0, 1)
    fList = False
    sList = False
    for i in json_object['users']:
        if i['id'] == user1:
            fList = True
            break
    for i in json_object['users']:
        if i['id'] == user2:
            sList = True
            break
    if fList == False:
        json_object["users"].append(
            {"id": user1, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        fList = True
    if fList and sList:
        if rand >= 0.4:
            for i in json_object['users']:
                if i['id'] == user1:
                    for j in json_object['users']:
                        if j['id'] == user2:
                            amount = random.randint(
                                1, int(j['balance'] // 1.2))
                            j['balance'] -= amount
                            i['balance'] += amount
                            a_file = open("users.json", "w")
                            json.dump(json_object, a_file)
                            return [True, amount]

        else:
            for i in json_object['users']:
                if i['id'] == user1:
                    for j in json_object['users']:
                        if j['id'] == user2:
                            amount = random.randint(
                                1, int(i['balance'] // 1.2))
                            i['balance'] -= amount
                            j['balance'] += amount
                            a_file = open("users.json", "w")
                            json.dump(json_object, a_file)
                            return [False, amount]
    else:
        return "You cant rob someone wtih no balance..."
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def rankings():
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    newlist = sorted(json_object['users'], key=lambda d: d['balance'])
    val = []
    for i in newlist:
        val.append((i['id'], i['balance']))
    return val


def bankHelp(userId, amount):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    if amount.isdigit():
        amount = int(amount)
        inList = False
        for i in json_object['users']:
            if i["id"] == userId:
                inList = True
                break
        if inList == False:
            json_object["users"].append(
                {"id": userId, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        for i in json_object['users']:
            if i['id'] == userId:
                if amount > i['balance']:
                    return f"You only have ${i['balance']}"
                elif amount > i['bankCap']:
                    return f"You only have enough sapce in the bank for another ${i['bankCap']}"
                else:
                    print(f"before: {i['balance']}")
                    i['bank'] += amount
                    i['balance'] -= amount
                    i['bankCap'] -= amount
                    print(f"after: {i['balance']}")
                break
        a_file = open("users.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
    else:
        if amount.lower() == 'all':
            lowerOfTwo = 0
            for i in json_object['users']:
                if i['id'] == userId:
                    lowerOfTwo = str(min(i['balance'], i['bankCap']))
                    bankHelp(userId, lowerOfTwo)

        else:
            return "Please enter a valid amount to send to the bank"


def donate(user1, user2, amount):
    a_file = open("users.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    fList = False
    sList = False
    if amount.isdigit():
        amount = int(amount)
        for i in json_object['users']:
            if i['id'] == user1:
                fList = True
                break
        for i in json_object['users']:
            if i['id'] == user2:
                sList = True
                break
        if fList == False:
            json_object["users"].append(
                {"id": user1, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        if sList == False:
            json_object["users"].append(
                {"id": user2, "balance": 100, 'inventory': [], 'vault': [], 'vaultCap': 20, "bank": 0, "bankCap": 350})
        for i in json_object['users']:
            if i['id'] == user1:
                if amount > i['balance']:
                    return f'Sorry, you only have ${i["balance"]}'
                else:
                    for j in json_object['users']:
                        if j['id'] == user2:
                            j['balance'] += amount
                            i['balance'] -= amount
                            break
                break
    a_file = open("users.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

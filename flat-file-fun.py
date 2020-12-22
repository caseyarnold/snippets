fin = open("data.txt")
users = dict()

def load_data():
    line_number = 0

    for line in fin:
        id, username, password, email = line.split(",")
        line_number += 1
        users[id] = {'username': username.strip(), 'password': password.strip(), 'email': email.strip()}

load_data()

def update_user(id, f, d):
    users[id][f] = d

def insert_user(*args):
    id = str(int(max(users,key=int)) + 1)
    users[id] = {'username': args[0], 'password': args[1], 'email': args[2]}
    return id

def delete_user(id):
    del users[id]

def save():
    line = ""
    writer = open("data.txt", "w")

    for user in users:
        line += str(user) + ","
        for fields in users[user].values():
            line += fields + ","

        line = line[0:-1] + "\n"

    writer.write(line)

print(users)
#save()

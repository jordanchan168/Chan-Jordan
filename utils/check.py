def getUsers():
    a = open("data/users.csv","r")
    list = a.readlines()
    dict = {}
    for user in list:
        entry = user.strip("\n").split(",")
        dict[entry[0]] = entry[1]
    a.close()
    return dict

def addUser(user, pw):
    a = open("data/users.csv","a")
    a.write(str(user)+","+str(pw)+"\n")
    a.close()
    return str(user)+","+str(pw)

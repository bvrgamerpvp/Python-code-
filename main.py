#start
 
users = {}
status = ""
 
def displayMenu():
    status = input("Vc está registrado? s/n? Aperte q para sair")
    if status == "s":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin já existe!\n")
    else:
        createPassw = input("Crie uma senha: ")
        users[createLogin] = createPassw
        print("\nUser criado\n")
 
def oldUser():
    login = input("Enter login name : ")
    passw = input("Enter senha: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()
   
#end

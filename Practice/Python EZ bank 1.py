import basics
app = basics.newProgram()
user= basics.newUser()

app.currentBalance=1000
app.programRunning=True


while app.programRunning==True:
    app.userInput= input("Which would you like to do, 1, Deposit, 2, Withdraw,3,Quit")
    if app.userInput=="1":
        app.userDeposit=input("How much money would you like to deposit")
        app.userDeposit=int(app.userDeposit)
        app.currentBalance+=app.userDeposit
    elif app.userInput=="2":
            app.userWithdraw=input("how much money would you like to Withdraw?")
            app.userWithdraw=int(app.userWithdraw)
            if app.userWithdraw > app.currentBalance:
                print("You do not have enough money")
            elif app.userWithdraw <= app.currentBalance:
                app.currentBalance= app.currentBalance - app.userWithdraw
    elif app.userInput== "3":
        app.programRunning=False
    else:
        print("Your choice is invalid")
            

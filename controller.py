import model
import view

def run():
    model.load()
    initialmenu()

def initialmenu():
    while True:
        view.show_initalmenu()
        selection = view.get_input()
        print(selection)
        if selection == '1':
            new_Firstname = view.get_FirstName()
            new_LastName = view.get_LastName()
            new_pin = view.get_pin()
            newaccount=model.create_account(new_Firstname,new_LastName,new_pin)
            model.save(newaccount)
            
            
        elif selection == '2':
            clientcheck=view.clientcheck()
            accountcheck = int(view.accountcheck())
            pin=int(view.pincheck())
            model.login(clientcheck,accountcheck, pin)
            mainmenu(clientcheck,accountcheck)

        elif selection == '3':
            pass
        else:
            view.bad_input()

def mainmenu(clientname,accountcheck):
    while True:
        view.show_mainmenu(clientname,accountcheck)
        selection = view.get_input()
        print(selection)
        if selection == '1':
            view.show_balance(model.get_balance(clientname))
        elif selection == '3':
            model.add_fund(clientname, view.get_deposit())
            
        elif selection == '2':
            model.withdraw(clientname,view.get_withdraw())
            pass
        elif selection == '4':
            view.goodby()
            initialmenu()
        else:
            view.bad_input()


if __name__ == "__main__":
    run()
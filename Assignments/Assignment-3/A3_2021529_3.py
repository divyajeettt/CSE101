import datetime as dt


class BankAccount:
    """represents the Bank Account of a IIIT-D associated person"""
     
    def __init__(self, username: str, password: str, amount: float) -> None:
        """initializes self with given parameters"""
         
        self.username = username
        self.password = password
        self.amount = amount
        
        with open(f"{username}.txt", "w") as file:
            pass
    
    
    def authenticate(self) -> bool:
        """returns True if given password matches with user's password, and
        False in all other cases"""
        
        return self.password == input("Enter your password: ")
    
    
    def deposit(self, amount: float, attempts: float=0) -> None:
        """deposits the given amount to the Bank Account"""
        
        try:
            assert attempts < 3, "Too many wrong attempts!!"
        except AssertionError as err:
            print(err)
            return
        
        if not self.authenticate():
            print("Wrong Password!")
            self.deposit(amount, attempts=attempts+1)
        else:
            self.amount += amount
            log = f"Amount of Rs. {amount} /- has been added. Current Balance: Rs. {self.amount} /-"
            print(log)
            with open(f"{self.username}.txt", "a") as file:
                file.write(f"{dt.datetime.now()}: {log} \n")
        
    
    def withdraw(self, amount: float, attempts: float=0) -> None:
        """withdraws the given amount from the Bank Account"""
        
        try:
            assert attempts < 3, "Too many wrong attempts!!"
        except AssertionError as err:
            print(err)
            return
        
        if not self.authenticate():
            print("Wrong Password!")
            self.withdraw(amount, attempts=attempts+1)
        else:
            if amount <= self.amount:
                self.amount -= amount
                log = f"Amount of Rs. {amount} /- has been debited. Current Balance: Rs. {self.amount} /-"
                print(log)
                with open(f"{self.username}.txt", "a") as file:
                    file.write(f"{dt.datetime.now()}: {log} \n")
            else:
                print("Low balance!! Cannot be debited at this time!")
    
    
    def bankStatement(self, attempts: float=0) -> None:
        """displays the transaction history for the user"""
        
        try:
            assert attempts < 3, "Too many wrong attempts!!"
        except AssertionError as err:
            print(err)
            return
        
        if not self.authenticate():
            print("Wrong Password!")
            self.bankStatement(amount, attempts=attempts+1)
        else:
            with open(f"{self.username}.txt") as file:
                print(*file.readlines(), sep="")


def valid(string: str) -> bool:
    """returns True if the string is a valid password, and False otherwise"""
    
    return len(string) >= 8 and string.isalnum()


def main() -> None:
    """__main__ function"""
    
    print("Welcome to the Bank of IIIT-D!")
    username = input("Enter your Username: ")
    
    while not valid(password := input("Choose a password: ")):
        print("Invalid Passowrd! A password must hvae at least 8 characters!")
        
    amount = float(input("Enter initial amount to be deposited: "))
    print()

    account = BankAccount(username, password, amount)
    
    while True:
        print("Enter 1. to deposit a sum into your account")
        print("Enter 2. to withdraw an amount from your account")
        print("Enter 3. to view your Bank Statement / Transaction History")
        print("Enter 4. to EXIT")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount to be deposited: "))
            account.deposit(amount)
            print()
        
        elif choice == "2":
            amount = float(input("Enter amount to be withdrawn: "))
            account.withdraw(amount)
            print()
        
        elif choice == "3":
            account.bankStatement()
        
        elif choice == "4":
            break
    
        else:
            print("Invalid Choice! Enter again! \n")
            

if __name__ == "__main__":
    main()
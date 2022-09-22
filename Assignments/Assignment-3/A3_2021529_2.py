import re


ID = 1
class LaundryService:
    """represents a cloth and apparel cleaning service"""
    
    def __init__(
            self, name: str, contact: int, mail: str, cloth_type: str, 
            branded: bool, season: str
        ) -> None:
        """initializes self with given parameters"""
        
        global ID
        
        self.ID = ID
        self.name, self.contact, self.mail = name, contact, mail
        self.cloth_type = cloth_type.capitalize()
        self.branded = bool(branded)
        self.season = season.capitalize()
        ID += 1
    
    def customerDetails(self) -> None:
        """prints detials of a customer"""
    
        print("=" * 50)
        print(f"1. Name: {self.name}")
        print(f"2. Contact Number: {self.contact}")
        print(f"3. E-Mail: {self.mail}")
        print(f"4. Type of Cloth: {self.cloth_type}")
        print(f"5. Branded: {self.branded}")
    
    def calculateCharge(self) -> float:
        """returns the total charge according to the given scheme, in Rupees"""
        
        cost = {"Cotton": 50, "Silk": 30, "Woolen": 90, "Polyester": 20}[self.cloth_type]
        cost *= (1.5 if self.branded else 1)
        cost *= (1/2 if self.season == "Winter" else 2)
        return cost
    
    def finalDetails(self) -> None:
        """displays the total charge and expected day of return"""
        
        self.customerDetails()
        print("Total Charge: \N{INDIAN RUPEE SIGN}", (charge := self.calculateCharge()) ,"/-")
        print(f"To be returned in {4 if charge > 200 else 7} days")


def valid(string: str) -> bool:
    """returns True if the string is a valid email, and False otherwise"""

    return re.fullmatch(r"[\w+_.-]+@[\w.-]+\.[\w.-]+", string) is not None


def main() -> None:
    """__main__ function"""
    
    global ID
    
    n = int(input("Enter number of instances to be created: "))
    print()
    
    customers = {}
    for i in range(1, n+1):
        name = input("Enter name of customer: ")
        
        while not (contact := input("Enter contact number of customer: ")).isnumeric():
            print("Invalid Contact Number!")
        
        while not valid(mail := input("Enter E-Mail ID of customer: ")):
            print("Invalid E-Mail ID!")
            
        cloth_type = input("Enter type of cloth: ")
        branded = int(input("Enter whether the cloth is Branded (0 / 1): "))
        season = input("Enter season: ")
        customers[i] = LaundryService(name, contact, mail, cloth_type, branded, season)
        print()

    for customer_id in range(1, ID):
        print(f"Details of customer with ID: {customer_id}")
        customers[customer_id].finalDetails()
        print()


if __name__ == "__main__":
    main()
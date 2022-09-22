class Person:
    """represents a Person with certain attributes"""
    
    def __init__(self, first: str, last: str, age: int) -> None:
        """initializes self with the given attributes"""
        
        self.firstname, self.lastname, self.age = first, last, age
    
    
    def __repr__(self) -> str:
        """implements repr for Person"""
        
        return f"{self.firstname} {self.lastname} {self.age}"
    
    
    def object_info(self) -> None:
        """displays all attributes of the object separated by space"""
        
        print(self)
    

def sort_attribute(people: list[Person], key: str) -> list[Person]:
    """returns a list of Persons sorted by given key (firsname, lastname, age)"""
    
    n = len(people)
    for i in range(n):
        for j in range(n-i-1):
            if getattr(people[j], key) > getattr(people[j+1], key):
                people[j], people[j+1] = people[j+1], people[j]
    return people


def main() -> None:
    """__main__ function"""
    
    n = int(input("Enter number of people to enroll: "))
    people = []
    for i in range(1, n+1):
        firstname = input(f"Enter firstname of Person {i}: ")
        lastname = input(f"Enter lastname of Person {i}: ")
        age = int(input(f"Enter age of Person {i}: "))
        people.append(Person(firstname, lastname, age))
    
    print()
    k = int(input("Enter number of queries: "))
    for _ in range(k):
        query = input("Enter Query (to sort by): ").lower()
        try:
            for person in sort_attribute(people, query):
                person.object_info()
        except AttributeError:
            print("Invalid Query!") 
        print()
    
    print("Thanks for using the Application!")
    choice = input("Enter 'Y' to restart the app, and 'N' to exit: ").upper()
    
    if choice == "Y":
        print()
        main()
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()
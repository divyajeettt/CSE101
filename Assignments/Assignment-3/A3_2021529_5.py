class Company:
    """represents a Company coming to hire IIIT-ians"""
    
    def __init__(self, name: str, requiredcgpa: float, branches: list[str], positionOpen: int) -> None:
        """initializes self with the given parameters"""
        
        self.name, self.requiredcgpa = name, requiredcgpa
        self.branches, self.positionOpen = branches, positionOpen
        
        self.appliedStudents: list["Student"] = []
        self.applicationOpen: bool = True
        
    
    def hireStudents(self) -> None:
        """hires the top k students from the list of appliedStudents"""
        
        self.appliedStudents.sort(reverse=True)
        
        self.hired = 0
        for i in range(self.positionOpen):
            try:
                student = self.appliedStudents[i]
                if student.isEligible(self):
                    self.appliedStudents[i].getsPlaced()
                    print("Hired:", student.name)
                    self.hired += 1
                    self.positionOpen -= 1
            except IndexError:
                break

        print("Number of positions open:", self.positionOpen)
        self.closeApplication()
    
    
    def closeApplication(self) -> None:
        """closes the application process for the company"""
        
        self.applicationOpen = False
        print("Number of students hired:", self.hired)


class Student:
    """represents a Student studying at IIIT-D"""
    
    def __init__(self, name: str, cgpa: float, branch: str) -> None:
        """inititalizes self with the given parameters"""
        
        self.name, self.cgpa, self.branch = name, cgpa, branch
        self.isPlaced: bool = False
   
    
    def __lt__(self, other: "Student") -> bool:
        """defines < operator for Student
        Assumption: a Student self is less than Student other if self.cgpa < other.cgpa"""
        
        return self.cgpa < other.cgpa
    
    
    def isEligible(self, company: Company, display: bool=False) -> bool:
        """returns True if the student is eligible for the given
        company and False otherwise"""
        
        eligible = (
            (self.cgpa >= company.requiredcgpa) and 
            (self.branch in company.branches) and
            (not self.isPlaced)
        )
        
        if display:
            if eligible:
                print(f"Student {self.name} is eligible for Company {company.name}")
            else:
                print(f"Student {self.name} is not eligible for Companny {company.name}")
        
        return eligible


    def apply(self, company: Company) -> None:
        """adds the student to the list of appliedStudents of the company"""
        
        company.appliedStudents.append(self)
    
    
    def getsPlaced(self) -> None:
        """changes the placed status to True"""
        
        self.isPlaced = True


def main() -> None:
    """__main__ function"""
    
    n = int(input("Enter number of students: "))
    
    students = []
    for i in range(1, n+1):
        name = input(f"Enter name of Student {i}: ")
        cgpa = float(input(f"Enter cgpa of Student {i}: "))
        try:
            assert 0 <= cgpa <= 10, "CGPA must be between 0 and 10!"
        except AssertionError as err:
            print(err)
        else:
            branch = input(f"Enter the branch of Student {i}: ").upper()
            students.append(Student(name, cgpa, branch))
    
    print()
    m = int(input("Enter number of companies: "))
    
    companies = []
    for i in range(1, m+1):
        name = input(f"Enter name of Company {i}: ")
        requiredcgpa = float(input(f"Enter cgpa requirement of Company {i}: "))
        try:
            assert 0 <= requiredcgpa <= 10, "CGPA must be between 0 and 10!"
        except AssertionError as err:
            print(err)
        else:
            branches = input(f"Enter space-separated branches of Company {i}: ").split()
            positionOpen = int(input(f"Enter the number of positions open of Company {i}: "))
            
            companies.append(Company(name, requiredcgpa, branches, positionOpen))
        
    print()
    
    # # Sample Test Case
    # students = [
    #     Student("Naman", 10.0, "CSE"),
    #     Student("Pankil", 9.6, "CSE"),
    #     Student("Himanshu", 5.9, "CSE"),
    #     Student("Vishwesh", 6.9, "CSAM"),
    #     Student("Mayank", 8.0, "ECE"),
    # ]
    
    # companies = [
    #     Company("Microsoft", 6.0, ["CSE", "CSAM"], 2),
    #     Company("Amzaon", 1.0, ["CSE", "CSAM", "ECE"], 5),
    # ]
    
    for company in companies:
        for student in students:
            if student.isEligible(company, display=True):
                student.apply(company)
        company.hireStudents()
        print()


if __name__ == "__main__":
    main()
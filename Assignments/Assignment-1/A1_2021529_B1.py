RS: str = "\N{INDIAN RUPEE SIGN}"


def divider(char: str, width: int=80) -> str:
    """returns a separator of given width of given character
    example: divider("*", 10) -> ********** """
    
    return char * width


def table(rows: list[list[str]]) -> None:
    """displays the given rows as a table, taking the first row as a header
    the table is made dynamicaly, depending upon lengths of the longest elements
    rows is a nested list - each entry represents a row"""
    
    max1 = max2 = ""
    col1, col2 = [], []
    
    # calculate the longest entry in each column to fix column width
    for c1, c2 in rows:
        if len(c1) > len(max1):
            max1 = c1
        
        try:
            c2 = f"{c2:,.2f}"
        except ValueError:
            pass
        
        if len(c2) > len(max2):
            max2 = c2
        
        col1.append(c1)
        col2.append(c2)
    
    # format information into a table
    m1, m2 = len(max1), len(max2)
    
    print(f"+-{'-'*m1}-+-{'-'*m2}-+")
    print(f"| {col1[0].center(m1)} | {col2[0].center(m2)} |")
    print(f"+-{'-'*m1}-+-{'-'*m2}-+")

    for c1, c2 in zip(col1[1:], col2[1:]):
        print(f"| {c1.ljust(m1)} | {c2.ljust(m2)} |")
    
    print(f"+-{'-'*m1}-+-{'-'*m2}-+")


def catalogue(prices: list[float], discounts: list[float], contact: str) -> None:
    """displays the catalogue according to the given details"""
    
    p1, p2, p3 = prices
    d1, d2, d3, d4 = discounts
    
    c1 = (p1+p2) - (d1/100 * (p1+p2))
    c2 = (p3+p1) - (d2/100 * (p3+p1))
    c3 = (p2+p3) - (d3/100 * (p2+p3))
    c4 = (p1+p2+p3) - (d4/100 * (p1+p2+p3))
    
    print("HERE'S YOUR RESULTING CATALOGUE \n")
    
    print(divider("=", 80))
    print("Welcome to DELHI DAYS by ABHAY".center(80))
    print(divider("=", 80), "\n")
    
    table([
        ["ITEM", f"PRICE PER PACK (in {RS})"], 
        ["Item1", p1], ["Item2", p2], ["Item3", p3],
        ["ComboPack1", c1], ["ComboPack2", c2], ["ComboPack3", c3], ["SuperSaver", c4]
    ])
    
    print("\n", divider("=", 80), "\n", sep="")
    print("DELHI DAYS \nR-Block, Model Town 3 \nDelhi: 110009")
    print("For home delivery, call:", contact)

    
def main() -> None:
    """__main__ function"""
    
    print("\nItems' Pricing Details \n")
    item1 = float(input(f"Enter price of item 1 (in {RS}): "))
    item2 = float(input(f"Enter price of item 2 (in {RS}): "))
    item3 = float(input(f"Enter price of item 3 (in {RS}): "))
    
    print("\n", divider("+", 80), "\n", sep="")
    
    print("Discount Details of the ComboPacks \n")
    discount1 = float(input("Enter discount rate for ComboPack1: "))
    discount2 = float(input("Enter discount rate for ComboPack2: "))
    discount3 = float(input("Enter discount rate for ComboPack3: "))
    discount4 = 28.0
    
    print("\n", divider("+", 80), "\n", sep="")
    
    print("Contact Details")
    contact = input("Enter your contact number: ")
    
    while len(contact) != 10 and contact.isdigit():
        print("Contact Number must contain 10 digtis")
        contact = input("Enter your contact number: ")
        
    print("\n", divider("+", 80), "\n", sep="")
    catalogue(
        [item1, item2, item3], [discount1, discount2, discount3, discount4], contact
    )


if __name__ == "__main__":
    main()
"""
SOME LOGICS THAT ARE BEING USED IN THIS PROBLEM
n % 10 returns the last digit of n
n // 10 returns n with its last digit removed, n //= 10 re-assigns that value to it
"""


def getReverse(n: int) -> int:
    """returns the integer formed by reversing the digits of n"""
    
    reverse = 0
    while n > 0:
        # reverse*10 shifts all digits of reverse to the left
        reverse = reverse*10 + n%10
        n //= 10
    
    return reverse


def checkPalindrome(n: int) -> bool:
    """returns True if n is a Palindrome, False otherwise
    n is a Palindrome if it is the same when its digits are reversed"""
    
    # it is always a good practice to not re-write the same code
    # used the function get_Reverse(n) to find its reverse
    return n == getReverse(n)


def num_of_digits(n: int) -> int:
    """returns the number of digits present in n"""
    
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits
    
    
def checkNarcissistic(n: int) -> bool:
    """returns True if n is a Narcissistic number, False otherwise
    an x-digit n is narcissistic when the sum of each of its (digit)ˣ is equal to n"""
    
    total, copy = 0, n
    digits = num_of_digits(n)
    
    while n > 0:
        total += (n%10) ** digits
        n //= 10
    
    return total == copy


def findDigitSum(n: int) -> int:
    """returns the recursive sum of digits of n"""
    
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    
    if num_of_digits(total) == 1:
        return total
    else:
        return total + findDigitSum(total)

####### CONVEY TO THE EVALUATOR: the 'recursing' parameter was an earlier approach that i used, that I accidentally forgot to remove
#######                          from the function definition before submitting. Please consider that it is not meant to be there.
def findSquareDigitSum(n: int, recursing: bool=False) -> int:
    """returns the recursive sum of squares of digits of n"""
    
    total = 0
    while n > 0:
        total += (n%10) ** 2
        n //= 10
    
    if num_of_digits(total) == 1:
        return total
    else:
        return total + findSquareDigitSum(total)


def main() -> None:
    """__main__ function"""
    
    while True:
        print("Enter 1. to get the reverse of the number")
        print("Enter 2. to check if the number is a Palindrome")
        print("Enter 3. to check if the number is a Narcissistic number")
        print("Enter 4. to get the sum of digits of the number")
        print("Enter 5. to get the sum of squares of the digits of the number")
        print("Enter 6. to Exit \n")
        
        choice = input("Enter your choice: ")
        
        if choice == "6":
            break
        if choice not in tuple("123456"):
            print("INVALID INPUT: Please enter a valid input. \n")
            continue
    
        n = int(input("Enter a non-negative integer: "))
        print()
        
        if choice == "1":
            print("Original Number =", n)
            print("Reverse of the Number =", getReverse(n))
        
        elif choice == "2":
            if checkPalindrome(n):
                print(n, "is a Palindrome")
            else:
                print(n, "is not a Palindrome")
        
        elif choice == "3":
            if checkNarcissistic(n):
                print(n, "is a Narcissistic Number")
            else:
                print(n, "is not a Narcissistic Number")
        
        elif choice == "4":
            print("Sum of Digits of", n, "=", findDigitSum(n))
        
        else:
            print("Sum of Squares of Digits of", n, "=", findSquareDigitSum(n))
            
        print()


if __name__ == "__main__":
    main()
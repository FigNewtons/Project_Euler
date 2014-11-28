#Project Euler Challenge 4

#Find the largest palindrome made from the product of two 3-digit numbers.

#Compare this to my original code to see which one is faster

def isPalindrome(number):
    return number == number[::-1]
 
largestPalindrome=0
for i in range(100,999):
    for j in range(100,999):
        result = i * j
        if (isPalindrome(str(result))) and result > largestPalindrome:
            largestPalindrome = result
            print (largestPalindrome)

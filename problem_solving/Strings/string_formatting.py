#Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    
    for i in range(1, number + 1):
        octal = oct(i)
        hexadecimal = hex(i)
        binary = bin(i)
    
        i = str(i)
        octal = str(octal)
        hexadecimal = str(hexadecimal).upper()
        binary = str(binary)
        
        print(i.rjust(3, " ") + " " + octal[2:].rjust(3, " ") + " " + hexadecimal[2:].rjust(3, " ") + " " + binary[2:].rjust(5, " "))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
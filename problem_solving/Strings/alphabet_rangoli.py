#Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #top
    counter = 0
    for i in range(1, n + 1):
        print("-" * (((n - 1) * 2) - counter), end="")
    
        for y in range (1, i + 1):
            print(alphabet[n - y], end="")
            if y != i:
                print("-", end="")

        for x in range (2, i + 1):
            print("-" + alphabet[n - (i + 1) + x], end="")

        print("-" * (((n - 1) * 2) - counter))
        counter += 2

    #bottom
    supp_counter = 2    # counter for "-" before letters
    supp_counter2 = 1   # counter for "-" after letters
    while_loop_counter = n
    for i in range (1, n):
        for y in range (1):
            print("-" * supp_counter, end="")
            supp_counter += 2

        y = 0
        while y != while_loop_counter - 1:
            print(alphabet[(n - 1) - y] + "-", end="")
            y += 1

        y = 1
        while y != while_loop_counter - 1:
            print(alphabet[i + y] + "-", end="")
            y += 1
        while_loop_counter -= 1

        for i in range (1):
            print("-" * supp_counter2, end="")
            supp_counter2 += 2
 
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



    


       

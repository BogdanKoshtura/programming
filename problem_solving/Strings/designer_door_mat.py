#Promlem: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

n, m = input().split()
n = int(n)
m = int(m)

a = "-"
b = ".|."
a_counter = 1 # counter for printing "-"
b_counter = 1 # counter for odd numbers, for printing ".|."

#Top
for i in range(1, n // 2 + 1):
        print(a * (m // 2 - a_counter), end="")
        
        print(b * b_counter, end="")
        b_counter += 2
        
        print(a * (m //  2 - a_counter), end="")        
        print()
        a_counter += 3

#Center
print(a * ((m - 7) // 2) +  "WELCOME" + a * ((m - 7) // 2))

#Bottom
for i in range(1, n // 2 + 1):
        a_counter -= 3
        print(a * (m // 2 - a_counter), end="")

        b_counter -=2
        print(b * b_counter, end="")

        print(a * (m // 2 - a_counter), end="")
        print()      

""" Write code that will print the following:
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9 """
print("Answer")
for i in range(9):
    for j in range(9):
        print(j, end=" ")
    print()

""" Adjust the prior program to print:
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9 """
print("Answer")
for i in range(9):
    for j in range(9):
        print(i, end=" ")
    print()
""" Write code that will print the following:
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9 """
print("Answer")
for i in range(9):
    for j in range(i):
        print(j, end=" ")
    print()
""" Write code that will print the following:
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0 """
print("Answer Part one")
for i in range(9):
    for k in range(i):
        print(" ", end=" ")
    for j in range(9 - i):
        print(j, end=" ")
    print()
""" Write code that will print the following (Getting the alignment is hard, at least get the numbers):
1   2   3   4   5   6   7   8   9
2   4   6   8  10  12  14  16  18
3   6   9  12  15  18  21  24  27
4   8  12  16  20  24  28  32  36
5  10  15  20  25  30  35  40  45
6  12  18  24  30  36  42  48  54
7  14  21  28  35  42  49  56  63
8  16  24  32  40  48  56  64  72
9  18  27  36  45  54  63  72  81 """

for i in range(9):
    for j in range(9):
        print(j * i, end=" ")
    print()
""" Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 """
print("Answer")
for i in range(11):
    for k in range(11-i):
        print(" ",end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
""" Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2 """
for i in range(11):
    for j in range(11 - i):
        print(" ", end=" ")
    for j in range(1, i):
        print(j, end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
for i in range(11):
    for j in range(i + 2):
        print(" ", end=" ")
    for j in range(1,10 - i):
        print(j, end=" ")

    print()
    
""" Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 4 3 2 1
            1 2 3 4 3 2 1
              1 2 3 2 1
                1 2 1
                  1 """


for i in range(11):
    for j in range(11 - i):
        print(" ", end=" ")
    for j in range(1, i):
        print(j, end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
print()
for i in range(11):
    for j in range(i + 2):
        print(" ", end=" ")
    for j in range(1,10 - i):
        print(j, end=" ")
    for l in range(10 - i, 0 , -1):
        print(l, end=" ")

    print()






    
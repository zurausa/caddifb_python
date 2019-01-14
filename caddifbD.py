import math,sys
def main():
    n = int(input())
    for i in range(0,n):
        if int(sys.stdin.readline()) % 2 == 1:
            print('first')
            sys.exit()
    print('second')

main()
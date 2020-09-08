from ICA8 import FizzBuzz

def main():
    list = []
    for i in range(0,51):     
        list.append (FizzBuzz(i))
    for j in list:
        print(j.fbn)
main()
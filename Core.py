# Logical Count
import multiprocessing

def main():
    print("Number of cores are : ",multiprocessing.cpu_count())       # output = 8

if __name__ == "__main__":
    main()
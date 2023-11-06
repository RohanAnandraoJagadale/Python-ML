import schedule
import time
import datetime
# hello world display on screen 1 min on console

def Fun():
    print("Inside Fun")

def main():
    print("Inside task schedular")

    schedule.every(1).minutes.do(Fun)    # register jhal

    while(True):                          # uncondition infinite loop
        schedule.run_pending()
        time.sleep(1)                      # 1 sec delay houshakto

if __name__ == "__main__":
    main()
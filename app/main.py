from datetime import datetime
import time


def main():
    while True:
        now = datetime.now()
        with open("app-{now.hour}_{now.minute}_{now.second}.log", "w") as file:
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(1)    

    print(datetime.now())        


if __name__ == "__main__":
    main()

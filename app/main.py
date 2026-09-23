from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log",
                   "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(1)
    print(datetime.now())


if __name__ == "__main__":
    main()

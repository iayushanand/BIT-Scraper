import time

from pipeline import (
    stage1,
    stage2,
    stage3,
    stage4,
    stage5,
    stage6,
    stage7,
)


def main():

    start = time.perf_counter()

    stage1()
    stage2()
    stage3()
    stage4()
    stage5()
    stage6()
    stage7()

    end = time.perf_counter()

    elapsed = end - start

    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    seconds = elapsed % 60

    print("\n" + "=" * 60)
    print("BIT Scraper Finished")
    print("=" * 60)
    print(f"Total Time: {hours:02d}:{minutes:02d}:{seconds:05.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
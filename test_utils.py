from utils import watch_process_time
import time

@watch_process_time
def test_delay(secs: int | float):
    time.sleep(secs)
    return True


if __name__ == '__main__':
    test_delay(10)
    res = test_delay(15)
    print(res)

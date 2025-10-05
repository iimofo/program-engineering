import datetime
import time

def display_time_with_sleep():
    print("--- Time Display with Sleep ---")
    for i in range(5):
        current_time = datetime.datetime.now()
        print(f"Current Time ({i+1}/5): {current_time.strftime('%H:%M:%S')}")
        time.sleep(1)

if __name__ == '__main__':
    display_time_with_sleep()
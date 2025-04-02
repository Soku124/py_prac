from datetime import datetime
import time


def logger(func):
    def wrapper():
        print("-"*50)
        print(f"> Execution started {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}")
        func()
        print(f"> Execution completed {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}")
        print("-"*50)
    
    return wrapper

@logger
def demo_function():
    print("Executing task!")
    time.sleep(2)
    print("Task Completed!")

demo_function()

# logger(demo_function())


def logger_args(func):
    def wrapper(*args, **kwargs):
        print("-"*50)
        print(f"> Execution started {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}")
        func(*args,**kwargs)
        print(f"> Execution completed {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}")
        print("-"*50)
    
    return wrapper

@logger_args
def demo_function_args(sleep_time):
    print("Executing task!")
    time.sleep(sleep_time)
    print("Task completed!")

demo_function_args(1)
demo_function_args(2)
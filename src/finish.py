import time

def finish_setup():
    """Wait for setup completion"""
    time.sleep(5)
    print("After type yes , Press Ctrl + C to end the setup!")

if __name__ == "__main__":
    finish_setup()

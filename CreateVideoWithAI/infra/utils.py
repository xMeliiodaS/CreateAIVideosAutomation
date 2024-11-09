import time


def stop_page_load(driver, wait_time=1):
    """
    Stops the page from loading after a set amount of time.
    """
    time.sleep(wait_time)
    try:
        driver.execute_script("window.stop();")
        print(f"Stopped page loading after {wait_time} seconds.")
    except Exception as e:
        print(f"Failed to stop page load: {e}")

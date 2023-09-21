import requests
import threading
import time

# Define a function that makes the request
def make_request():
    url = "https://url/test"
    response = requests.get(url, verify=False)
    print (response.status_code)
    # You can add any handling or processing of the response here if needed

i = 0

for i in range(0, 2):
    # Define the number of threads you want to use
    num_threads = 5  # Adjust this based on your needs

    # Create a list to hold the thread objects
    threads = []

    # Create and start the threads
    for _ in range(num_threads):
        thread = threading.Thread(target=make_request)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    time.sleep(1)
    print("Thread finished")



# The requests have been made concurrently using threads

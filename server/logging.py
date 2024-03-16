import datetime

def log_data(data):
    """
    Log data to a file with a timestamp.

    Args:
        data (dict): Data to be logged.

    Returns:
        None
    """
    try:
        # Generate timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log data to a file with timestamp
        with open('data/log.txt', 'a') as log_file:
            log_file.write(f"{timestamp}: {data}\n")

        print("Data logged successfully.")
    except Exception as e:
        # Handle logging errors
        print(f"Logging error: {e}")

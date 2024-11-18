import logging
import os
from datetime import datetime

# Generate a log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where logs will be stored
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure the directory for logs exists, create it if not
os.makedirs(logs_path, exist_ok=True)

# Full path of the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    # Log messages will be written to this file
    filename=LOG_FILE_PATH,
    # Define the format of the log messages
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Set the logging level to INFO (logs INFO, WARNING, ERROR, CRITICAL)
    level=logging.INFO,
)

# if __name__=="_main__":
#     logging.info("logging has started")s
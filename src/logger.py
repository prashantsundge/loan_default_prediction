import logging
import os 
from datetime import datetime


# create logs directory if not exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# create log files name with timestamps 

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

#configure logging 

logging.basicConfig(
    filename=LOG_PATH,
    level= logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S"
)


def get_logger():
    return logging.getLogger()

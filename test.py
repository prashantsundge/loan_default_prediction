# test logging and exceptions configured correctly 


from src.logger import get_logger
from src.exception import CustomException
import sys

logger = get_logger()


try:
    a = 1/0
except Exception as e:
    logger.error(f"Error Occured : {CustomException(e, sys)}")
    raise CustomException(e, sys)

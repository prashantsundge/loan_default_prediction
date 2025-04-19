import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from data_loader import DataLoader
from logger import get_logger
from exception import CustomException
import sys


logger = get_logger()


if __name__ == "__main__":
    try:
        data_loader = DataLoader(file_path=r"E:\ML PROJECT\loan_default_prediction\data\raw\Loan_default.csv")  # raw string
        df = data_loader.load_data()
        logger.info(f"first 5 rows :\n {df.head()}")

    except Exception as e:
        logger.error(f"Pipeline Failed : {CustomException(e, sys)}")

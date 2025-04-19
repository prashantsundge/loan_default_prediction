import pandas as pd 
from logger import get_logger
from exception import CustomException
import sys
import os

logger = get_logger()

class DataLoader:
    def __init__(self, file_path:str):
        self.file_path = file_path

    
    def load_data(self) -> pd.DataFrame:
        """
        Load Data from a CSV file into a pandas Dataframe

        """
        logger.info(f"Attempting to load from : {self.file_path}")
        try:
            if not os.path.exists(self.file_path):
                message = f"file not found at path: {self.file_path}"
                logger.error(message)
                raise FileNotFoundError(message)
            data = pd.read_csv(self.file_path)
            logger.info(f"Data Loaded Successfully. shape:{data.shape}")
            return data
        
        except Exception as e:
            logger.error(f"failed to load data : {CustomException(e, sys)}")
            raise CustomException(e, sys)
        
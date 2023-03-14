import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logger import logging
from exceptions import CustomException
import pandas as pd 


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("readdata as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            
            logging.info("train testsplit initiated")
            train_set,test_set = train_test_split(df,test_set = 0.2,random_state = 42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            
            logging.info("ingestion of data comleted")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
            
        except Exeption as e:
            raise CustonException(e,sys)
        
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj = DataIngestionConfig()
        
        
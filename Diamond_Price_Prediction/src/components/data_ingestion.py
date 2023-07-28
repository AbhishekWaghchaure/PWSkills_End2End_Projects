import os
import sys
from src.logger import logging
from src.exception_handling import CustomException
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

## initializing the data ingestion configuration

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_dataingestion(self):
        logging.info('Data Ingestion Starts')
        
        try:
            df = pd.read_csv('/Users/abhishekwaghchaure/Desktop/PW_Skills _End2End_Projects/Diamond_Price_Prediction/notebooks/data/gemstone.csv')
            logging.info('Dataset reading happening')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Raaw data created')
            
            train_set,test_set = train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index =False, header = True)
            logging.info('Ingestion of data is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            logging.info()
        except Exception as e:
            logging.info('Error occured at data ingestion stage')
            raise CustomException(e,sys)
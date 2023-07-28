import os
import sys
from src.logger import logging
from src.exception_handling import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_dataingestion()
    print(train_data_path,test_data_path)
    
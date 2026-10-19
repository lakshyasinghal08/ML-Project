import sys
from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_transformation import DataTransformation

if __name__ == "__main__":
    logging.info("The execution has started")    
    
    try: 
        # Data Ingestion
        data_ingestion = DataIngestion()
        # FIX: Added () to properly call the method
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # Data Transformation
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformer(train_data_path, test_data_path)
        
        logging.info("Data Transformation executed successfully")
        
    except Exception as e: 
        logging.info("Custom Exception executed")
        raise CustomException(e, sys)
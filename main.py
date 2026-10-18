import sys
from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info("The execution has started")    
    
    try: 
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        logging.info(f"Data ingestion completed successfully. Train path: {train_data_path}, Test path: {test_data_path}")
    except Exception as e:
        logging.info("Custom Exception executed Successfully")
        raise CustomException(e, sys)
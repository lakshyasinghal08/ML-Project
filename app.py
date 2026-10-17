from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("the execution has started")    
    
    try: 
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception executed Sucessfully")
        raise CustomException(e,sys)
        
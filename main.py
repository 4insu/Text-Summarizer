from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"------ Stage {STAGE_NAME} has started ------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"------ Stage {STAGE_NAME} has completed ------\n\n<=============>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"------ Stage {STAGE_NAME} has started ------")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"------ Stage {STAGE_NAME} has completed ------\n\n<=============>")
except Exception as e:
    logger.exception(e)
    raise e
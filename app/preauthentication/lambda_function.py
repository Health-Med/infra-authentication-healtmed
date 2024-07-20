from src.pre_authentication_service import pre_authentication_service
from aws_lambda_powertools import Logger

logger = Logger(service="lambda_pre_authentication")


@logger.inject_lambda_context
def lambda_handler(event, context):
    logger.info(f"Received event: {event}")
    return pre_authentication_service(event, logger=logger)

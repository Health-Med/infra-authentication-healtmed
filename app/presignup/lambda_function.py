from src.pre_sign_up_service import pre_sign_up
from aws_lambda_powertools import Logger

logger = Logger(service="lambda_pre_sign_up")


@logger.inject_lambda_context
def lambda_handler(event, context):
    logger.info(f"Received event: {event}")
    return pre_sign_up(event, logger=logger)

from src.post_confirmation_service import post_confirmation_service
from aws_lambda_powertools import Logger

logger = Logger(service="lambda_pre_sign_up")


@logger.inject_lambda_context
def lambda_handler(event, context):
    logger.info(f"Received event: {event}")
    return post_confirmation_service(event, logger=logger)

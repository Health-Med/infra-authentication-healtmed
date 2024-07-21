from src.pre_sign_up_service import pre_sign_up
from aws_lambda_powertools import Logger

logger = Logger(service="lambda_pre_sign_up")


@logger.inject_lambda_context
def lambda_handler(event, context):
    logger.info(f"Received event: {event}")
    return pre_sign_up(event, logger=logger)


if __name__ == '__main__':
    evento = {'version': '1', 'region': 'us-east-1', 'userPoolId': 'us-east-1_b0nXokgLH', 'userName': 'd408c488-80f1-7062-6493-e803a2ff44b2', 'callerContext': {'awsSdkVersion': 'aws-sdk-unknown-unknown', 'clientId': '6nf5of4slqo8pfrqrhp5el0v8u'}, 'triggerSource': 'PreSignUp_SignUp', 'request': {'userAttributes': {'custom:crm': '123456', 'custom:user_type': 'medico', 'email': 'medico@gmail.com'}, 'validationData': None}, 'response': {'autoConfirmUser': False, 'autoVerifyEmail': False, 'autoVerifyPhone': False}}
    pre_sign_up(evento, logger=logger)

import boto3


def post_confirmation_service(event, logger):
    client = boto3.client('cognito-idp')

    user_pool_id = event['userPoolId']
    username = event['userName']
    user_attributes = event['request']['userAttributes']

    if 'custom:CRM' in user_attributes:
        group = 'doctors'
    elif 'custom:CPF' in user_attributes:
        group = 'patients'
    elif 'email' in user_attributes:
        group = 'patients'
    else:
        raise Exception("User does not have a valid custom attribute")

    client.admin_add_user_to_group(
        UserPoolId=user_pool_id,
        Username=username,
        GroupName=group
    )

    logger.info(f'Usuario: {username} confirmado com sucesso, e adicionado ao grupo: {group}')
    return event

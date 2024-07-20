def pre_authentication_service(event, logger):
    username = event['userName']
    logger.info(f'Username: {username}')

    if is_valid_cpf(username) or is_valid_email(username) or is_valid_crm(username):
        logger.info(f"Usuário {username} válido, prosseguir com a autenticação.")
    else:
        logger.error(f"Nome de usuário inválido: {username}")
        raise Exception("Nome de usuário inválido")

    return event


def is_valid_cpf(username):
    return username.isdigit() and len(username) == 11


def is_valid_email(username):
    return '@' in username


def is_valid_crm(username):
    return username.isdigit() and len(username) >= 6

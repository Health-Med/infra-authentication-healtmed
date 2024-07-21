def pre_authentication_service(event, logger):
    username = event['userName']
    email = event['request']['userAttributes'].get('email')
    cpf = event['request']['userAttributes'].get('custom:CPF')
    crm = event['request']['userAttributes'].get('custom:CRM')

    logger.info(f'Username: {username}')

    if is_valid_cpf(cpf, logger) or is_valid_email(email) or is_valid_crm(crm):
        logger.info(f"Usuário {username} válido, prosseguir com a autenticação.")
    else:
        logger.error(f"Dados de autenticação inválidos")
        raise Exception("Dados de autenticação inválidos")

    return event


def is_valid_email(email):
    if not email:
        return False

    return '@' in email


def is_valid_crm(crm):
    if not crm:
        return False

    return crm.isdigit() and len(crm) >= 6


def is_valid_cpf(cpf, logger):
    if not cpf:
        return False

    # Remove caracteres especiais e espaços em branco do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        logger.warning("cpf nao possui 11 digitos: " + cpf)
        return False

    # Verifica se todos os dígitos do CPF são iguais, o que o tornaria inválido
    if len(set(cpf)) == 1:
        logger.warning("cpf invalido: " + cpf)
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    # Calcula o segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    # Verifica se os dígitos verificadores calculados correspondem aos dígitos fornecidos
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        logger.info("cpf validado com sucesso : " + cpf)
        return True
    else:
        logger.warning("cpf com digitos verificadores invalido: " + cpf)
        return False


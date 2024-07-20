def pre_sign_up(event, logger):
    user_type = event['request']['userAttributes'].get('custom:userType')
    logger.info(f'user_type: {user_type}')

    if user_type == 'Medico':
        crm = event['request']['userAttributes'].get('custom:CRM')
        if not validate_crm(crm):
            logger.error(f'CRM inválido: {crm}')
            event['response']['autoConfirmUser'] = False
            return event

    if user_type == 'Paciente':
        cpf = event['request']['userAttributes'].get('custom:CPF')
        username = event['request']['userAttributes'].get('username')

        if cpf:
            if not validate_cpf(cpf, logger):
                logger.error(f'CPF inválido: {cpf}')
                event['response']['autoConfirmUser'] = False
                return event
        elif is_valid_email(username):
            event['response']['autoConfirmUser'] = False
            return event

    event['response']['autoConfirmUser'] = True
    return event


def validate_crm(crm):
    """ TO-DO: implementar a Lógica para validação do CRM (Conselho Regional de Medicina) fornecido"""
    return True


def is_valid_email(username):
    return '@' in username


def validate_cpf(cpf, logger):
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

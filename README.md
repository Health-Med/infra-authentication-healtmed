# Provisionamento Amazon Cognito e Lambdas Triggers

Este repositório contém código Terraform para provisionar um Cognito User pools e Lambdas que funcionam como triggers personalizados para um pool de usuários no Amazon Cognito. As Lambdas são integradas ao fluxo de autenticação personalizado do Cognito.

---

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos configurados:

1. Conta AWS com permissões suficientes para provisionar recursos como Lambdas, Cognito, IAM, etc.
2. Terraform instalado localmente. Para instalar, consulte a [documentação oficial do Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli).
3. Python 3.11 ou superior instalado para desenvolvimento das funções Lambda.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:


- `app`: Implementação da lógica dos requisitos.
  - `presignup`
    - `pre_sign_up_service.py`: Lambda responsável por validar atributos de cadastro de usuarios.
  - `postconfirmation`
    - `post_confirmation_service.py`: Lambda responsável por identificar o tipo de usuario novo e adicioná-lo em seu respectivo grupo.
  - `preauthentication`
    - `pre_authentication_service.py`: Lambda responsável por validar atributos pré autenticação.
  - `postauthentication`
    - `post_authentication_service.py`: Lambda responsável por realizar uma ação após autenticação com sucesso.



- `infra`: Arquivos do Terraform para provisionar os recursos na AWS.
  - `cloudwatch.tf`
  - `cognito.tf`
  - `data.tf`
  - `lambda.tf`
  - `provider.tf`
  - `role.tf`
  - `variable.tf`


## 3. Inicialize o Terraform
```sh
terraform init
```


### 4. Visualize o Plano de Execução

Visualize o plano de execução para verificar as alterações que o Terraform fará na sua infraestrutura:

```sh
terraform plan
```

### 5. Aplique a Configuração

Aplique a configuração para provisionar os recursos:


```sh
terraform apply
```
Digite yes quando solicitado para confirmar a execução.


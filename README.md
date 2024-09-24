# Testes E2E para a Aplicação Sauce Demo

Este repositório contém um conjunto de testes end-to-end (E2E) desenvolvidos para a aplicação [Sauce Demo](https://www.saucedemo.com/).

## Descrição dos Testes

Os testes verificam as seguintes funcionalidades críticas da aplicação:

1. **Login e Logout**
   - Testes com diferentes usuários para validar o login e logout.

2. **Navegação e Acesso a Produtos**
   - Verificação se os produtos são exibidos corretamente após o login.
   - Acesso às informações dos produtos e verificação de erros para usuários problemáticos.

3. **Verificação de Erros**
   - Cenários com o usuário "problem_user" e "error_user" para verificar se as mensagens de erro aparecem conforme esperado, como quando o sobrenome não é preenchido no processo de checkout.

## Usuários Testados

### Teste com o Usuário Problem User

- O teste faz login com o usuário "problem_user".
- Adiciona um produto ao carrinho e tenta acessar a página de detalhes de um produto.
- Verifica se a mensagem de erro "ITEM NOT FOUND" é exibida corretamente ao tentar acessar um item não disponível.
- Simula um erro ao tentar continuar o checkout sem preencher o sobrenome, e verifica se a mensagem de erro "Error: Last Name is required" é exibida.

### Teste com o Usuário Error User

- O teste faz login com o usuário "error_user".
- Adiciona um produto ao carrinho e tenta acessar um produto que falha ao carregar a descrição.
- Verifica se a mensagem de erro correta aparece quando o sobrenome não é preenchido durante o checkout, confirmando se a aplicação lida adequadamente com campos obrigatórios.
- Registra as mensagens de erro durante o teste para garantir que os problemas sejam documentados.

## Tecnologias Utilizadas

- Python
- Selenium
- Unittest

### Pré-requisitos

1. Python instalado.
2. Dependências do Selenium instaladas. Você pode instalar com o seguinte comando:

   ```bash
   pip install selenium

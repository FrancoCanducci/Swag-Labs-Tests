# README - Testes Automatizados de Performance e Funcionalidade

## Descrição

Este repositório contém uma série de testes automatizados usando Selenium para verificar a funcionalidade e a performance de usuários no site da Sauce Demo. Os testes incluem simulações de login, adição de produtos ao carrinho e processos de checkout.

## Pré-requisitos

- Python 3.x
- Selenium
- WebDriver do Chrome
- Biblioteca `unittest` (inclusa no Python)

## Executando os Testes

1. Teste do Usuário Padrão (standard_user)
Este teste verifica se o usuário padrão consegue realizar o login, adicionar um produto ao carrinho e completar o checkout.

Fluxo do Teste:

Login: Acessa a página de login e insere as credenciais do standard_user.
Adicionar Produto: Adiciona um produto ao carrinho.
Checkout: Preenche as informações necessárias para o checkout.
Finalizar Checkout: Clica no botão de finalizar e aguarda a URL mudar para a página de inventário.

2.Teste do Usuário com Glitch de Performance (performance_glitch_user)
Este teste simula um processo de checkout e mede o tempo necessário para a transição para a página de inventário após a conclusão do checkout.

Fluxo do Teste:

Login: Acessa a página de login e insere as credenciais do performance_glitch_user.
Adicionar Produto: Adiciona um produto ao carrinho.
Checkout: Preenche as informações necessárias, incluindo nome, sobrenome e CEP.
Finalizar Checkout: Clica no botão de finalizar e aguarda a URL mudar para a página de inventário.
Medição de Performance: Calcula e registra o tempo necessário para a URL mudar.

3. Teste do Usuário com Problemas (problem_user)
Este teste verifica se o usuário com problemas consegue realizar o login, adicionar um produto ao carrinho e completar o checkout, mesmo enfrentando problemas na interface.

Fluxo do Teste:

Login: Acessa a página de login e insere as credenciais do problem_user.
Adicionar Produto: Adiciona um produto ao carrinho.
Checkout: Preenche as informações necessárias e tenta finalizar o checkout.
Verificação de Erros: Confirma se os erros apropriados aparecem na interface quando o usuário tenta concluir o checkout com informações inválidas ou incompletas.





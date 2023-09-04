# Projeto de Redução do Desperdício Alimentar

Bem-vindo ao nosso projeto dedicado à redução do desperdício de alimentos, utilizando a avançada tecnologia GPT-3.5 Turbo da OpenAI para criar um plano de refeições com base nos ingredientes que você tem à disposição.

## Instruções para Utilização

1. **Requisitos**
   - Certifique-se de que possui uma chave de API válida para o GPT-3.5 Turbo da OpenAI.
   - Verifique se as dependências necessárias estão instaladas corretamente. O projeto requer a biblioteca `requests` e `json`.

2. **Obtenção do Cardápio**
   - O programa solicitará que você insira os ingredientes disponíveis.
   - Para cada ingrediente, forneça o nome, a quantidade e a data de validade.
   - Após inserir os ingredientes desejados, você será perguntado se deseja adicionar mais um item.
   - O programa considera duas refeições por dia (almoço e jantar).

3. **Definição do Cronograma**
   - Após a obtenção dos ingredientes, o programa solicitará informações adicionais.
   - Digite o número de dias para o cronograma alimentar.

4. **Geração do Cronograma Alimentar**
   - O programa utilizará a tecnologia GPT-3.5 Turbo para criar um cronograma alimentar com base nos ingredientes fornecidos.
   - O cronograma será apresentado, considerando os ingredientes disponíveis.

## Detalhes do Projeto

Este projeto faz uso da biblioteca `apiKey` para importar a chave de API necessária para autenticação com a API da OpenAI. Certifique-se de possuir uma chave válida para utilizar o serviço.

A função `gpt3_responder(pergunta)` realiza solicitações à API do GPT-3.5 Turbo, enviando a pergunta como entrada e obtendo uma resposta gerada pelo modelo.

A função `obter_cardapio()` solicita ao usuário que insira os ingredientes disponíveis, armazenando-os em uma lista junto com suas quantidades e datas de validade.

A função `pergunta_chatgpt()` utiliza a função `obter_cardapio()` para obter os ingredientes, suas quantidades e datas de validade, e monta uma pergunta para o GPT-3.5 Turbo com base nesses dados.

Finalmente, o programa gera a pergunta para o GPT-3.5 Turbo e obtém a resposta correspondente, que será exibida na saída.

## Execução do Código

Para executar o código com sucesso, certifique-se de que preencheu corretamente as informações necessárias, incluindo a chave de API e as dependências do projeto. Após isso, execute o código e siga as instruções fornecidas pelo programa.

Esperamos que este projeto contribua para a redução do desperdício de alimentos e promova hábitos alimentares mais conscientes e equilibrados.
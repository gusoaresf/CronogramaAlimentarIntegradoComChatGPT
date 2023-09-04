from apiKey import api_key
# Por favor, forneça-nos a chave de API da OpenAI no arquivo (apiKey).
import requests
import json

def gpt3_responder(pergunta):
    headers = {"Authorization": f'Bearer {api_key}', 'Content-Type': 'application/json'}

    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = 'gpt-3.5-turbo-0301'

    body_mensagem = {
        'model': id_modelo,
        'messages': [{'role': 'user', 'content': pergunta}]
    }
    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    print(requisicao)
    resposta = requisicao.json()
    mensagem = resposta['choices'][0]['message']['content']
    print(mensagem)

def obter_cardapio():
    ingredientes = []

    continuar = "1"
    i = 1

    while continuar == "1":
        pergunta_ingrediente = f"Digite seu {i}º ingrediente: "
        resposta_ingrediente = input(pergunta_ingrediente)
        
        pergunta_quantidade = f"Digite a quantidade que você possui de {resposta_ingrediente}: "
        resposta_quantidade = input(pergunta_quantidade)
        pergunta_validade = f"Digite a válidade do ingrediente {resposta_ingrediente}: "
        resposta_validade = input(pergunta_validade)
        print()

        ingredientes.append((resposta_ingrediente, resposta_quantidade, resposta_validade))
        
        continuar = input("Deseja digitar mais um item? (1 - Sim / 2 - Não): ")
        print()
        
        while continuar != "1" and continuar != "2":
            print("Opção inválida. Digite 1 para Sim ou 2 para Não.\n")
            continuar = input("Deseja digitar mais um item? (1 - Sim / 2 - Não): ")
            print()
        
        i += 1
    
    print("Considerando duas refeições por dia (almoço e janta).")
    pergunta_dias = "Você deseja um cronograma alimentar de quantos dias? Digite: "
    resposta_dias = int(input(pergunta_dias))
    print()
        
    return ingredientes, resposta_dias, resposta_validade

def pergunta_chatgpt():
    ingredientes, resposta_dias, resposta_validade = obter_cardapio()

    montar_cardapio = ""
    for i, (ingrediente, quantidade, resposta_validade) in enumerate(ingredientes):
        montar_cardapio += f"{i+1}. Ingrediente: {ingrediente}, quantidade: {quantidade}, vencimento: {resposta_validade}\n"
    
    quantidade_informada_chatgpt = f"Será um cronograma de {resposta_dias} dias, e serão duas refeições por dia, considerando somente almoço e janta.\n"

    return quantidade_informada_chatgpt, montar_cardapio

quantidade_informada_chatgpt, montar_cardapio = pergunta_chatgpt()

pergunta_chatgpt = ("Monte um cronograma alimentar saudável e equilibrado, segue a lista dos ingredientes e suas qunatidades:\n\n"
                    f"{montar_cardapio}\n{quantidade_informada_chatgpt}\n"
                    "CRITÉRIOS IMPORTANTES:\n"
                    "- Não acrescente no cronograma nenhum ingrediente que não esteja na lista acima! Exemplo: não adicione salada, temperos, sal, azeite... (adicione somente o solicitado),\n"
                    "- Deixe os alimentos com a válidade mais proxíma (perecíveis) do vencimento nos primeiros dias,\n"
                    "- Diga a quantidade devo usar em cada refeição referente a cada alimento\n"
                    "- É obrigatório utilizar toda a quantidade fornecida na lista,\n"
                    "- Relembrando que não pode acrescentar nada que não esteja na lista!")

print("\nSegue cronograma de acordo com seus ingredientes:")
resposta_chatgpt = gpt3_responder(pergunta_chatgpt)
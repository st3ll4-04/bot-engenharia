# Importar a classe principal do SeleniumBase
from seleniumbase import SB

# Iniciar o robô
with SB() as sb:
    # Guarda o endereço
    url = "https://www.saucedemo.com/"
    # Abre o site
    sb.open(url)
    # 1. Acesso ao Site 
    #prenenche o nome do usuário
    sb.type("#user-name", "standard_user")
    #digita a senha
    sb.type("#password", "secret_sauce")
    #clica no botão de login
    sb.click("#login-button")

    
    # 2.Coleta de Dados 
    #cria a lista com os nomes e preços dos produtos
    nomes = sb.find_elements(".inventory_item_name")
    precos = sb.find_elements(".inventory_item_price")
    descricao = sb.find_elements(".inventory_item_desc")
    
    # Exibe a quantidade de produtos encontrados
    print(f"{len(nomes)}")

    #cria uma lista fazia para guardar o catálogo
    catalogo = []

    # O range cria um contador: 0, 1, 2, 3, 4, 5...
    for i in range(len(nomes)):
        # Pega o texto do nome número 'i'
        texto_nome = nomes[i].text
        # Pega o texto do preço número 'i'
        texto_preco = precos[i].text
        # Pega o textoda descrição número 'i
        texto_descricao = descricao[i].text
        # prepara o dicionário do produto atual
        produto_atual = {"nome": texto_nome, "valor": texto_preco, "descricao": texto_descricao}
        # Adiciona esse dicionário na lista principal
        catalogo.append(produto_atual)
    

    # Exibe o catálogo completo
    print("Dados salvos na memória:")
    print(catalogo)    
  

    #3. Automação de Compra

    # Adicionar todos os itens ao carrinho
    sb.click("#add-to-cart-sauce-labs-backpack")
    sb.click("#add-to-cart-sauce-labs-bike-light")
    sb.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    sb.click("#add-to-cart-sauce-labs-fleece-jacket")
    sb.click("#add-to-cart-sauce-labs-onesie")
    sb.click('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

    # Usar wait para aguardar para aguardar o botao carregar
    sb.wait_for_element(".shopping_cart_link")
    # Ir para o carrinho de comptras
    sb.click(".shopping_cart_link")
    
    # Usar wait para carregar o botao de checkout
    sb.wait_for_element("#checkout")
    # Iniciar o processo de checkout
    sb.click("#checkout")

    # Preencher o formulário
    sb.type("#first-name", "Trainee")
    sb.type("#last-name", "PiJunior")
    sb.type("#postal-code", "31270-901")

    # Usar wait para carregar o botao continue
    sb.wait_for_element("#continue")
    # Continuar para a tela de resumo
    sb.click("#continue")

    # Usar wait para carregar o botao finish
    sb.wait_for_element("#finish")
    # Finalizar compra
    sb.click("#finish")

    # Raspar informações da compra
    #CONFERIR!!!
    # Raspar as informacoes da compra
    pagamento = sb.get_text('.summary_value_label[data-test="payment-info-value"]')
    entrega = sb.get_text('.summary_value_label[data-test="shipping-info-value"]')
    valor_total = sb.get_text('.summary_total_label[data-test="total-label"]')

    print("\nInformações da compra:")
    print("Meio de pagamento:", pagamento)
    print("Forma de entrega:", entrega)
    print("Valor total:", valor_total)

    # Verificar se a compra foi concluída
    confirmacao = sb.get_text(".complete-header")

    print("\nMensagem de confirmação:")
    print(confirmacao)

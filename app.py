def calcular_taxas_shopee(valor, frete_gratis=False):
    comissao = 0.12 * valor
    taxa_transacao = 0.02 * valor

    if valor < 8:
        taxa_item = valor / 2
    else:
        taxa_item = 4

    taxa_frete_gratis = 0.06 * valor if frete_gratis else 0

    total_taxas = comissao + taxa_transacao + taxa_item + taxa_frete_gratis
    valor_liquido = valor - total_taxas
    return valor_liquido, total_taxas

def calcular_valor_venda_desejado(valor_desejado, frete_gratis=False):
    valor = valor_desejado
    for i in range(1000):  
        liquido, _ = calcular_taxas_shopee(valor, frete_gratis)
        if abs(liquido - valor_desejado) < 0.01:
            break
        valor += valor_desejado - liquido 
    return valor

def main():
    print("=== Calculadora Shopee ===\n")
    
    valor = float(input("Digite o valor de venda do produto: R$ "))
    fg = input("Vendedor no Programa Frete Grátis? (s/n): ").strip().lower() == "s"
    
    liquido, total_taxas = calcular_taxas_shopee(valor, fg)
    print(f"\nValor líquido após taxas: R$ {liquido:.2f}")
    print(f"Total de taxas cobradas: R$ {total_taxas:.2f}")
    
    valor_desejado = float(input("\nDigite o valor líquido que você quer receber: R$ "))
    valor_venda = calcular_valor_venda_desejado(valor_desejado, fg)
    print(f"Para receber R$ {valor_desejado:.2f}, você deve vender o produto por aproximadamente: R$ {valor_venda:.2f}")

if __name__ == "__main__":
    main()

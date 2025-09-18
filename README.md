# calculadora-taxa-shopee

Calculadora em Python para vendedores da Shopee. Este projeto permite:

- Calcular o **valor líquido recebido** após todas as taxas da Shopee.  
- Determinar o **preço ideal de venda** para atingir um valor líquido desejado.  
- Considerar regras do **Programa Frete Grátis** e a taxa adicional por item vendido.

O cálculo leva em conta as diretrizes oficiais da Shopee (agosto/2025):

- Comissão padrão: 12% sobre o valor do produto  
- Taxa de transação: 2% sobre o valor do produto  
- Adicional por item vendido: R$4 (ou metade do valor do produto se for menor que R$8)  
- Programa Frete Grátis: 6% sobre o valor do produto (opcional)

---

## Funcionalidades

1. **Calcular valor líquido**
   - Pergunta o valor de venda do produto.
   - Pergunta se o vendedor está no Programa Frete Grátis.
   - Retorna o valor líquido que o vendedor receberá após todas as taxas.

2. **Calcular preço ideal de venda**
   - Pergunta qual valor líquido você deseja receber.
   - Retorna o preço aproximado de venda necessário para atingir o valor líquido desejado.

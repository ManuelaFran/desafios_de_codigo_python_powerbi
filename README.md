# Desafios de código Python e Power BI - Análise de Dados

## :female_detective:_Análise de Vendas com Lista_

### Descrição:<br>
Você está trabalhando em um projeto de Power BI onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal.<br>

#### Detalhamento:<br>

Na função obter_entrada_vendas() você deverá:<br>

1. Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.<br>

2. Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.<br>

3. Usar a função list() para converter o objeto map resultante em uma lista de inteiros.<br>

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função.<br>

### Entrada<br>
Uma lista com 12 números inteiros, cada um representando o número de vendas realizadas em um mês do ano.<br>

### Saída<br>
Um único número inteiro representando o total de vendas e um número decimal representando a média mensal de vendas, separados por um espaço.<br>

### Exemplos<br>
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.<br>

| Entrada                                                    | Saída        |
|------------------------------------------------------------|--------------|
| 120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190 | 2120, 176.67 |
| 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120          | 780, 65.00   |
| 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60              | 390, 32.50   |
## Cartão Corporativo do Estado do CE (2015-2018)

* Dados recuperados do Portal da Transparência do Governo do Estado do Ceará
* Dados de gastos do cartão corporativo de responsabilidade do Chefe do Poder Executivo, período de 2015 a 2018
* Média de gastos e desvio padrão anuais
* Gráficos ilustrando os gastos do cartão corporativo

**em desenvolvimento**

### Bibliotecas

* bs4
* contextlib
* matplotlib
* numpy
* requests
* ~seaborn~

### Funções

* Para cada ano retorna (em R$): ( média, desvio padrão)
* Para cada ano um gráfico é plotado (Gastos X Mês)

### Próximos passos

* ~Melhorar saída dos resultados~
* ~Melhorar apresentação dos meses no gráfico~
* ~Salvar gráficos em .png~
* Gráfico unificado
* Refatoração

### Para executar

```

    $ python3.6 cartao_corp.py

```

### Resultado

```

	Gastos com Cartão Corporativo 2018
	Média de gastos -> R$ 2513.30
	Desvio padrão   ->    1723.37

	Gastos com Cartão Corporativo 2017
	Média de gastos -> R$ 2524.33
	Desvio padrão   ->    1865.36

	Gastos com Cartão Corporativo 2016
	Média de gastos -> R$ 1016.25
	Desvio padrão   ->    979.13

	Gastos com Cartão Corporativo 2015
	Média de gastos -> R$ 786.42
	Desvio padrão   ->    598.68

```
![Gastos 2018](images/'Gastos com Cartão Corporativo 2018.png')
![Gastos 2017](images/'Gastos com Cartão Corporativo 2017.png')
![Gastos 2016](images/'Gastos com Cartão Corporativo 2016.png')
![Gastos 2015](images/'Gastos com Cartão Corporativo 2015.png')

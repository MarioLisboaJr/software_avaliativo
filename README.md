***>>> Descrição do Problema***:

Analistas precisam constantemente extrair, transformar e carregar dados de clientes. <br>
1. Implementar módulo Extract que, utilizando Pandas:
    - Extraia dados de forma agnóstica informações de um .csv, um .json e um .xlsx
    - Retorna dados como Dicionário de arrays
    - Retorna dados como CSV
    - Retorna dados como DataFrame


2. Uma vez implementadas as classes, Extract será necessário para extrair DataFrames dos arquivos ``skus.json`` e ``sku_map.csv``. Antes módulo Transform que, utilizando Pandas, receba ambos DataFrames e os converta no relatório especificado em ``answer.csv``. O módulo Transform deve ser invocado apenas uma vez, através do seu método format(DataFrame).


3. Implementados ambos módulos, extraia ``skus.json`` e ``sku_map.csv``, aplique ``Transform.format(<skus>, <sku_map>)`` e salve o resultado em uma planilha .csv. O resultado deve ser idêntico a ``answer.csv``


<hr>

***>>> Solução***

**Instalação**:

```pip install git+https://github.com/MarioLisboaJr/software_avaliativo.git#subdirectory=packages```


<hr>

### packages.fourmatt.extract.[Extract](https://github.com/MarioLisboaJr/software_avaliativo/blob/main/packages/fourmatt/extract.py)

classe packages.fourmatt.extract.**Extract(arquivo, **kwargs)**

Extrai dados de forma agnóstica de arquivos csv, json, xls, xlsx, xlsm, xlsb, odf, ods e odt. <br>

**Parâmetros**:

- `arquivo`: **str**, qualquer caminho de ‘string’ válido é aceitável.


- `**kwargs`: propiedade de pandas.read_csv, pandas.read_json ou pandas.read_excel, a depender da extensão do arquivo.

**Atributo**:

- `df`: **objeto pandas**, retorna o arquivo convertido em um DataFrame.

**Métodos**:

- `to_dict(**kwargs)`: converta arquivo num dicionário.

    - **Parâmetro**: **kwargs, propiedade de pandas.DataFrame.to_dict
    - **Devolução**: **dict**, arquivo formatado como dicionário.


- `to_csv(**kwargs)`: converta arquivo num arquivo de valores separado por vírgula (csv).

    - **Parâmetro**: **kwargs, propiedade de pandas.DataFrame.to_csv
    - **Devolução**: **dict**, arquivo formatado como CSV.

<hr>

### packages.fourmatt.transform.[format](https://github.com/MarioLisboaJr/software_avaliativo/blob/main/packages/fourmatt/transform.py)

método packages.fourmatt.transform.**format(skus, sku_map)**

Utiliza arquivos skus e sku_map para criar relatório especificado em answer.csv.

**Parâmetros**:

- `skus`: **pandas DataFrame**, arquivo skus convertido num objeto pandas.


- `sku_map`: **pandas DataFrame**, arquivo sku_map convertido num objeto pandas.

**Devolução**:

- pandas Dataframe, relatório especificado num objeto pandas.


<hr>

**[Aplicação](https://github.com/MarioLisboaJr/software_avaliativo/blob/main/script.py)**:

```python
from fourmatt.extract import Extract
import fourmatt.transform as transform

# codificacao do arquivo sku_map.csv é ANSI
# codificacao do arquivo skus.json é UTF-8
# referencia para codificacao https://docs.python.org/3/library/codecs.html#text-encodings
sku_map = Extract('sku_map.csv', encoding='mbcs')
skus = Extract('skus.json')

# exemplo de converção em dicionário de arrays
skus_dict_arrays = skus.to_dict(orient='list')
# exemplo de conversão em csv
skus_csv = skus.to_csv(index=False)

resultado = transform.format(skus.df, sku_map.df)

# salvar resultado em uma planilha .csv
resultado.to_csv('resultado.csv', index=False)

# comparar se o relatorio gerado é igual ao modelo
answer = Extract('answer.csv').df
resultado = Extract('resultado.csv').df
print(answer.equals(resultado))
```

`>>> True`


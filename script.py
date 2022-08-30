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

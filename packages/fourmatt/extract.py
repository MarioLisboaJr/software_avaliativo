import pandas as pd


class Extract:
    """
    Extrai dados de forma agnóstica de arquivos csv, json, xls, xlsx, xlsm, xlsb, odf, ods e odt.

    Parâmetros
    ----------
    - arquivo: str, qualquer caminho de ‘string’ válido é aceitável.
    - **kwargs: propiedade de pandas.read_csv, pandas.read_json ou pandas.read_excel, a depender da extensão do arquivo.
    Atributo
    ----------
    - df: objeto pandas, retorna o arquivo convertido em um DataFrame.
    Métodos
    ----------
    - to_dict(**kwargs): converta arquivo num dicionário.
    - to_csv(**kwargs): converta arquivo num arquivo de valores separado por vírgula (csv).
    """
    def __init__(self, arquivo, **kwargs):

        self._arquivo = arquivo
        self._extension = self._extension()

        # importar arquivo em um DataFrame do pandas
        if self._extension == 'csv':
            dataframe = pd.read_csv(self._arquivo, **kwargs)
        elif self._extension == 'json':
            dataframe = pd.read_json(self._arquivo, **kwargs)
        else:
            dataframe = pd.read_excel(self._arquivo, **kwargs)

        self.df = dataframe

    def _extension(self):
        """
        Checa se a extensão do arquivo é válida.

        :return: str, extenção do arquivo.
        """
        supported_extension = ['csv', 'json', 'xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']
        point_position = self._arquivo.rfind('.')
        extension = self._arquivo[point_position + 1:]
        if extension not in supported_extension:
            raise ImportError('Arquivo nao suportado. Suporta extensoes csv,json,xls,xlsx,xlsm,xlsb,odf,ods,odt.')
        else:
            return extension

    def to_dict(self, **kwargs):
        """
        Converta DataFrame em Dicionário.

        :param kwargs: propiedade de pandas.DataFrame.to_dict
        :return: dict, arquivo formatado como dicionário.
        """
        dictionary = self.df.to_dict(**kwargs)
        return dictionary

    def to_csv(self, **kwargs):
        """
        Grava o objeto num arquivo de valores separados por vírgula (csv).

        :param kwargs: propiedade de pandas.DataFrame.to_csv
        :return: str, arquivo formatado como CSV.
        """
        csv = self.df.to_csv(**kwargs)
        return csv

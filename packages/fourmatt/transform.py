def format(skus, sku_map):
    """
    Utiliza arquivos skus e sku_map para criar relatório especificado em answer.csv.

    :param skus: pandas DataFrame, arquivo skus convertido num objeto pandas.
    :param sku_map: pandas DataFrame, arquivo sku_map convertido num objeto pandas.
    :return: pandas Dataframe, relatório especificado num objeto pandas.
    """
    # left join skus on skus.skuid = sku_map.guid
    df = skus.merge(
        right=sku_map[['GUID', 'Product_Display_Name']].drop_duplicates(),
        how='left',
        left_on='skuId',
        right_on='GUID'
    )

    # organizar relatório
    df = df[['Product_Display_Name', 'skuPartNumber', 'prepaidUnits.enabled', 'consumedUnits', 'capabilityStatus']]
    df = df.rename(columns={
        'Product_Display_Name': 'titulo_do_produto',
        'skuPartNumber': 'sku_part_number',
        'prepaidUnits.enabled': 'total_de_licencas',
        'consumedUnits': 'licencas_atribuidas',
        'capabilityStatus': 'mensagem_de_status'
    })

    return df

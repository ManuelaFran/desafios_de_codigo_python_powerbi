def analise_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

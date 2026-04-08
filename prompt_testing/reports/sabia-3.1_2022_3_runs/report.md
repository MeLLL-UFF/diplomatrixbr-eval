f# Relatório de Avaliação: {model}-{model_version} - {num_runs} execuções
**Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo {model} em diferentes prompts/temperaturas versus a correção humana.

![Distribuição de Notas](distribuicao_notas.png)

## 2. Comparação de Notas Geradas e Humanas
Nesta seção, apresentamos a comparação entre as notas finais geradas pelo modelo e as notas dadas por avaliadores humanos.

![Comparação Notas](comparacao_notas.png)

## 3. Análise de Erro Absoluto de Validação

<table>
  <tr>
    <td>
      <img src="area_val_error.png" width="700">
    </td>
    <td>
      {df_area_sob_grafico.to_html(index=False, justify="center")}
    </td>
  </tr>
</table>

## 4. Análise de Erros Gramaticais
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Comparação de Número de Erros](comparacao_num_erros.png)

## 5. Correlação de Pearson
{df_notas_normalizado.corr(method='pearson').to_markdown()}

## 6. Correlação de Spearman
{df_notas_normalizado.corr(method='spearman').to_markdown()}

## Estatísticas Descritivas
### Modelo {model}-{model_version}
{df_eval.describe().to_markdown()}

### Humano
{df_human.describe().to_markdown()}

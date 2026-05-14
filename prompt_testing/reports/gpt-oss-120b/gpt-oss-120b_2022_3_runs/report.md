# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 14/05/2026 09:20:46**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo gpt-oss-120b em diferentes prompts/temperaturas versus a correção humana.

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
      <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: center;">
      <th>prompt</th>
      <th>temp</th>
      <th>area_sob_curva</th>
      <th>mae</th>
      <th>rmse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7</td>
      <td>0.0</td>
      <td>89.80</td>
      <td>17.2333</td>
      <td>17.8541</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>6.35</td>
      <td>1.2500</td>
      <td>1.5138</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>36.90</td>
      <td>7.2333</td>
      <td>7.3652</td>
    </tr>
  </tbody>
</table>
    </td>
  </tr>
</table>

## 4. Análise de RMSE por Prompt e Temperatura
Nesta seção, apresentamos o heatmap de RMSE calculado por combinação de prompt e temperatura.

![Heatmap RMSE](RMSE_notas_heatmap.png)

## 5. Análise de Erros Gramaticais
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Comparação de Número de Erros](comparacao_num_erros.png)

## 6. Correlações
![Correlações](correlacoes.png)

## Estatísticas Descritivas
### Modelo gpt-oss-120b
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |       1A |      1B |       1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|---------:|--------:|---------:|---------:|-------------:|
| count | 18        |     18 |  18       |     18       |               18 | 6        | 6       |  6       |  6       |     18       |
| mean  |  8        |      0 |   3.5     |     48.3278  |                0 | 7.83333  | 7.5     | 14.6667  |  9.16667 |      7.72222 |
| std   |  0.840168 |      0 |   1.75734 |      7.93642 |                0 | 0.408248 | 0.83666 |  1.63299 |  2.73983 |      8.47005 |
| min   |  7        |      0 |   1       |     34.5     |                0 | 7        | 7       | 12       |  5.9     |      0       |
| 25%   |  7        |      0 |   2       |     42.3     |                0 | 8        | 7       | 14.25    |  7.725   |      3       |
| 50%   |  8        |      0 |   3.5     |     50       |                0 | 8        | 7       | 15       |  8.4     |      3       |
| 75%   |  9        |      0 |   5       |     56.325   |                0 | 8        | 7.75    | 15       | 10.65    |     12       |
| max   |  9        |      0 |   6       |     57.3     |                0 | 8        | 9       | 17       | 13.4     |     27       |

### Humano
|       |   redacao |   nota_final |        1A |        1B |        1C |      CGPL |   num_errors |
|:------|----------:|-------------:|----------:|----------:|----------:|----------:|-------------:|
| count |   6       |      6       |  6        |  6        |  6        |  6        |     6        |
| mean  |   3.5     |     56.4     |  9.75     |  9.75     | 18.5      | 18.4      |     0.333333 |
| std   |   1.87083 |      1.24258 |  0.273861 |  0.273861 |  0.447214 |  0.532917 |     0.516398 |
| min   |   1       |     54.7     |  9.5      |  9.5      | 18        | 17.7      |     0        |
| 25%   |   2.25    |     55.625   |  9.5      |  9.5      | 18.125    | 18.05     |     0        |
| 50%   |   3.5     |     56.35    |  9.75     |  9.75     | 18.5      | 18.35     |     0        |
| 75%   |   4.75    |     57.3     | 10        | 10        | 18.875    | 18.875    |     0.75     |
| max   |   6       |     58       | 10        | 10        | 19        | 19        |     1        |

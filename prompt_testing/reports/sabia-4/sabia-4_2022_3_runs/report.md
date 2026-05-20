# Relatório de Avaliação: sabia-4 - 3 execuções
**Gerado em: 20/05/2026 13:29:09**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo sabia-4 em diferentes prompts/temperaturas versus a correção humana.

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
      <td>17.9668</td>
      <td>3.6334</td>
      <td>3.9886</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>8.6666</td>
      <td>1.7500</td>
      <td>1.8672</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>31.9000</td>
      <td>6.4000</td>
      <td>6.4997</td>
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
### Modelo sabia-4
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |   1A |       1B |        1C |      CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|-----:|---------:|----------:|----------:|-------------:|
| count | 18        |     18 |  18       |      18      |        18        |    6 | 6        |  6        |  6        |    18        |
| mean  |  8        |      0 |   3.5     |      53.0981 |         0.234156 |    9 | 9.1111   | 17.6111   | 17.0445   |     1.74074  |
| std   |  0.840168 |      0 |   1.75734 |       2.9401 |         0.399258 |    0 | 0.172115 |  0.490654 |  0.656136 |     0.812932 |
| min   |  7        |      0 |   1       |      50      |         0        |    9 | 9        | 17        | 16.1      |     1        |
| 25%   |  7        |      0 |   2       |      50      |         0        |    9 | 9        | 17.1667   | 16.6417   |     1        |
| 50%   |  8        |      0 |   3.5     |      53.0667 |         0        |    9 | 9        | 17.8333   | 17.0833   |     1.66665  |
| 75%   |  9        |      0 |   5       |      55.3833 |         0.47635  |    9 | 9.24997  | 18        | 17.625    |     2        |
| max   |  9        |      0 |   6       |      57.8333 |         1.1547   |    9 | 9.3333   | 18        | 17.7      |     3        |

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

# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 21/05/2026 08:50:41**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo gemma-4-31B-it em diferentes prompts/temperaturas versus a correção humana.

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
      <td>33.225</td>
      <td>3.91</td>
      <td>4.4191</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>28.775</td>
      <td>3.24</td>
      <td>4.4613</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>25.475</td>
      <td>3.16</td>
      <td>4.5463</td>
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
### Modelo gemma-4-31B-it
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |        1A |       1B |       1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|----------:|---------:|---------:|---------:|-------------:|
| count | 30        |     30 |  30       |      30      |               30 | 10        | 10       | 10       | 10       |     30       |
| mean  |  8        |      0 |   5.5     |      52.9167 |                0 |  8.65     |  8.25    |  7.65    | 27.7     |      1.71111 |
| std   |  0.830455 |      0 |   2.92138 |       4.117  |                0 |  0.914391 |  1.03414 |  1.39543 |  1.25167 |      1.33831 |
| min   |  7        |      0 |   1       |      42      |                0 |  7        |  7       |  6       | 26       |      0       |
| 25%   |  7        |      0 |   3       |      50      |                0 |  8.5      |  7.25    |  6.25    | 27       |      0       |
| 50%   |  8        |      0 |   5.5     |      54      |                0 |  8.5      |  8.25    |  7.75    | 28       |      2       |
| 75%   |  9        |      0 |   8       |      55.375  |                0 |  9.375    |  9       |  8.5     | 28       |      3       |
| max   |  9        |      0 |  10       |      60      |                0 | 10        | 10       | 10       | 30       |      4       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |  10       |     10       |      10      |
| mean  |   5.5     |     52.66    |       1.6    |
| std   |   3.02765 |      2.19669 |       1.7127 |
| min   |   1       |     48       |       0      |
| 25%   |   3.25    |     51.525   |       1      |
| 50%   |   5.5     |     52.875   |       1      |
| 75%   |   7.75    |     54.5     |       2      |
| max   |  10       |     55.25    |       6      |

# Relatório de Avaliação: Qwen3.6-35B-A3B - 3 execuções
**Gerado em: 21/05/2026 08:53:07**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo Qwen3.6-35B-A3B em diferentes prompts/temperaturas versus a correção humana.

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
      <td>30.425</td>
      <td>6.3083</td>
      <td>6.5252</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>21.925</td>
      <td>4.6417</td>
      <td>5.1108</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>38.425</td>
      <td>8.4750</td>
      <td>9.2374</td>
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
### Modelo Qwen3.6-35B-A3B
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |       1A |       1B |       1C |   CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|---------:|---------:|---------:|-------:|-------------:|
| count | 18        |     18 |  18       |     18       |       18         | 6        | 6        | 6        |      6 |     18       |
| mean  |  8        |      0 |   3.5     |     47.1111  |        0.0481111 | 7.08333  | 6.13888  | 6.27778  |     26 |      2.38889 |
| std   |  0.840168 |      0 |   1.75734 |      3.53368 |        0.204118  | 0.204124 | 0.221521 | 0.443059 |      0 |      1.85151 |
| min   |  7        |      0 |   1       |     45       |        0         | 7        | 6        | 6        |     26 |      0       |
| 25%   |  7        |      0 |   2       |     45       |        0         | 7        | 6        | 6        |     26 |      0       |
| 50%   |  8        |      0 |   3.5     |     45.5     |        0         | 7        | 6        | 6        |     26 |      3.5     |
| 75%   |  9        |      0 |   5       |     47.5     |        0         | 7        | 6.24998  | 6.50002  |     26 |      4       |
| max   |  9        |      0 |   6       |     57.5     |        0.866     | 7.5      | 6.5      | 7        |     26 |      4       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |   6       |      6       |      6       |
| mean  |   3.5     |     49.8583  |      1.83333 |
| std   |   1.87083 |      5.53809 |      1.16905 |
| min   |   1       |     39.15    |      0       |
| 25%   |   2.25    |     49.5     |      1.25    |
| 50%   |   3.5     |     52.25    |      2       |
| 75%   |   4.75    |     52.75    |      2.75    |
| max   |   6       |     54       |      3       |

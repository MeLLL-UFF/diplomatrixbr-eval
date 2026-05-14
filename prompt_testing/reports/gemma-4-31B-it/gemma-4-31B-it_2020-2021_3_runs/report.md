# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 14/05/2026 18:24:38**

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
      <td>18.5500</td>
      <td>3.9000</td>
      <td>4.3882</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>22.2166</td>
      <td>4.3056</td>
      <td>4.6107</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>23.0500</td>
      <td>4.7500</td>
      <td>5.7404</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |        1A |        1B |       1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|----------:|----------:|---------:|---------:|-------------:|
| count | 18        |     18 |  18       |     18       |       18         |  6        |  6        |  6       |  6       |     18       |
| mean  |  8        |      0 |   3.5     |     54.3759  |        0.0160389 |  9.16667  |  9.33333  | 18.5     | 17.85    |      1.11111 |
| std   |  0.840168 |      0 |   1.75734 |      2.64913 |        0.0680472 |  0.408248 |  0.516398 |  0.83666 |  1.09864 |      1.2314  |
| min   |  7        |      0 |   1       |     50       |        0         |  9        |  9        | 18       | 17.1     |      0       |
| 25%   |  7        |      0 |   2       |     53.1     |        0         |  9        |  9        | 18       | 17.1     |      0       |
| 50%   |  8        |      0 |   3.5     |     54.0833  |        0         |  9        |  9        | 18       | 17.25    |      1       |
| 75%   |  9        |      0 |   5       |     55       |        0         |  9        |  9.75     | 18.75    | 18.375   |      2       |
| max   |  9        |      0 |   6       |     60       |        0.2887    | 10        | 10        | 20       | 19.7     |      3       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |   6       |      6       |      6       |
| mean  |   3.5     |     58.4167  |      1.66667 |
| std   |   1.87083 |      1.06474 |      2.73252 |
| min   |   1       |     56.4     |      0       |
| 25%   |   2.25    |     58.425   |      0       |
| 50%   |   3.5     |     58.6     |      0.5     |
| 75%   |   4.75    |     58.925   |      1.75    |
| max   |   6       |     59.5     |      7       |

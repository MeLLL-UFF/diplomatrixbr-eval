# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 21/05/2026 08:51:11**

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
      <td>40.6834</td>
      <td>6.8278</td>
      <td>12.0420</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>19.6500</td>
      <td>3.6500</td>
      <td>6.0475</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>25.5000</td>
      <td>4.5000</td>
      <td>7.1935</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |      1A |       1B |      1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|--------:|---------:|--------:|---------:|-------------:|
| count | 18        |     18 |  18       |     18       |        18        | 6       |  6       |  6      |  6       |     18       |
| mean  |  8        |      0 |   3.5     |     52.0852  |         0.266222 | 8.44445 |  9.02778 | 16.3333 | 15.8667  |      1.35185 |
| std   |  0.840168 |      0 |   1.75734 |      7.81841 |         1.12949  | 1.14827 |  1.52904 |  4.2269 |  4.34312 |      2.0178  |
| min   |  7        |      0 |   1       |     28.4     |         0        | 7       |  6       |  8      |  7.4     |      0       |
| 25%   |  7        |      0 |   2       |     54.125   |         0        | 7.5     |  9.125   | 16.5    | 15.775   |      0       |
| 50%   |  8        |      0 |   3.5     |     55       |         0        | 9       |  9.58335 | 18      | 17.9     |      0       |
| 75%   |  9        |      0 |   5       |     55.6     |         0        | 9       |  9.91667 | 18.75   | 18       |      2       |
| max   |  9        |      0 |   6       |     60       |         4.792    | 9.6667  | 10       | 19      | 18.9     |      7       |

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

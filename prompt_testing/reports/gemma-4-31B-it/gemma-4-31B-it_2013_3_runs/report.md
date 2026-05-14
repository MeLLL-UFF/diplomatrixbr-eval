# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 14/05/2026 18:23:33**

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
      <td>27.225</td>
      <td>11.0875</td>
      <td>14.5367</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>16.425</td>
      <td>6.8375</td>
      <td>10.9239</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>16.425</td>
      <td>7.2125</td>
      <td>11.3553</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |    1A |    1B |   1C |      CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|------:|------:|-----:|----------:|-------------:|
| count | 12        |     12 |  12       |     12       |               12 |  4    |  4    |  4   |  4        |     12       |
| mean  |  8        |      0 |   2.5     |     54.75    |                0 |  9.75 |  9.75 | 19.5 | 19.125    |      1.16667 |
| std   |  0.852803 |      0 |   1.16775 |      3.51503 |                0 |  0.5  |  0.5  |  1   |  0.991211 |      1.11464 |
| min   |  7        |      0 |   1       |     50       |                0 |  9    |  9    | 18   | 17.7      |      0       |
| 25%   |  7        |      0 |   1.75    |     52       |                0 |  9.75 |  9.75 | 19.5 | 18.975    |      0       |
| 50%   |  8        |      0 |   2.5     |     54.5     |                0 | 10    | 10    | 20   | 19.4      |      1.5     |
| 75%   |  9        |      0 |   3.25    |     57.225   |                0 | 10    | 10    | 20   | 19.55     |      2       |
| max   |  9        |      0 |   4       |     60       |                0 | 10    | 10    | 20   | 20        |      3       |

### Humano
|       |   redacao |   nota_final |
|:------|----------:|-------------:|
| count |   4       |      4       |
| mean  |   2.5     |     47.0375  |
| std   |   1.29099 |      9.61192 |
| min   |   1       |     32.65    |
| 25%   |   1.75    |     46.4125  |
| 50%   |   2.5     |     51.5     |
| 75%   |   3.25    |     52.125   |
| max   |   4       |     52.5     |

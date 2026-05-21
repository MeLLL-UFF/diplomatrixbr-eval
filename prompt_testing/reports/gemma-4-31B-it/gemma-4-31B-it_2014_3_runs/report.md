# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 21/05/2026 08:50:29**

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
      <td>79.7917</td>
      <td>4.6898</td>
      <td>5.5009</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>79.7083</td>
      <td>4.7546</td>
      <td>5.9395</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>65.1250</td>
      <td>3.9028</td>
      <td>4.9248</td>
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
| count | 54        |     54 |  54       |     54       |        54        | 18        | 18       | 18       | 18       |     54       |
| mean  |  8        |      0 |   9.5     |     50.9722  |         0.315407 |  8.26852  |  7.63889 |  7.08334 | 27.6852  |      1.7284  |
| std   |  0.824163 |      0 |   5.23684 |      3.34475 |         1.78857  |  0.882179 |  1.01178 |  1.09701 |  1.56545 |      1.43346 |
| min   |  7        |      0 |   1       |     42.5     |         0        |  6.3333   |  6       |  5       | 24       |      0       |
| 25%   |  7        |      0 |   5       |     50       |         0        |  7.5      |  7.125   |  7       | 27       |      0       |
| 50%   |  8        |      0 |   9.5     |     50.5833  |         0        |  8.5      |  8       |  7.5     | 28       |      2       |
| 75%   |  9        |      0 |  14       |     54.5     |         0        |  8.5      |  8       |  7.5     | 28       |      3       |
| max   |  9        |      0 |  18       |     56       |        12.9904   |  9.5      |  9       |  9       | 30       |      6       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |  18       |     18       |     18       |
| mean  |   9.5     |     47.6806  |      2.11111 |
| std   |   5.33854 |      4.67928 |      1.71117 |
| min   |   1       |     38       |      0       |
| 25%   |   5.25    |     46.75    |      1       |
| 50%   |   9.5     |     49       |      2       |
| 75%   |  13.75    |     50.75    |      3       |
| max   |  18       |     53.25    |      6       |

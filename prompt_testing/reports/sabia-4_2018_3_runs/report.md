# Relatório de Avaliação: sabia-4 - 3 execuções
**Gerado em: 08/05/2026 01:38:44**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo sabia em diferentes prompts/temperaturas versus a correção humana.

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
      <td>12.5583</td>
      <td>3.1139</td>
      <td>5.2982</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.2</td>
      <td>13.5584</td>
      <td>3.3361</td>
      <td>5.5453</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.5</td>
      <td>12.8417</td>
      <td>3.2250</td>
      <td>5.5235</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>26.9250</td>
      <td>5.9750</td>
      <td>7.5014</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.2</td>
      <td>24.8415</td>
      <td>5.6416</td>
      <td>7.3532</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.5</td>
      <td>25.3416</td>
      <td>5.6972</td>
      <td>7.3834</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>15.9250</td>
      <td>3.8917</td>
      <td>5.0575</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.2</td>
      <td>15.9250</td>
      <td>3.8917</td>
      <td>5.0575</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.5</td>
      <td>15.9250</td>
      <td>3.8917</td>
      <td>5.0575</td>
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
|       |    prompt |      temp |   redacao |   nota_final |   nota_final_std |   1A |   1B |        1C |      CGPL |   num_errors |
|:------|----------:|----------:|----------:|-------------:|-----------------:|-----:|-----:|----------:|----------:|-------------:|
| count | 54        | 54        |  54       |     54       |        54        |   18 |   18 | 18        | 18        |    54        |
| mean  |  8        |  0.233333 |   3.5     |     52.8049  |         0.275363 |    9 |    9 | 17.7037   | 17.0815   |     1.75926  |
| std   |  0.824163 |  0.20741  |   1.72386 |      2.47458 |         0.438456 |    0 |    0 |  0.410471 |  0.667968 |     0.842817 |
| min   |  7        |  0        |   1       |     50       |         0        |    9 |    9 | 17        | 15.9      |     0.6667   |
| 25%   |  7        |  0        |   2       |     50       |         0        |    9 |    9 | 17.3333   | 16.4333   |     1        |
| 50%   |  8        |  0.2      |   3.5     |     53.4     |         0        |    9 |    9 | 18        | 17.4      |     1.5      |
| 75%   |  9        |  0.5      |   5       |     54.4583  |         0.2887   |    9 |    9 | 18        | 17.6      |     2.24998  |
| max   |  9        |  0.5      |   6       |     56.8333  |         1.4434   |    9 |    9 | 18        | 17.7      |     3.6667   |

### Humano
|       |   redacao |   nota_final |
|:------|----------:|-------------:|
| count |   6       |      6       |
| mean  |   3.5     |     49.8583  |
| std   |   1.87083 |      5.53809 |
| min   |   1       |     39.15    |
| 25%   |   2.25    |     49.5     |
| 50%   |   3.5     |     52.25    |
| 75%   |   4.75    |     52.75    |
| max   |   6       |     54       |

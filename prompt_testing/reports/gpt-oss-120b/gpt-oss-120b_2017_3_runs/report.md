# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 21/05/2026 08:51:54**

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
      <td>28384.85</td>
      <td>2839.84</td>
      <td>8941.4475</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>94.15</td>
      <td>10.89</td>
      <td>12.1616</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>27.20</td>
      <td>3.34</td>
      <td>3.8602</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |       1A |       1B |       1C |      CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|---------:|---------:|---------:|----------:|-------------:|
| count | 30        |     30 |  30       |        30    |               30 | 10       | 10       | 10       |     10    |       30     |
| mean  |  8        |      0 |   5.5     |      -895.71 |                0 |  5.9     |  5.83    |  4.94    |  -2810.1  |      947.967 |
| std   |  0.830455 |      0 |   2.92138 |      5162.31 |                0 |  3.12517 |  3.63625 |  2.86015 |   8939.38 |     5162.58  |
| min   |  7        |      0 |   1       |    -28228.3  |                0 |  0       |  0       |  0       | -28252    |        0     |
| 25%   |  7        |      0 |   3       |        38.25 |                0 |  7       |  3.25    |  5       |      4.25 |        0     |
| 50%   |  8        |      0 |   5.5     |        50    |                0 |  7.25    |  8       |  5       |     15    |        2     |
| 75%   |  9        |      0 |   8       |        57.3  |                0 |  7.5     |  8       |  6.875   |     27    |       10.25  |
| max   |  9        |      0 |  10       |        57.3  |                0 |  8       |  9       |  8       |     30    |    28282     |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |  10       |      10      |     10       |
| mean  |   5.5     |      46.41   |      1.1     |
| std   |   3.02765 |       5.707  |      1.28668 |
| min   |   1       |      31.35   |      0       |
| 25%   |   3.25    |      46.8125 |      0       |
| 50%   |   5.5     |      47.25   |      0.5     |
| 75%   |   7.75    |      47.875  |      2       |
| max   |  10       |      53.75   |      3       |

# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 21/05/2026 08:51:48**

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
      <td>1.515154e+08</td>
      <td>15151539.900</td>
      <td>4.791330e+07</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>4.075500e+01</td>
      <td>4.644</td>
      <td>5.091900e+00</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>8.947500e+01</td>
      <td>10.110</td>
      <td>1.098260e+01</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |       1A |       1B |       1C |         CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|---------:|---------:|---------:|-------------:|-------------:|
| count | 30        |     30 |  30       | 30           |               30 | 10       | 10       | 10       | 10           | 30           |
| mean  |  8        |      0 |   5.5     | -5.05046e+06 |                0 |  4.9     |  5.43    |  5.03    | -1.51515e+07 |  5.05051e+06 |
| std   |  0.830455 |      0 |   2.92138 |  2.76628e+07 |                0 |  2.79682 |  2.90672 |  2.21312 |  4.79133e+07 |  2.76628e+07 |
| min   |  7        |      0 |   1       | -1.51515e+08 |                0 |  0       |  0       |  1       | -1.51515e+08 |  0           |
| 25%   |  7        |      0 |   3       | 32.6         |                0 |  5       |  3       |  4.25    |  2           |  2           |
| 50%   |  8        |      0 |   5.5     | 40           |                0 |  5       |  7       |  5.15    |  5.5         |  3.5         |
| 75%   |  9        |      0 |   8       | 57.3         |                0 |  7       |  7.75    |  6.75    | 15.5         | 15           |
| max   |  9        |      0 |  10       | 60           |                0 |  7.5     |  8.3     |  8       | 30           |  1.51515e+08 |

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

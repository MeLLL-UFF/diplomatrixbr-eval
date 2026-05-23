# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 21/05/2026 08:51:42**

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
      <td>207.15</td>
      <td>14.0594</td>
      <td>15.0092</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>202.35</td>
      <td>13.4281</td>
      <td>14.3905</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>101.10</td>
      <td>6.7531</td>
      <td>7.7972</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |       1A |       1B |       1C |    CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|---------:|---------:|---------:|--------:|-------------:|
| count | 48        |     48 |  48       |      48      |               48 | 16       | 16       | 16       | 16      |     48       |
| mean  |  8        |      0 |   8.5     |      45.4958 |                0 |  3.625   |  3.6875  |  2.625   | 19.875  |      5.47917 |
| std   |  0.825137 |      0 |   4.65855 |      12.216  |                0 |  3.75722 |  3.87675 |  2.72947 | 10.7696 |      7.59896 |
| min   |  7        |      0 |   1       |      19      |                0 |  0       |  0       |  0       |  2      |      0       |
| 25%   |  7        |      0 |   4.75    |      33.75   |                0 |  0       |  0       |  0       | 13.25   |      0       |
| 50%   |  8        |      0 |   8.5     |      50      |                0 |  3.5     |  2.5     |  2.5     | 21.5    |      2       |
| 75%   |  9        |      0 |  12.25    |      57.3    |                0 |  7       |  8       |  5       | 30      |      5       |
| max   |  9        |      0 |  16       |      60      |                0 |  8       |  8       |  6       | 30      |     28       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |  16       |     16       |     16       |
| mean  |   8.5     |     43.8719  |      1.6875  |
| std   |   4.76095 |      5.34397 |      1.01448 |
| min   |   1       |     35.35    |      0       |
| 25%   |   4.75    |     40.25    |      1       |
| 50%   |   8.5     |     43.5     |      2       |
| 75%   |  12.25    |     46.5     |      2       |
| max   |  16       |     54.25    |      4       |

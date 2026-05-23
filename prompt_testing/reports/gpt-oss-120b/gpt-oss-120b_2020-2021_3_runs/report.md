# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 21/05/2026 08:52:12**

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
      <td>123.48</td>
      <td>24.5433</td>
      <td>28.5853</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>6.95</td>
      <td>1.4167</td>
      <td>1.4804</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>42.55</td>
      <td>8.4167</td>
      <td>8.4726</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |      1A |       1B |       1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|--------:|---------:|---------:|---------:|-------------:|
| count | 18        |     18 |  18       |      18      |               18 | 6       |  6       |  6       |  6       |     18       |
| mean  |  8        |      0 |   3.5     |      47.0578 |                0 | 4.13333 |  4.65    |  6.94    | 18.15    |      2.94444 |
| std   |  0.840168 |      0 |   1.75734 |      13.0544 |                0 | 4.59638 |  5.30424 |  7.67656 |  2.94194 |      5.86588 |
| min   |  7        |      0 |   1       |      20      |                0 | 0       |  0       |  0       | 13.4     |      0       |
| 25%   |  7        |      0 |   2       |      48.755  |                0 | 0       |  0       |  0       | 16.625   |      0       |
| 50%   |  8        |      0 |   3.5     |      50      |                0 | 3.5     |  3.95    |  6.07    | 20       |      2       |
| 75%   |  9        |      0 |   5       |      57.3    |                0 | 7.975   |  7.975   | 13.535   | 20       |      2       |
| max   |  9        |      0 |   6       |      57.3    |                0 | 9.5     | 12       | 15.5     | 20       |     22       |

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

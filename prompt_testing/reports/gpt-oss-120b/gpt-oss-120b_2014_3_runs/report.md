# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 21/05/2026 08:51:35**

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
      <td>287.825</td>
      <td>16.6361</td>
      <td>17.3679</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>161.475</td>
      <td>9.6194</td>
      <td>10.6402</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>62.125</td>
      <td>4.1528</td>
      <td>6.7043</td>
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
| count | 54        |     54 |  54       |      54      |               54 | 18       | 18       | 18       | 18      |     54       |
| mean  |  8        |      0 |   9.5     |      46.3    |                0 |  3.88889 |  4.40556 |  3.13889 | 19.6111 |      5.38889 |
| std   |  0.824163 |      0 |   5.23684 |      11.7195 |                0 |  3.6564  |  4.12403 |  2.98607 | 10.8473 |      7.85822 |
| min   |  7        |      0 |   1       |      23      |                0 |  0       |  0       |  0       |  2      |      0       |
| 25%   |  7        |      0 |   5       |      35.75   |                0 |  0       |  0       |  0       | 15      |      0       |
| 50%   |  8        |      0 |   9.5     |      50      |                0 |  5.25    |  7       |  5       | 18      |      2       |
| 75%   |  9        |      0 |  14       |      57.3    |                0 |  7       |  7.75    |  5       | 30      |      5       |
| max   |  9        |      0 |  18       |      60      |                0 |  8       |  9.3     |  8.2     | 30      |     28       |

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

# Relatório de Avaliação: Qwen3.6-35B-A3B - 3 execuções
**Gerado em: 21/05/2026 08:52:35**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo Qwen3.6-35B-A3B em diferentes prompts/temperaturas versus a correção humana.

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
      <td>14.425</td>
      <td>6.4625</td>
      <td>10.3123</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>30.550</td>
      <td>11.6500</td>
      <td>14.2558</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>18.925</td>
      <td>7.2125</td>
      <td>7.9651</td>
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
### Modelo Qwen3.6-35B-A3B
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |   1A |      1B |      1C |   CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|-----:|--------:|--------:|-------:|-------------:|
| count | 12        |     12 |  12       |     12       |       12         |  4   | 4       | 4       |   4    |    12        |
| mean  |  8        |      0 |   2.5     |     52.3125  |        0.0721667 |  8.5 | 7.79167 | 8.20833 |  26.25 |     3.25     |
| std   |  0.852803 |      0 |   1.16775 |      5.61464 |        0.249993  |  0   | 0.58335 | 0.41665 |   0.5  |     0.866025 |
| min   |  7        |      0 |   1       |     45       |        0         |  8.5 | 7.5     | 8       |  26    |     2        |
| 25%   |  7        |      0 |   1.75    |     48.75    |        0         |  8.5 | 7.5     | 8       |  26    |     3        |
| 50%   |  8        |      0 |   2.5     |     51.5     |        0         |  8.5 | 7.5     | 8       |  26    |     3        |
| 75%   |  9        |      0 |   3.25    |     58.5625  |        0         |  8.5 | 7.79167 | 8.20833 |  26.25 |     4        |
| max   |  9        |      0 |   4       |     58.75    |        0.866     |  8.5 | 8.6667  | 8.8333  |  27    |     5        |

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

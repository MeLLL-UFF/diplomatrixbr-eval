# Relatório de Avaliação: Qwen3.6-35B-A3B - 3 execuções
**Gerado em: 21/05/2026 08:53:00**

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
      <td>48.2833</td>
      <td>5.7233</td>
      <td>7.3842</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>100.7000</td>
      <td>11.1900</td>
      <td>11.5726</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>49.9500</td>
      <td>5.7400</td>
      <td>6.8776</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |        1A |       1B |       1C |    CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|----------:|---------:|---------:|--------:|-------------:|
| count | 30        |     30 |  30       |     30       |       30         | 10        | 10       | 10       | 10      |    30        |
| mean  |  8        |      0 |   5.5     |     53.4444  |        0.0192467 |  8.55     |  8.64    |  8.61    | 25.9333 |     2.41111  |
| std   |  0.830455 |      0 |   2.92138 |      4.96199 |        0.105418  |  0.831665 |  1.11176 |  1.02464 |  1.4555 |     1.83971  |
| min   |  7        |      0 |   1       |     45       |        0         |  7        |  6.5     |  7       | 24      |     0        |
| 25%   |  7        |      0 |   3       |     48.8125  |        0         |  8.5      |  8       |  8.125   | 26      |     0.750025 |
| 50%   |  8        |      0 |   5.5     |     55       |        0         |  8.5      |  9       |  8.75    | 26      |     2        |
| 75%   |  9        |      0 |   8       |     58.4583  |        0         |  9.25     |  9.6     |  9.525   | 26      |     4        |
| max   |  9        |      0 |  10       |     58.75    |        0.5774    |  9.5      |  9.8     |  9.7     | 29.3333 |     6        |

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

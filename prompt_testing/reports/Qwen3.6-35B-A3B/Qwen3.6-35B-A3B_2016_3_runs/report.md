# Relatório de Avaliação: Qwen3.6-35B-A3B - 3 execuções
**Gerado em: 21/05/2026 08:52:54**

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
      <td>40.975</td>
      <td>4.560</td>
      <td>5.9147</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>43.505</td>
      <td>5.063</td>
      <td>5.9860</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>37.975</td>
      <td>4.160</td>
      <td>5.2458</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |        1A |        1B |       1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|----------:|----------:|---------:|---------:|-------------:|
| count | 30        |     30 |  30       |     30       |               30 | 10        | 10        | 10       | 10       |     30       |
| mean  |  8        |      0 |   5.5     |     51.7957  |                0 |  8.3      |  7.75     |  8.05    | 24.6     |      3.4     |
| std   |  0.830455 |      0 |   2.92138 |      5.57889 |                0 |  0.421637 |  0.857969 |  0.68516 |  2.50333 |      2.31338 |
| min   |  7        |      0 |   1       |     38       |                0 |  7.5      |  6        |  6.5     | 18       |      0       |
| 25%   |  7        |      0 |   3       |     48.125   |                0 |  8.5      |  7.5      |  8       | 24       |      2       |
| 50%   |  8        |      0 |   5.5     |     52.44    |                0 |  8.5      |  7.5      |  8       | 26       |      3       |
| 75%   |  9        |      0 |   8       |     55       |                0 |  8.5      |  8        |  8       | 26       |      4       |
| max   |  9        |      0 |  10       |     58.75    |                0 |  8.5      |  9        |  9       | 26       |     12       |

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

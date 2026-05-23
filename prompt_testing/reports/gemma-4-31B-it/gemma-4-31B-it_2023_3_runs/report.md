# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 21/05/2026 08:51:17**

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
      <td>38.40</td>
      <td>9.14</td>
      <td>9.9490</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>25.60</td>
      <td>6.06</td>
      <td>6.7969</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>33.85</td>
      <td>8.06</td>
      <td>9.0409</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |   1A |       1B |       1C |     CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|-----:|---------:|---------:|---------:|-------------:|
| count | 15        |     15 |  15       |     15       |               15 |    5 | 5        |  5       |  5       |     15       |
| mean  |  8        |      0 |   3       |     51.3067  |                0 |    9 | 8.9      | 16.4     | 15.62    |      1.73333 |
| std   |  0.845154 |      0 |   1.46385 |      3.72126 |                0 |    0 | 0.547723 |  1.67332 |  1.83085 |      1.57963 |
| min   |  7        |      0 |   1       |     43.8     |                0 |    9 | 8        | 14       | 12.8     |      0       |
| 25%   |  7        |      0 |   2       |     49.4     |                0 |    9 | 9        | 16       | 15.4     |      0       |
| 50%   |  8        |      0 |   3       |     52       |                0 |    9 | 9        | 16       | 15.4     |      2       |
| 75%   |  9        |      0 |   4       |     54       |                0 |    9 | 9        | 18       | 17.1     |      3       |
| max   |  9        |      0 |   5       |     56.5     |                0 |    9 | 9.5      | 18       | 17.4     |      4       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |   5       |     5        |      5       |
| mean  |   3       |    59.06     |      0.8     |
| std   |   1.58114 |     0.563915 |      0.83666 |
| min   |   1       |    58.2      |      0       |
| 25%   |   2       |    59        |      0       |
| 50%   |   3       |    59        |      1       |
| 75%   |   4       |    59.4      |      1       |
| max   |   5       |    59.7      |      2       |

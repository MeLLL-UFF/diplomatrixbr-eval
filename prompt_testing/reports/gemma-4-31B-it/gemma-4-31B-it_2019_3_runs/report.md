# Relatório de Avaliação: gemma-4-31B-it - 3 execuções
**Gerado em: 14/05/2026 12:28:25**

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
      <td>19.5583</td>
      <td>3.1762</td>
      <td>3.6627</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>15.8250</td>
      <td>2.6000</td>
      <td>2.9747</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>17.8250</td>
      <td>2.8857</td>
      <td>2.9974</td>
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
|       |   prompt |   temp |   redacao |   nota_final |   nota_final_std |        1A |       1B |      1C |      CGPL |   num_errors |
|:------|---------:|-------:|----------:|-------------:|-----------------:|----------:|---------:|--------:|----------:|-------------:|
| count | 21       |     21 |  21       |     21       |       21         |  7        |  7       |  7      |  7        |    21        |
| mean  |  8       |      0 |   4       |     55.5921  |        0.0406619 |  9.19047  |  9.28571 | 18.5714 | 18.1571   |     0.571424 |
| std   |  0.83666 |      0 |   2.04939 |      2.10689 |        0.151431  |  0.377962 |  0.48795 |  0.9759 |  0.927105 |     0.907635 |
| min   |  7       |      0 |   1       |     52       |        0         |  9        |  9       | 18      | 17.1      |     0        |
| 25%   |  7       |      0 |   2       |     54       |        0         |  9        |  9       | 18      | 17.7      |     0        |
| 50%   |  8       |      0 |   4       |     55       |        0         |  9        |  9       | 18      | 17.7      |     0        |
| 75%   |  9       |      0 |   6       |     56       |        0         |  9.16665  |  9.5     | 19      | 18.65     |     1        |
| max   |  9       |      0 |   7       |     60       |        0.6807    | 10        | 10       | 20      | 19.6      |     3        |

### Humano
|       |   redacao |   nota_final |
|:------|----------:|-------------:|
| count |   7       |      7       |
| mean  |   4       |     57.4571  |
| std   |   2.16025 |      1.61385 |
| min   |   1       |     54       |
| 25%   |   2.5     |     57.5     |
| 50%   |   4       |     58.05    |
| 75%   |   5.5     |     58.2     |
| max   |   7       |     58.75    |

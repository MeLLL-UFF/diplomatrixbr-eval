# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 14/05/2026 18:27:36**

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
      <td>166.075</td>
      <td>26.0714</td>
      <td>29.2519</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>5.925</td>
      <td>1.1857</td>
      <td>1.5024</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>55.825</td>
      <td>8.8857</td>
      <td>9.7972</td>
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
|       |   prompt |   temp |   redacao |   nota_final |   nota_final_std |      1A |      1B |       1C |     CGPL |   num_errors |
|:------|---------:|-------:|----------:|-------------:|-----------------:|--------:|--------:|---------:|---------:|-------------:|
| count | 21       |     21 |  21       |      21      |               21 | 7       | 7       |  7       |  7       |     21       |
| mean  |  8       |      0 |   4       |      45.7524 |                0 | 5.85714 | 6.85714 | 12.1429  |  6.52857 |      8.90476 |
| std   |  0.83666 |      0 |   2.04939 |      13.7038 |                0 | 2.73426 | 3.07834 |  5.45981 |  3.71919 |      9.90406 |
| min   |  7       |      0 |   1       |       0      |                0 | 0       | 0       |  0       |  0       |      0       |
| 25%   |  7       |      0 |   2       |      38.5    |                0 | 6       | 7.5     | 13       |  5.25    |      2       |
| 50%   |  8       |      0 |   4       |      50      |                0 | 7       | 8       | 14       |  6.9     |      2       |
| 75%   |  9       |      0 |   6       |      57.3    |                0 | 7       | 8       | 15       |  8.45    |     15       |
| max   |  9       |      0 |   7       |      57.3    |                0 | 8       | 9       | 15       | 11.4     |     28       |

### Humano
|       |   redacao |   nota_final |   num_errors |
|:------|----------:|-------------:|-------------:|
| count |   7       |      7       |     7        |
| mean  |   4       |     57.4571  |     0.571429 |
| std   |   2.16025 |      1.61385 |     0.786796 |
| min   |   1       |     54       |     0        |
| 25%   |   2.5     |     57.5     |     0        |
| 50%   |   4       |     58.05    |     0        |
| 75%   |   5.5     |     58.2     |     1        |
| max   |   7       |     58.75    |     2        |

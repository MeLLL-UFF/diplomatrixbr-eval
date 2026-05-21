# Relatório de Avaliação: Qwen3.6-35B-A3B - 3 execuções
**Gerado em: 21/05/2026 08:52:42**

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
      <td>57.1250</td>
      <td>3.4583</td>
      <td>4.3688</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>137.1584</td>
      <td>8.0596</td>
      <td>9.2656</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>85.8750</td>
      <td>5.0139</td>
      <td>5.4086</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |        1A |       1B |        1C |      CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|----------:|---------:|----------:|----------:|-------------:|
| count | 54        |     54 |  54       |     54       |       54         | 18        | 18       | 18        | 18        |     54       |
| mean  |  8        |      0 |   9.5     |     50.6264  |        0.0685333 |  8.19444  |  7.72222 |  7.66667  | 25.5556   |      2.88889 |
| std   |  0.824163 |      0 |   5.23684 |      4.93672 |        0.490965  |  0.621641 |  1.14046 |  0.985184 |  0.855585 |      1.63299 |
| min   |  7        |      0 |   1       |     45       |        0         |  7        |  6       |  6        | 24        |      0       |
| 25%   |  7        |      0 |   5       |     45.125   |        0         |  7.5      |  6.5     |  7        | 26        |      1.49998 |
| 50%   |  8        |      0 |   9.5     |     50       |        0         |  8.5      |  8       |  8        | 26        |      3       |
| 75%   |  9        |      0 |  14       |     54.75    |        0         |  8.5      |  9       |  8.5      | 26        |      4       |
| max   |  9        |      0 |  18       |     58.75    |        3.6084    |  9.5      |  9       |  9.5      | 26        |      6       |

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

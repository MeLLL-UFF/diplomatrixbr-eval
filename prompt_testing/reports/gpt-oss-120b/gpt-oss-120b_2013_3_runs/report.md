# Relatório de Avaliação: gpt-oss-120b - 3 execuções
**Gerado em: 14/05/2026 12:29:04**

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
      <td>51.825</td>
      <td>20.8625</td>
      <td>27.7323</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.0</td>
      <td>26.325</td>
      <td>10.2625</td>
      <td>13.2140</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>12.925</td>
      <td>5.7125</td>
      <td>8.8356</td>
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
|       |    prompt |   temp |   redacao |   nota_final |   nota_final_std |   1A |      1B |    1C |   CGPL |   num_errors |
|:------|----------:|-------:|----------:|-------------:|-----------------:|-----:|--------:|------:|-------:|-------------:|
| count | 12        |     12 |  12       |      12      |               12 |    4 | 4       |  4    |   4    |     12       |
| mean  |  8        |      0 |   2.5     |      46.2833 |                0 |    6 | 5.75    | 11.25 |   8.55 |      5       |
| std   |  0.852803 |      0 |   1.16775 |      15.7794 |                0 |    4 | 3.94757 |  7.5  |   5.7  |      5.22233 |
| min   |  7        |      0 |   1       |       0      |                0 |    0 | 0       |  0    |   0    |      0       |
| 25%   |  7        |      0 |   1.75    |      42.9    |                0 |    6 | 5.25    | 11.25 |   8.55 |      2       |
| 50%   |  8        |      0 |   2.5     |      50      |                0 |    8 | 7       | 15    |  11.4  |      2       |
| 75%   |  9        |      0 |   3.25    |      57.3    |                0 |    8 | 7.5     | 15    |  11.4  |     12       |
| max   |  9        |      0 |   4       |      57.3    |                0 |    8 | 9       | 15    |  11.4  |     12       |

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

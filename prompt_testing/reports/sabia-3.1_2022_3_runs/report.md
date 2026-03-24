# Relatório de Avaliação: sabia-3.1_2022 - 3 execuções
**Gerado em: 24/03/2026 18:45:27**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo sabia em diferentes prompts/temperaturas versus a correção humana.

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
      <td>8</td>
      <td>0.0</td>
      <td>5.7917</td>
      <td>1.1389</td>
      <td>1.3620</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.5</td>
      <td>6.7217</td>
      <td>1.4211</td>
      <td>1.4892</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.0</td>
      <td>7.5000</td>
      <td>1.5000</td>
      <td>1.8019</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.5</td>
      <td>9.1667</td>
      <td>1.7778</td>
      <td>2.1573</td>
    </tr>
    <tr>
      <td>11</td>
      <td>0.0</td>
      <td>14.1667</td>
      <td>2.8194</td>
      <td>3.0355</td>
    </tr>
    <tr>
      <td>11</td>
      <td>0.5</td>
      <td>9.8333</td>
      <td>1.9167</td>
      <td>2.3989</td>
    </tr>
    <tr>
      <td>12</td>
      <td>0.0</td>
      <td>7.5000</td>
      <td>1.5000</td>
      <td>1.8019</td>
    </tr>
    <tr>
      <td>12</td>
      <td>0.5</td>
      <td>11.9001</td>
      <td>2.5111</td>
      <td>3.0317</td>
    </tr>
  </tbody>
</table>
    </td>
  </tr>
</table>

## 4. Análise de Erros Gramaticais
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Comparação de Número de Erros](comparacao_num_erros.png)

## 5. Correlação de Pearson
|           |       human |    p8, t0.0 |   p8, t0.5 |   p9, t0.0 |   p9, t0.5 |   p11, t0.0 |   p11, t0.5 |   p12, t0.0 |   p12, t0.5 |
|:----------|------------:|------------:|-----------:|-----------:|-----------:|------------:|------------:|------------:|------------:|
| human     |   1         |  -0.0623566 |  -0.457182 |        nan |  -0.118278 |   -0.433841 |  -0.0722752 |         nan |  -0.0197004 |
| p8, t0.0  |  -0.0623566 |   1         |   0.734989 |        nan |   0.948715 |    0.84746  |   0.986619  |         nan |  -0.158197  |
| p8, t0.5  |  -0.457182  |   0.734989  |   1        |        nan |   0.580343 |    0.82697  |   0.724385  |         nan |   0.40301   |
| p9, t0.0  | nan         | nan         | nan        |        nan | nan        |  nan        | nan         |         nan | nan         |
| p9, t0.5  |  -0.118278  |   0.948715  |   0.580343 |        nan |   1        |    0.766085 |   0.945636  |         nan |  -0.400004  |
| p11, t0.0 |  -0.433841  |   0.84746   |   0.82697  |        nan |   0.766085 |    1        |   0.874263  |         nan |  -0.11641   |
| p11, t0.5 |  -0.0722752 |   0.986619  |   0.724385 |        nan |   0.945636 |    0.874263 |   1         |         nan |  -0.212289  |
| p12, t0.0 | nan         | nan         | nan        |        nan | nan        |  nan        | nan         |         nan | nan         |
| p12, t0.5 |  -0.0197004 |  -0.158197  |   0.40301  |        nan |  -0.400004 |   -0.11641  |  -0.212289  |         nan |   1         |

## 6. Correlação de Spearman
|           |       human |    p8, t0.0 |   p8, t0.5 |   p9, t0.0 |   p9, t0.5 |   p11, t0.0 |   p11, t0.5 |   p12, t0.0 |   p12, t0.5 |
|:----------|------------:|------------:|-----------:|-----------:|-----------:|------------:|------------:|------------:|------------:|
| human     |   1         |   0.0308607 |  -0.314286 |        nan |  -0.130931 |   -0.617914 |  -0.0857143 |         nan |    0.092582 |
| p8, t0.0  |   0.0308607 |   1         |   0.92582  |        nan |   0.707107 |    0.715097 |   0.92582   |         nan |    0.183333 |
| p8, t0.5  |  -0.314286  |   0.92582   |   1        |        nan |   0.654654 |    0.882735 |   0.942857  |         nan |    0.216025 |
| p9, t0.0  | nan         | nan         | nan        |        nan | nan        |  nan        | nan         |         nan |  nan        |
| p9, t0.5  |  -0.130931  |   0.707107  |   0.654654 |        nan |   1        |    0.6742   |   0.654654  |         nan |   -0.424264 |
| p11, t0.0 |  -0.617914  |   0.715097  |   0.882735 |        nan |   0.6742   |    1        |   0.794461  |         nan |   -0.143019 |
| p11, t0.5 |  -0.0857143 |   0.92582   |   0.942857 |        nan |   0.654654 |    0.794461 |   1         |         nan |    0.123443 |
| p12, t0.0 | nan         | nan         | nan        |        nan | nan        |  nan        | nan         |         nan |  nan        |
| p12, t0.5 |   0.092582  |   0.183333  |   0.216025 |        nan |  -0.424264 |   -0.143019 |   0.123443  |         nan |    1        |

## Estatísticas Descritivas
### Modelo sabia-3.1_2022
|       |   prompt |      temp |   redacao |   nota_final |   nota_final_std |   1A |   1B |   1C |   CGPL |   num_errors |
|:------|---------:|----------:|----------:|-------------:|-----------------:|-----:|-----:|-----:|-------:|-------------:|
| count | 48       | 48        |   48      |      48      |        48        |    0 |    0 |    0 |      0 |    48        |
| mean  | 10       |  0.25     |    3.5    |      55.2651 |         0.743915 |  nan |  nan |  nan |    nan |     0.430552 |
| std   |  1.59787 |  0.252646 |    1.7259 |       1.4009 |         1.34477  |  nan |  nan |  nan |    nan |     0.813474 |
| min   |  8       |  0        |    1      |      51.6667 |         0        |  nan |  nan |  nan |    nan |     0        |
| 25%   |  8.75    |  0        |    2      |      55      |         0        |  nan |  nan |  nan |    nan |     0        |
| 50%   | 10       |  0.25     |    3.5    |      55      |         0        |  nan |  nan |  nan |    nan |     0        |
| 75%   | 11.25    |  0.5      |    5      |      55.75   |         1.3919   |  nan |  nan |  nan |    nan |     0.3333   |
| max   | 12       |  0.5      |    6      |      58.5    |         5.4848   |  nan |  nan |  nan |    nan |     3        |

### Humano
|       |   redacao |   nota_final |        1A |        1B |        1C |      CGPL |   num_errors |
|:------|----------:|-------------:|----------:|----------:|----------:|----------:|-------------:|
| count |   6       |      6       |  6        |  6        |  6        |  6        |     6        |
| mean  |   3.5     |     56.4     |  9.75     |  9.75     | 18.5      | 18.4      |     0.333333 |
| std   |   1.87083 |      1.24258 |  0.273861 |  0.273861 |  0.447214 |  0.532917 |     0.516398 |
| min   |   1       |     54.7     |  9.5      |  9.5      | 18        | 17.7      |     0        |
| 25%   |   2.25    |     55.625   |  9.5      |  9.5      | 18.125    | 18.05     |     0        |
| 50%   |   3.5     |     56.35    |  9.75     |  9.75     | 18.5      | 18.35     |     0        |
| 75%   |   4.75    |     57.3     | 10        | 10        | 18.875    | 18.875    |     0.75     |
| max   |   6       |     58       | 10        | 10        | 19        | 19        |     1        |

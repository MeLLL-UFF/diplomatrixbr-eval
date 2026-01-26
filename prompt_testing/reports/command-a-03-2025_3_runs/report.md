# Relatório de Avaliação: command-a-03-2025 - 3 execuções
**Gerado em: 26/01/2026 16:04:54**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo command-a em diferentes prompts/temperaturas versus a correção humana.

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
    <tr style="text-align: right;">
      <th></th>
      <th>prompt</th>
      <th>temp</th>
      <th>area_sob_curva</th>
      <th>mae</th>
      <th>rmse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>0.0</td>
      <td>13.2000</td>
      <td>2.6167</td>
      <td>2.7077</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>0.5</td>
      <td>12.5333</td>
      <td>2.5056</td>
      <td>2.6173</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>0.9</td>
      <td>12.8668</td>
      <td>2.5334</td>
      <td>2.7365</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>0.0</td>
      <td>7.1000</td>
      <td>1.4333</td>
      <td>1.8921</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>0.5</td>
      <td>7.1000</td>
      <td>1.4333</td>
      <td>1.8921</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8</td>
      <td>0.9</td>
      <td>7.1000</td>
      <td>1.4333</td>
      <td>1.8921</td>
    </tr>
    <tr>
      <th>6</th>
      <td>9</td>
      <td>0.0</td>
      <td>26.0667</td>
      <td>5.0111</td>
      <td>6.0313</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9</td>
      <td>0.5</td>
      <td>27.7333</td>
      <td>5.2889</td>
      <td>6.2795</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>0.9</td>
      <td>23.5666</td>
      <td>4.4555</td>
      <td>5.3529</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>0.0</td>
      <td>15.8667</td>
      <td>3.0056</td>
      <td>3.9132</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>0.5</td>
      <td>14.0333</td>
      <td>2.6722</td>
      <td>3.3080</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10</td>
      <td>0.9</td>
      <td>14.0334</td>
      <td>2.7278</td>
      <td>3.3414</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11</td>
      <td>0.0</td>
      <td>11.5000</td>
      <td>2.1667</td>
      <td>2.6920</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11</td>
      <td>0.5</td>
      <td>9.5000</td>
      <td>1.8333</td>
      <td>2.1863</td>
    </tr>
    <tr>
      <th>14</th>
      <td>11</td>
      <td>0.9</td>
      <td>10.1667</td>
      <td>1.9444</td>
      <td>2.3354</td>
    </tr>
    <tr>
      <th>15</th>
      <td>12</td>
      <td>0.0</td>
      <td>17.5000</td>
      <td>3.1667</td>
      <td>5.0577</td>
    </tr>
    <tr>
      <th>16</th>
      <td>12</td>
      <td>0.5</td>
      <td>17.5000</td>
      <td>3.1667</td>
      <td>5.0577</td>
    </tr>
    <tr>
      <th>17</th>
      <td>12</td>
      <td>0.9</td>
      <td>17.5000</td>
      <td>3.1667</td>
      <td>5.0577</td>
    </tr>
  </tbody>
</table>
    </td>
  </tr>
</table>

## 4. Análise de Erros Gramaticais
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Comparação de Número de Erros](comparacao_num_erros.png)

## 4. Estatísticas Descritivas
### Modelo command-a v03-2025
|       |    prompt |       temp |   redacao |   nota_final |        1A |       1B |        1C |      CGPL |   num_errors |
|:------|----------:|-----------:|----------:|-------------:|----------:|---------:|----------:|----------:|-------------:|
| count | 108       | 108        | 108       |    108       | 36        | 36       | 36        | 36        |   108        |
| mean  |   9.5     |   0.466667 |   3.5     |     54.5466  |  9.25926  |  8.75463 | 17.8796   | 17.8296   |     0.138889 |
| std   |   1.71579 |   0.369895 |   1.71579 |      3.23169 |  0.288516 |  0.29943 |  0.469058 |  0.469566 |     0.347443 |
| min   |   7       |   0        |   1       |     45       |  8.5      |  8       | 16        | 16        |     0        |
| 25%   |   8       |   0        |   2       |     53.5     |  9        |  8.5     | 18        | 17.7      |     0        |
| 50%   |   9.5     |   0.5      |   3.5     |     55       |  9.41665  |  9       | 18        | 18        |     0        |
| 75%   |  11       |   0.9      |   5       |     58       |  9.5      |  9       | 18        | 18        |     0        |
| max   |  12       |   0.9      |   6       |     58       |  9.5      |  9       | 18.3333   | 18.3333   |     1        |

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

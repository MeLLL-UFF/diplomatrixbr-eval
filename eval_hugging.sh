NITERACOES="3"
TEMPS="0.0"
PROMPTS="7 8 9"
ESSAY=""
NOME_MODELO="Qwen/Qwen3.6-35B-A3B"

python3 -m scripts.juiz_hugging --n_iteracoes $NITERACOES --temps $TEMPS --anos 2019 --prompts $PROMPTS --nome_modelo $NOME_MODELO
python3 -m scripts.juiz_hugging --n_iteracoes $NITERACOES --temps $TEMPS --anos 2020-2021 --prompts $PROMPTS --nome_modelo $NOME_MODELO
python3 -m scripts.juiz_hugging --n_iteracoes $NITERACOES --temps $TEMPS --anos 2022 --prompts $PROMPTS --nome_modelo $NOME_MODELO
python3 -m scripts.juiz_hugging --n_iteracoes $NITERACOES --temps $TEMPS --anos 2023 --prompts $PROMPTS --nome_modelo $NOME_MODELO
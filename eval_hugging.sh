NITERACOES="1"
TEMPS="0.3"
PROMPTS="8"
ESSAY="1"
NOME_MODELO="google/gemma-3-1b-it"

python -m scripts.juiz_hugging --n_iteracoes $NITERACOES --temps $TEMPS --anos 2022 --prompts $PROMPTS --nome_modelo $NOME_MODELO --redacoes $ESSAY
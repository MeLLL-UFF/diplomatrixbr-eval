NITERACOES="3"
TEMPS="0.0 0.2 0.5"
PROMPTS="7 8 9"
ESSAY=""

python -m scripts.juiz_sabia --n_iteracoes $NITERACOES --temps $TEMPS --anos 2018 --prompts $PROMPTS

python -m scripts.juiz_sabia --n_iteracoes $NITERACOES --temps $TEMPS --anos 2022 --prompts $PROMPTS
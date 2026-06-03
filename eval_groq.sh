NITERACOES="3"
TEMPS="0.0 0.5"
PROMPTS="7 8 9 10 11 12"

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2014 --prompts $PROMPTS --modelo llama-3.3-70b-versatile

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2018 --prompts $PROMPTS --modelo llama-3.3-70b-versatile

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2020-2021 --prompts $PROMPTS --modelo llama-3.3-70b-versatile

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2014 --prompts $PROMPTS --modelo openai/gpt-oss-120b

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2018 --prompts $PROMPTS --modelo openai/gpt-oss-120b

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2020-2021 --prompts $PROMPTS --modelo openai/gpt-oss-120b

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2014 --prompts $PROMPTS --modelo qwen/qwen3-32b

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2018 --prompts $PROMPTS --modelo qwen/qwen3-32b

python -m scripts.juiz_groq --n_iteracoes $NITERACOES --temps $TEMPS --anos 2020-2021 --prompts $PROMPTS --modelo qwen/qwen3-32b
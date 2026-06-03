NITERACOES="3"
TEMPS="0.0"
PROMPTS="7 8 9"

years="2024"

essays="1"

for year in $years
do
    echo Ano $year
    python -m scripts.juiz_google_cloud --n_iteracoes $NITERACOES --temps $TEMPS --anos $year --prompts $PROMPTS --redacoes $essays
done
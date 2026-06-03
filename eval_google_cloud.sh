NITERACOES="3"
TEMPS="0.0"
PROMPTS="8"
ESSAY=""

years="2015"

essays="7"

for year in $years
do
    echo Ano $year
    python -m scripts.juiz_google_cloud --n_iteracoes $NITERACOES --temps $TEMPS --anos $year --prompts $PROMPTS --redacoes $essays
done
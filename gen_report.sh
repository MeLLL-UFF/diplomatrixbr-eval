YEAR="2018"
EVALPATH="prompt_testing\sheets\sabia-4_${YEAR}_p7-9_3r.csv"
HUMANPATH="prompt_testing\sheets\notas_humanas_${YEAR}.csv"

python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model sabia --model_version 4 --year $YEAR &

YEAR="2022"
EVALPATH="prompt_testing\sheets\sabia-4_${YEAR}_p7-9_3r.csv"
HUMANPATH="prompt_testing\sheets\notas_humanas_${YEAR}.csv"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model sabia --model_version 4 --year $YEAR &

wait
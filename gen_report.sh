YEAR="2018"
MODEL="sabia-3.1"
EVALPATH="prompt_testing\sheets\\${MODEL}\\${MODEL}_${YEAR}_p7-15_3r.csv"
HUMANPATH="prompt_testing\sheets\notas_humanas\notas_humanas_${YEAR}.csv"

python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR &

YEAR="2022"
EVALPATH="prompt_testing\sheets\\${MODEL}\\${MODEL}_${YEAR}_p7-15_3r.csv"
HUMANPATH="prompt_testing\sheets\notas_humanas\notas_humanas_${YEAR}.csv"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR &

wait
YEAR="2013"
MODEL="gemma-4-31B-it"
EVALPATH="prompt_testing/sheets/${MODEL}/${MODEL}_${YEAR}_p7-9_3r.csv"
HUMANPATH="prompt_testing/sheets/notas_humanas/notas_humanas_${YEAR}.csv"

python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2014"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2015"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2016"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2017"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2019"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2020-2021"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR

YEAR="2023"
python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model $MODEL --year $YEAR
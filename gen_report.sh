EVALPATH="MODEL_SCORES_PATH"
HUMANPATH="HUMAN_SCORES_PATH"

python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model sabia --model_version 3.1_2022
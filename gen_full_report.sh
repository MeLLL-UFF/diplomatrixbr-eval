# Pra rodar:
# chmod +x gen_full_report.sh
# ./gen_full_report.sh

full_report(){
    local num_runs="$1"
    local model="$2"

    python -m scripts.full_report --num_runs $num_runs --num_redacoes 88 --model $model
}

models=(
	#Models to gen report for
)

NUM_RUNS="3"

for model in "${models[@]}"; do
    full_report "$NUM_RUNS" "$model"
done
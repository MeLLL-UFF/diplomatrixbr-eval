# Pra rodar:
# chmod +x gen_full_report.sh
# ./gen_full_report.sh

full_report(){
    local num_runs="$1"
    local model="$2"

    python -m scripts.full_report --num_runs $num_runs --num_redacoes 93 --model $model
}

models=(
	"claude-opus-4-6"
    "gemma-4-31B-it"
    "gpt-oss-120b"
    "Qwen3.6-35B-A3B"
    "sabia-4"
)

NUM_RUNS="3"

for model in "${models[@]}"; do
    full_report "$NUM_RUNS" "$model"
done
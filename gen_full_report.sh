full_report(){
    local num_runs="$1"
    local model="$2"

    python -m scripts.full_report --num_runs $num_runs --model $model
}

models=(
	"gemma-4-31B-it"
	"Qwen3.6-35B-A3B"
	"gpt-oss-120b"
)

NUM_RUNS="3"

for model in "${models[@]}"; do
    full_report "$NUM_RUNS" "$model"
done
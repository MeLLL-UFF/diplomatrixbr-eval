set -euo pipefail

models=(
	"sabia-3.1"
)

years=(
	"2018"
	"2022"
)

run_report() {
	local model="$1"
	local year="$2"
	local eval_path="prompt_testing/sheets/${model}/${model}_${year}_p7-15_3r.csv"
	local human_path="prompt_testing/sheets/notas_humanas/notas_humanas_${year}.csv"

	python -m scripts.analysis_report \
		--num_runs 3 \
		--eval_path "$eval_path" \
		--human_path "$human_path" \
		--model "$model" \
		--year "$year"
}

for model in "${models[@]}"; do
	for year in "${years[@]}"; do
		run_report "$model" "$year"
	done
done
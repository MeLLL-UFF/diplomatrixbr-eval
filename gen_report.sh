set -euo pipefail

models=(
	"gemma-4-31B-it"
	"Qwen3.6-35B-A3B"
	"gpt-oss-120b"
)

years=(
	"2013"
	"2014"
	"2015"
	"2016"
	"2017"
	"2018"
	"2019"
	"2020-2021"
	"2022"
	"2023"
)

run_report() {
	local model="$1"
	local year="$2"
	local eval_path="prompt_testing/sheets/${model}/${model}_${year}_p7-9_3r.csv"
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
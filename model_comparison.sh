MODEL_LIST="claude-opus-4-6 gemma-4-31B-it gpt-oss-120b Qwen3.6-35B-A3B sabia-4"

python -m scripts.inter_model_comparison --models $MODEL_LIST --num_runs 3
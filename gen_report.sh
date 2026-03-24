EVALPATH="D:\Users\Rodrigo\Documents\Estudos\Faculdade\VsCode\IniciacaoCientifica\diplomatrixbr-eval\prompt_testing\sheets\sabia_2018_p7-12_3r.csv"
HUMANPATH="D:\Users\Rodrigo\Documents\Estudos\Faculdade\VsCode\IniciacaoCientifica\diplomatrixbr-eval\prompt_testing\sheets\notas_humanas_2018.csv"

python -m scripts.analysis_report --num_runs 3 --eval_path $EVALPATH --human_path $HUMANPATH --model sabia --model_version 3.1_2018
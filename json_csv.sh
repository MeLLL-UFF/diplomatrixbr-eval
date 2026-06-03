MODEL="claude-opus-4-6"

years="2013 2014 2015 2016 2017 2018 2019 2020-2021 2022 2023 2024"

for year in $years
do
    python scripts/json_to_csv.py --model $MODEL --year $year
done
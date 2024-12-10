day=$1
touch "inputs/${day}.txt"
touch "src/day${day}.py"
cp src/test_template.py "src/test_day${day}.py"

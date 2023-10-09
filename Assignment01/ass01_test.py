from ass01_main import ass01_main
from pathlib import Path

def test_ass01_main():
    with open("Assignment01/airlinehub.ans") as answersFile:
        correct_answers = [line.rstrip() for line in answersFile]
        
    my_answers = ass01_main()

    assert my_answers == correct_answers
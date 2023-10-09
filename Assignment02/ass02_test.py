from ass02_main import ass02_main

def test_ass02_main():
    correct_answer = load_correct_answer()
    my_answer = ass02_main()

    assert my_answer == correct_answer

def load_correct_answer(correct_answer_file="Assignment02/stringmultimatching.ans"):
    with open(correct_answer_file) as answersFile:
        correct_answer = answersFile.read()

    return correct_answer

if __name__ == "__main__":
    test_ass02_main()
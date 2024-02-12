import lab4q2
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('6\n10\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab4q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'6 times 10 =  60') != -1
    assert captured_stdout.strip().find(f'6 times 11') == -1

def test_case2(monkeypatch, capsys):
  with open(f"lab4q2.py") as tf:
    head = [next(tf) for _ in range(23)]
    s = tf.read()
    assert(s.find("while") != -1 )


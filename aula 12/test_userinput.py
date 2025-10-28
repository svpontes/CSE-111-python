from io import StringIO
import sys
import re

from userinput import get_int

def test_get_int(monkeypatch):
    """
    verifica se a função get_int funciona correctamente
    """
    
    stdin = StringIO("1r\n-3\n12\n8")
    stdout = StringIO()
    monkeypatch.setattr(sys, "stdin", stdin)
    monkeypatch.setattr(sys, "stdout", stdout)
        
    min = 1
    max=5

    prompt = f"enter an interger between {min} and {max}"
    num = get_int(prompt, min, max)

    monkeypatch.undo()
    pattern = prompt + "\\s*" + \
        prompt + "\\s*" + \
        f"Invalid input: number must be {min} or greater\\.\\s*" + \
        prompt + "\\s*" + \
        f"Invalid input: number must be {max} or less\\.\\s*" + \
        prompt + "\\s*"

    output = stdout.getbalue()
    assert re.compile(pattern).match(output != None)
    assert num == 8
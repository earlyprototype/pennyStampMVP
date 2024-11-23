#import sys
#print(sys.path)

from ..sandbox import execute_sandboxed_code
import pandas as pd

def test_sandbox_execution():
    code = """
    _print_(df['Close'].mean())
    """
    data = {'Close': [150.0, 155.0, 160.0]}
    df = pd.DataFrame(data)
    output, error = execute_sandboxed_code(code, df)
    assert error is None
    assert float(output.strip()) == 155.0
    print("Sandbox test passed!")


if __name__ == "__main__":
    test_sandbox_execution()
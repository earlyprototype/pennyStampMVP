from restrictedpython import safe_builtins, compile_restricted
from io import StringIO

restricted_globals = {
    '__builtins__': safe_builtins,
    '_print_': lambda x: output_buffer.write(str(x) + '\n'),  # Capture print output
    '_getattr_': getattr,  # Allow attribute access
    # Add any other safe built-ins or modules here (e.g., math)
}

def execute_sandboxed_code(code, data):
    """Executes Python code in a restricted environment.

    Args:
        code: The Python code to execute (string).

    Returns:
        A tuple containing (output, error).
    """

    output_buffer = StringIO()
    byte_code = compile_restricted(code, '<string>', 'exec')
    try:
        exec(byte_code, restricted_globals, {'df': data}) # df will be the pandas DataFrame
        output = output_buffer.getvalue()
        error = None
    except Exception as e:
        output = None
        error = str(e)
    return output, error
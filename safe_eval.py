"""
Overriding eval function defined in the base module
in order to complete globals_dict with missing Python __builtins__
"""

from hr_payroll import hr_payroll

native_safe_eval = hr_payroll.eval


def new_safe_eval(expr, globals_dict=None, locals_dict=None, mode="eval", nocopy=False):
    globals_dict = globals_dict or {}
    globals_dict.update({
        'divmod': divmod,
        'enumerate': enumerate,
        'float': float,
        'int': int,
        'isinstance': isinstance,
        'pow': pow,
        'range': range,
        'reversed': reversed,
        'sorted': sorted,
        'sum': sum,
        'type': type,
        'xrange': xrange,
        'zip': zip,
    })
    return native_safe_eval(expr, globals_dict, locals_dict, mode, nocopy)

hr_payroll.eval = new_safe_eval

import traceback

def log_traceback(ex):
    tb_lines = traceback.format_exception(ex.__class__, ex, ex.__traceback__)
    tb_text = ''.join(tb_lines)
    # I'll let you implement the ExceptionLogger class,
    # and the timestamping.
    exception_logger.log(tb_text)

try:
    x = get_number()
except Exception as ex:
    log_traceback(ex)
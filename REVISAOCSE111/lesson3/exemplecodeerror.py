def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print(f"Oh no error: {error_message} ")

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code=45,error_severity=1,log_to_db=True,error_message="second number greater than first", source_module="my_math_method")
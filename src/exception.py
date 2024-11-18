import sys
from src.logger import logging

# Function to extract detailed error messages
def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message with script name, line number, and error description.

    Parameters:
    - error: The exception object.
    - error_detail: sys module used to extract exception details (like traceback).

    Returns:
    - error_message: A formatted string containing the file name, line number, and error details.
    """
    # Extract traceback details from the sys module
    _, _, exc_tb = error_detail.exc_info()
    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Format a detailed error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


# Custom exception class to provide additional context for errors
class CustomException(Exception):
    """
    A custom exception class to enhance standard Python exceptions with detailed error information.

    Parameters:
    - error_message: The initial error message from the exception.
    - error_detail: sys module to extract detailed traceback information.

    Methods:
    - __str__: Returns the detailed error message as a string.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException class by calling the error_message_detail function.

        Parameters:
        - error_message: The raw error message.
        - error_detail: sys module for traceback extraction.
        """
        # Initialize the base Exception class with the raw error message
        super().__init__(error_message)
        # Generate the detailed error message using the helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        """
        Overrides the __str__ method to return the detailed error message when the exception is printed.

        Returns:
        - str: The detailed error message.
        """
        return self.error_message

# if __name__=="__main__":

#     try:
#         a=1/0
#     except:
#         logging.info("logging has started")
#         raise CustomException
        
    
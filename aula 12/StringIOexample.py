from io import StringIO
import sys

def get_int(prompt, min, max):

    num = None

    while num is None:
        try:
            text = input(prompt)
            

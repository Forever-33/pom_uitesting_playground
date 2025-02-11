import os
from dotenv import load_dotenv

load_dotenv()


class Data:

    PRIMER_TEST = os.getenv("PRIMER_TEST")

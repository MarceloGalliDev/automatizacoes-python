from pyzbar.pyzbar import decode
from pdf2image import convert_from_path
import os
import numpy as np


pdfs = [os.listdir()]
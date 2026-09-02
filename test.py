"""Test at dit AI-miljø er sat korrekt op.
Kør med: python test.py (husk 'conda activate aau-ai' først)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("scikit-learn:", sklearn.__version__)
print("Alt virker!")

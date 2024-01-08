import string as st
import numpy as np
from tkinter import *

letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
algarismo = letras+numeros+especial
senha = np.random.choice(list(algarismo),10) 
print(''.join(senha))



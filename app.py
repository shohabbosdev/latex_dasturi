# import streamlit 
# streamlit.title('Latexda ishlaydigan dastur')
# 1-kodimiz har safar streamlit so'zini yozishni talab qiladi

from streamlit import *
from math import *
import matplotlib.pyplot as plt

markdown('# :rainbow[Kvadrat tenglamaning ildizlarini hisoblash dasturi]')
latex(r'''
    a\cdot x^2+b\cdot x+c=0
    ''')
write("Tenglamaning a,b,c koeffitsiyentlarini kiriting")
# a = text_input("A ni kiriting")
ustun1,ustun2,ustun3 = columns(3)

with ustun1:
    a = sidebar.slider("A ni kiriting",-10,10)
with ustun2:
    b = sidebar.slider("B ni kiriting",-10,10)
with ustun3:
    c = sidebar.slider("C ni kiriting",-10,10)

D = b*b-4*a*c
if D>0:
    x1 = write(f"Birinchi yechim {(-b+sqrt(D))/2*a}")
    x2 = write(f"Ikkinchi yechim {(-b-sqrt(D))/2*a}")
    header(f"{a}x^2+{b}x + {c} = 0")
    x = [i for i in range(2001)]
    y = [a*i+b*i+c for i in range(2001)]
    import numpy as np

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    pyplot(fig)
    
elif D==0:
    x = write(f"Yagona yechim {-b/2*a}")
    header(f"{a}x^2+{b}x + {c} = 0")
else:
    write("Yechim yo'q")
    header(f"{a}x^2+{b}x + {c} = 0")

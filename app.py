# import streamlit 
# streamlit.title('Latexda ishlaydigan dastur')
# 1-kodimiz har safar streamlit so'zini yozishni talab qiladi

from streamlit import *
from math import *

markdown('# :rainbow[Kvadrat tenglamaning ildizlarini hisoblash dasturi]')
with expander("Kvadrat tenglama dasturi"):
    latex(r'''
        a\cdot x^2+b\cdot x+c=0
        ''')
    write("Tenglamaning a,b,c koeffitsiyentlarini kiriting")
    # a = text_input("A ni kiriting")
    ustun1,ustun2,ustun3 = columns(3)

    with ustun1:
        a = sidebar.number_input("A ni kiriting",-10,10)
    with ustun2:
        b = sidebar.number_input("B ni kiriting",-10,10)
    with ustun3:
        c = sidebar.number_input("C ni kiriting",-10,10)

    D = b*b-4*a*c
    if D>0:
        x1 = write(f"Birinchi yechim {(-b+sqrt(D))/2*a}")
        x2 = write(f"Ikkinchi yechim {(-b-sqrt(D))/2*a}")
    elif D==0:
        x = write(f"Yagona yechim {-b/2*a}")
    else:
        write("Yechim yo'q")
import streamlit as st
#Definir el título
st.title('Mi primer app')

st.write("Esta aplicación tiene el objetivo de elevar cualquier número al cuadrado:")

x = st.number_input('Introduzca un número: ')
st.write('El número al cuadrado es:', x**2)

st.write('muchas gracias, hasta luego :D')
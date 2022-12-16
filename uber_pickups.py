import streamlit as st
import pandas as pd
import numpy as np
import time 
st.title('Recogidas en uber en la gran ciudad de new yorkkkkkkk :)')



DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Cargando la info, espera...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Data cargada... excelente!')

st.subheader('Datos sin procesar')
st.write(data)

st.subheader('Cantadidad de recogidas por hora')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.write(' se puede ver que en el horario que más las personas piden uber es a ls 17 con casi 800 recogidas :o')


hour_to_filter = st.slider('puedes ver un horario de las 0 a 23 horas', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Mapa de todas las recogidas a las: {hour_to_filter}:00')
st.map(filtered_data)

if st.checkbox('Mostrar datos sin procesar  '):
    st.subheader('Datos sin procesar')
    st.write(data)

st.write('Nicolas Gutierrez')




st.write("Aquí está nuestro primer intento de usar datos para crear una tabla:")

df = pd.DataFrame({
  'animes buenos': ['Dragon ball z', 'Bokuno hero', 'no me se más xd'],
  'calificación': [10, 9, 0]
})

st.dataframe(df)

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


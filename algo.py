import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.title('The ultimate visualization experience')

DATE_COLUMN = 'Series1'
DATA_URL = ('./dat.csv')

@st.cache
def load_data(nrows):
    data = df = pd.read_csv(DATA_URL,nrows=nrows) 
    return data

data_load_state = st.text('Loading data...')
data = load_data(100)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Some barcharts')
hist_values = np.histogram(data[DATE_COLUMN], bins=10)[0]
st.bar_chart(hist_values)

st.subheader('Some linecharts')
st.line_chart(data, columns=['Series1'])
st.area_chart(data, columns=['Series1'])

df = pd.DataFrame(data,columns=['Series1', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)

#Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
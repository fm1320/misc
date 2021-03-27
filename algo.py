import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

st.title('The ultimate visualization experience')

DATE_COLUMN = 'Series1'
DATA_URL = ('./dat.csv')

@st.cache
def load_data(nrows):

 st.write(f"""### Loaded **{rows}** rows""")

    data = df = pd.read_csv(DATA_URL,nrows=nrows) 
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

bins_slide = st.sidebar.slider("Graph width ", 5, 10, 20)


st.subheader('Some barcharts')
hist_values = np.histogram(data[DATE_COLUMN], bins=bins_slide)[0]
st.bar_chart(hist_values)

st.subheader('Some linecharts')
st.line_chart(data)
st.area_chart(data)

# pr = ProfileReport(data, explorative=True)
# st.header('**Pandas Profiling Report**')
# st_profile_report(pr)

st.write("Other possibilites with data")
df1 = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
c = alt.Chart(df1).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)

#Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
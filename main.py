import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt


selectbox = st.sidebar.selectbox(
    "Choose one",
    ("Data Visualization", "Machine Learning", "Interpretability")
)
st.title('Food Demand Forecasting')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv('train.csv', nrows=nrows)
    return data

@st.cache_data
def load_center_data(nrows):
    data = pd.read_csv('fulfilment_center_info.csv', nrows=nrows)
    return data

@st.cache_data
def load_meal_data(nrows):
    data = pd.read_csv('meal_info.csv', nrows=nrows)
    return data

st.set_option('deprecation.showPyplotGlobalUse', False)

weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)

tab1,tab2,tab3,tab4 = st.tabs(['Data','Charts','Custom','Contact Form'])

with tab1:
    st.subheader("Weekly Data - 1000 rows")
    st.dataframe(weekly_data)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Center info data")
        st.dataframe(center_info_data)
    with col2:
        st.subheader("Meal Data")
        st.dataframe(meal_data)


with tab2:
    # WeeklyDemand Data
    st.header('Weekly Demand Data')
    # st.write(weekly_data)
    st.divider()

    st.subheader("Bar Chart of number of orders")
    st.bar_chart(weekly_data['num_orders'])

    st.subheader("Histogram for order, checkout price and base price")
    df = pd.DataFrame(weekly_data[:200], columns=['num_orders', 'checkout_price', 'base_price'])
    df.hist()
    st.pyplot()

    st.subheader("Line Chart")
    st.line_chart(df)
    chart_data = pd.DataFrame(weekly_data[:40], columns=['num_orders', 'base_price'])

    st.subheader("Area chart")
    st.area_chart(chart_data)

    # Center Information
    st.subheader('Center Information')
    if st.checkbox('Show Center Information data'):
        st.subheader('Center Information data')
        st.write(center_info_data)

    st.bar_chart(center_info_data['region_code'])
    st.bar_chart(center_info_data['center_type'])

    st.subheader('Meal Information')
    st.write(meal_data)
    st.bar_chart(meal_data['cuisine'])
    agree = st.button('Click to see Categories of Meal')
    if agree:
        st.bar_chart(meal_data['category'])

with tab3:
    import streamlit.components.v1 as components

    components.html(
        """
    
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <title>Bootstrap Example</title>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
          <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
          <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
        </head>
        <body>
         
        <div class="container">
          <h2>Profile</h2>
          <div class="card" style="width:400px">
            <div class="card-body">
              <h4 class="card-title">Aniket Wattamwar</h4>
              <p class="card-text">Senior Software Developer</p>
              <a href="#" class="btn btn-primary">See Profile</a>
            </div>
            <img class="card-img-bottom" src="https://louisville.edu/enrollmentmanagement/images/person-icon/image" alt="Card image" style="width:100%">
          </div>
        </div>
        
        </body>
        </html>


        """,
        height=600,
    )


with tab4:
    st.subheader("Enter Information")
    name = st.text_input("Enter your name")
    msg = st.text_area("Enter message/feedback")
    date = st.date_input("Enter Today's Date")
    st.text("Upload any documents(Optional)")
    uploaded_file = st.file_uploader("Choose a file")
    if st.button('Submit'):
        arr = []
        arr.append([name,msg,date])
        st.write("Data submitted successfully")


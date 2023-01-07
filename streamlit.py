# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 21:19:57 2023

@author: Mleko
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.set_page_config(
    page_title = 'PAD_6 Streamlit',
    layout = 'wide'
)

page = st.sidebar.select_slider('Page',['Form', 'Stats'])


if page == 'Form':

    st.title('Survey')
    with st.form('name_and_surname_form'):

        name_text = st.text_input('Name', placeholder='Your name')
        surname_text = st.text_input('Surname', placeholder='Your surname')
        submitted = st.form_submit_button('Submit')

        if submitted:
            if name_text != "" and surname_text != "":
                st.success(f'Form submitted successfully')
            else:
                st.error('Missing required information')


elif page == 'Stats':

    st.title('CSV Dataset')
    data = st.file_uploader('Dataset', type=['csv'])
    if data is not None:
        with st.spinner("Please wait..."):
            df = pd.read_csv(data, sep=',')
            st.dataframe(df.sample(10))
        st.success(f'File uploaded successfully')
    st.text('')

    if data is not None:
        st.header('Data visualization')

        graph_type = st.radio('Graph type', ['Scatter 3D', 'Bar'])       
        
        col1, col2 = st.columns(2)

        if graph_type == 'Scatter 3D':
            x_column = st.selectbox('X', df.columns[1:])
            y_column = st.selectbox('Y', df.columns[1:])
            z_column = st.selectbox('Z', df.columns[1:])
            fig = px.scatter_3d(df, x=x_column, y=y_column, z=z_column, title=f'{graph_type}, {x_column} of {y_column}')

        elif graph_type == 'Bar':
            x_column = st.selectbox('X', df.columns[1:])
            y_column = st.selectbox('Y', df.columns[1:])
            fig = px.bar(df, x=x_column, y=y_column, title=f'{graph_type}, {x_column} of {y_column}')

        else:
            st.text('Graph Type not supported')

        col1.plotly_chart(fig, use_container_width = True)


else:
    st.text('Selection not supported')
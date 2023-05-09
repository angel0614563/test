import streamlit as st
import numpy as np
import pandas as pd

st.header("折线图演示")

data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)
st.write(data)
st.line_chart(data)

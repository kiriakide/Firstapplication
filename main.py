import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("HealthCoach :heart: :running:")
    st.subheader("hey")

st.sidebar.success("select a page above")



import boto3


def lambda_handler(event, context):

    client = boto3.client("elasticbeanstalk")

    response = client.describe_environment_health(
        EnvironmentName="Myebapp-env", AttributeNames=["HealthStatus"]
    )

    output = (
        """<font size="56 px" color="#444444">"""
        + response["HealthStatus"]
        + """</font>"""
    )

    return output

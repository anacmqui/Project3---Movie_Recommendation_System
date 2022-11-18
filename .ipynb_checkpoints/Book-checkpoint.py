import streamlit as st
import streamlit_book as stb
import pandas as pd
import numpy as np
import requests
import json
from datetime import time
from PIL import Image
import sklearn
from sklearn.neighbors import NearestNeighbors

#[theme]
base="light"

st.set_page_config(layout="wide")

stb.set_chapter_config(path="Streamlit/")
# importing required library for developing model and for doing data analysis
import pandas as pd
import glob
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn import model_selection
from sklearn.preprocessing import LabelEncoder

from flask import Flask, render_template
from flask import Flask, flash, request, redirect, url_for
import shutil
import os


UPLOAD_FOLDER = 'uploadFiles'
#initialize a variable with flask __name__ : referring to local python file
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#decorator -> a step before a function
@app.route("/")
def home_page():
    return render_template('home.html')


#dynamic route
@app.route("/healthcareclassification", methods=['GET', 'POST'])
def image_preprocessing():
    filepath = r'./data/external' #assuming the files are in same directory - as this notebook file is
    fileslist = glob.glob(filepath + "/Part1*.csv")

    li = []

    print("shape and size of each file :: \n")
    #importing all datasets, exploring each dataset shape and size
    for file in fileslist:
        df = pd.read_csv(file, index_col=None, header=0)
        print(file , " is of size :: ", df.size)
        print(file , " is having  ", df.shape[0], "rows,  and ", df.shape[1], " Columns \n")
        li.append(df)

    df_concatenated = pd.concat(li, axis=0, ignore_index=True)
    #Merge all datasets onto one

    #concatenated DataFrame
    print("Final dataframe shape :: " ,df_concatenated.shape)
    print("Final dataframe size",df_concatenated.size)

    return render_template('imagePreProcessing.html')
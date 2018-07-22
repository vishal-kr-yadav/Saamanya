import boto3
import pickle

import pandas as pd

s3 = boto3.client(
    's3',
    aws_access_key_id="",
    aws_secret_access_key=""
    # aws_session_token=SESSION_TOKEN,
)

bucket = ""
file_name = "trainings/output/final_model.pickle"



obj = s3.get_object(Bucket= bucket, Key= file_name)

nb_detector = pickle.loads(obj['Body'].read())


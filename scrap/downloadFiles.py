#!/usr/bin/python3
import requests

def downloadPdf(file_url):

    r = requests.get(file_url, stream=True)
    fileName =file_url.split('/')[-1]

    with open(fileName, "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):

            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)

def downLoadPng(image_url):

    # URL of the image to be downloaded is defined as image_url
    r = requests.get(image_url)  # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    fileName =image_url.split('/')[-1]
    with open(fileName, 'wb') as f:
        # Saving received content as a png file in
        # binary format

        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)

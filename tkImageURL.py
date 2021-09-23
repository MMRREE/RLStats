import requests as req
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO


def tkLabelImageURL(imageURL="https://cdn.icon-icons.com/icons2/1380/PNG/512/vcsconflicting_93497.png", master=None, ):
    imageReq = req.get(imageURL)
    photo = Image.open(BytesIO(imageReq.content))
    photo = photo.resize((120, 120), Image.ANTIALIAS)
    userImageRaw = ImageTk.PhotoImage(image=photo)
    returnLabel = tk.Label(master, image=userImageRaw)
    returnLabel.image = userImageRaw
    return returnLabel
# End of tkLabelImageURL


def tkRawImageURL(imageURL="https://cdn.icon-icons.com/icons2/1380/PNG/512/vcsconflicting_93497.png"):
    imageReq = req.get(imageURL)
    photo = Image.open(BytesIO(imageReq.content))
    photo = photo.resize((120, 120), Image.ANTIALIAS)
    userImageRaw = ImageTk.PhotoImage(image=photo)
    return userImageRaw
# End of tkRawImageURL

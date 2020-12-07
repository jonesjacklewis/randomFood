from tkinter import *

def getJSON(u):
    import requests, json

    r = requests.get(u)

    binaryContent = r.content
    stringContent = binaryContent.decode("utf8")
    jsonContent = json.loads(stringContent)

    return jsonContent


def getJSONElement(jsonContent, element):
    data = jsonContent.get(element)

    return data

def saveImageFromURL(u, destination):
    import requests

    r = requests.get(u)

    with open(destination, "wb") as f:
        f.write(r.content)

def displayImage(img, title="Image"):
    from PIL import ImageTk, Image

    root = Toplevel()

    root.title(title)
    root.wm_attributes("-transparentcolor", "white")
    root.resizable(False, False)

    img = ImageTk.PhotoImage(Image.open(img))

    canv = Canvas(root, width=img.width(), height=img.height())
    canv.grid(row=2, column=3)
    canv.create_image(0, 0, anchor=NW, image=img)

    mainloop()
    root.destroy()


def interface():
    import PySimpleGUI as sg

    layout = [
        [sg.Text("Random Food Generator")],
        [sg.Text("Generate a random image of some food")],
        [sg.Button("Random Food")]
        ]

    window = sg.Window("Random Food Generator", layout, element_justification = 'c')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Random Food":
            jsonObject = getJSON("https://foodish-api.herokuapp.com/api/")
            foodURL = getJSONElement(jsonObject, "image")

            saveImageFromURL(foodURL, "image.jpg")
            displayImage("image.jpg")
    window.close()
    quit()
    

interface()
#displayImage("image.jpg", "food")
    

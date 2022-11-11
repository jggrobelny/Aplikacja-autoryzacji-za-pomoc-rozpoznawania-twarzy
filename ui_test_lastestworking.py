import pickle
import tkinter as tk
from tkinter import ttk

import PIL.Image
import PIL.ImageTk
import cv2

LARGE_FONT = ("Verdana", 12)


#################################################################
#                                                               #
# TODO:         vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv        #
#                IMPLEMENT TAKING AND SAVING PICTURES           #
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        #
#                                                               #
# TODO:         IMPLEMENT ADDING NEW USER                       #
#                   MAKE BUTTON ACTIVE IF TEXT IS ENTERED       #
#                   CREATE NEW FOLDER WITH USER'S NAME          #
#                   IMPLEMENT TAKING PHOTOS OF USER FOR REG     #
#                   ADD BUTTON FOR RUNNING TRAIN.PY             #
#                   ADD INSTRUCTIONS                            #
#                                                               #
# TODO:         AFTER TAKING PHOTOS IMPLEMENT TRAIN.PY          #
#               FIX CLOSING CV2 AFTER CLOSING APP               #
#                                                               #
#################################################################

class AutoryzacjaApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Global variable for managing cv2 functions on multiple frames
        global key, update_on, update_on_reg, key_reg
        key, update_on, update_on_reg, key_reg = False, False, False, False

        # Setting icon, title and initializing GUI
        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Aplikacja auroryzacji za pomocą rozponawania twarzy")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (EkranStartowy, EkranGlowny, EkranRejestracja):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(EkranStartowy)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def key_switch(self, cont):
        global key, update_on
        key, update_on = cont, cont

    def key_switch_reg(self, cont):
        global key_reg, update_on_reg
        key_reg, update_on_reg = cont, cont


class EkranStartowy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Loading image and putting it on the canvas
        self.cv_img = cv2.cvtColor(cv2.imread("obraz.jpg"), cv2.COLOR_BGR2RGB)
        self.height, self.width, no_channels = self.cv_img.shape
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Creating label and buttons
        label = tk.Label(self, text="Praca inżynierska \n Jakub Grobelny", font=LARGE_FONT)
        label.pack()
        btn = ttk.Button(self, text="start", command=lambda: [controller.show_frame(EkranRejestracja),
                                                              controller.key_switch(False),
                                                              controller.key_switch_reg(True)])
        # TODO: ABOVE IS TEMP FIX TO BYPASS MAIN SCREEN AND GO STRAIGHT INTO REG SCREEN // CPY BELOW TO RETURN TO NORMAL
        # [controller.show_frame(EkranGlowny),
        # controller.key_switch(True)]

        btn.pack()


class EkranGlowny(tk.Frame):

    def __init__(self, parent, controller, video_source=0):
        tk.Frame.__init__(self, parent)

        # Validation variables
        self.validation_count = 0
        self.id_validation = False
        # Init cam and recognizer
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        self.face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("trainer.yml")

        # Creating label and button
        label = tk.Label(self,
                         text="W celu autoryzacji przybliż twarz i zaczekaj aż żółta ramka zmieni kolor na zieloną",
                         font=LARGE_FONT)
        label.pack()
        self.btn_reg = ttk.Button(self, text="Zarejestruj nowa osobe",
                                  command=lambda: [controller.show_frame(EkranRejestracja),
                                                   controller.key_switch(False),
                                                   controller.key_switch_reg(True)])

        # Refresh interval
        self.interval = 20
        self.canvas = tk.Canvas(self, width=900, height=400)
        self.canvas.pack()

        # Looks for changes in global variable to update or to not update img
        # which avoids multiple cv2windows in background that create lags
        self.key_receiver()
        self.btn_reg.place(relx=0.5, rely=0.9)

    def key_receiver(self):
        global key
        if key:
            self.update_image()
            key = False
        self.after(200, self.key_receiver)

    def update_image(self):

        # Loading labels
        labels = {"persons_name": 1}
        with open("pickles/labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}

        # Reading camera and painting frame
        ret, vid_frame = self.vid.read()
        gray = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            id_, conf = self.recognizer.predict(roi_gray)

            # Face is recognized
            if 35 <= conf <= 65:
                name = labels[id_]
                self.validation_count += 1

                # Validating if in 15 tries user gets recognized with no bad matches
                if not self.id_validation:
                    color = (30, 255, 255)  # yellow
                if self.validation_count > 15:
                    color = (0, 255, 0)  # green
                    self.id_validation = True

            # No match with database
            else:
                name = "Unknown"
                color = (0, 0, 255)  # red
                self.validation_count = 0
                self.id_validation = False

            # Drawing rectangle around detected face
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(vid_frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Labeling the face
            color = (0, 0, 0)  # black
            stroke = 2
            cv2.putText(vid_frame, name, (x, y), font, 2, color, stroke, cv2.LINE_AA)

        # Validation
        if self.id_validation:
            img_path = "autoryzacja_udana.png"
            self.btn_reg["state"] = "enabled"
        else:
            img_path = "autoryzacja_nieudana.png"
            self.btn_reg["state"] = "disabled"

        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2RGB)  # to RGB
        self.image = PIL.Image.fromarray(self.image)  # to PIL format
        self.image = PIL.ImageTk.PhotoImage(self.image)  # to ImageTk format

        # Update cam image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        # Create authorization pictures
        self.auth_img = tk.PhotoImage(file=img_path)
        self.canvas.create_image(650, 100, anchor=tk.NW, image=self.auth_img)
        # Repeat every 'interval' ms
        if update_on:
            self.canvas.after(self.interval, self.update_image)


class EkranRejestracja(tk.Frame):
    def __init__(self, parent, controller, video_source=0):
        tk.Frame.__init__(self, parent)

        # creating label and buttons
        label = tk.Label(self, text="Ekran rejestracja", font=LARGE_FONT)
        label.place(relx=0.5, rely=0.01)
        btn_reg = ttk.Button(self, text="Stwórz nowego użytkownika")
        btn_reg.place(relx=0.75, rely=0.5)  # TODO: ADD COMMAND
        btn_back = ttk.Button(self, text="cofnij", command=lambda: [controller.show_frame(EkranGlowny),
                                                                    controller.key_switch(True),
                                                                    controller.key_switch_reg(False)])
        btn_back.place(relx=0.5, rely=0.9)

        # Text entry
        name_entry = tk.Entry(self)
        name_label = tk.Label(self, text="Imie i nazwisko", font=LARGE_FONT)
        name_label.place(relx=0.75, rely=0.3)
        name_entry.place(relx=0.75, rely=0.35)

        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        self.face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

        # Refresh interval
        self.interval = 20

        self.canvas = tk.Canvas(self, width=700, height=400)
        self.canvas.place(relx=0.01, rely=0.05)
        self.key_receiver()

    def key_receiver(self):
        global key_reg
        if key_reg:
            self.update_image()
            key_reg = False
        self.after(200, self.key_receiver)

    def update_image(self):

        # Reading camera and painting frame
        ret, vid_frame = self.vid.read()
        gray = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            # Drawing rectangle around detected face
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(vid_frame, (x, y), (end_cord_x, end_cord_y), (30, 255, 255), stroke)

        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2RGB)  # to RGB
        self.image = PIL.Image.fromarray(self.image)  # to PIL format
        self.image = PIL.ImageTk.PhotoImage(self.image)  # to ImageTk format

        # Update cam image
        self.canvas.create_image(325, 200, image=self.image)
        # Repeat every 'interval' ms
        if update_on_reg:
            self.canvas.after(self.interval, self.update_image)


app = AutoryzacjaApp()
app.geometry("1024x576")
app.mainloop()
cv2.destroyAllWindows()

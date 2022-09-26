import pickle
import tkinter as tk
from tkinter import ttk

import PIL.Image
import PIL.ImageTk
import cv2

LARGE_FONT = ("Verdana", 12)


class AutoryzacjaApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting icon, title and initializing GUI
        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Aplikacja auroryzacji za pomocą rozponawania twarzy")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=100, pady=50)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (EkranStartowy, EkranGlowny, EkranRejestracja):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(EkranStartowy)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class EkranStartowy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # loading image and putting it on the canvas
        self.cv_img = cv2.cvtColor(cv2.imread("obraz.jpg"), cv2.COLOR_BGR2RGB)
        self.height, self.width, no_channels = self.cv_img.shape
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # creating label and buttons
        label = tk.Label(self, text="Praca inżynierska \n Jakub Grobelny", font=LARGE_FONT)
        label.pack()
        btn = ttk.Button(self, text="start", command=lambda: controller.show_frame(EkranGlowny))
        btn.pack()


class EkranGlowny(tk.Frame):

    def __init__(self, parent, controller, video_source=0):
        tk.Frame.__init__(self, parent)

        # validation variables
        self.validation_count = 0
        self.id_validation = False
        # TODO: validation images
        # TODO: auth_img = tk.PhotoImage(file=auth_img_path)
        # TODO: self.cv_img2 = cv2.cvtColor(cv2.imread(auth_img_path), cv2.COLOR_BGR2RGB)

        # init cam and recognizer
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        self.face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("trainer.yml")
        # TODO: OGARNAC WRZUCANIE OBRAZOW AUTORYZACJI -> CANVAS? -> LABEL? MOZE ZMIENIC ROZMIAR CANVAS I OKNA IDK //////

        # refresh interval
        self.interval = 20
        self.canvas = tk.Canvas(self, width=600, height=400)
        # self.canvas.create_image(1, 1, image=auth_img, anchor="s")
        self.canvas.pack()
        self.update_image()

        # creating label and button
        label = tk.Label(self, text="e2", font=LARGE_FONT)
        label.pack()
        btn_rej = ttk.Button(self, text="Zarejestruj nowa osobe",
                             command=lambda: controller.show_frame(EkranRejestracja))
        btn_rej.pack()

    def update_image(self):

        # loading labels
        global color
        labels = {"persons_name": 1}
        with open("pickles/labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}

        # reading camera and painting frame
        ret, vid_frame = self.vid.read()
        gray = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            id_, conf = self.recognizer.predict(roi_gray)

            # face is recognized
            if 35 <= conf <= 65:
                name = labels[id_]
                self.validation_count += 1

                # validating if in 10 tries user gets access with no bad matches
                if not self.id_validation:
                    color = (30, 255, 255)  # yellow
                if self.validation_count > 10:
                    color = (0, 255, 0)  # green
                    self.id_validation = True

            # no match with database
            else:
                name = "Unknown"
                color = (0, 0, 255)  # red
                self.validation_count = 0
                self.id_validation = False

            # drawing rectangle around detected face
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(vid_frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
            font = cv2.FONT_HERSHEY_SIMPLEX

            # labeling the face
            color = (0, 0, 0)  # black
            stroke = 2
            cv2.putText(vid_frame, name, (x, y), font, 2, color, stroke, cv2.LINE_AA)

        # validation TODO: FINISH THIS PART below works but need to implement photo for those etc
        if self.id_validation:
            # auth_img_path = "autoryzacja_udana.jpg"
            print("test_auth")
        else:
            print("no auth")
            # auth_img_path = "autoryzacja_nieudana.jpg"

        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2RGB)  # to RGB
        self.image = PIL.Image.fromarray(self.image)  # to PIL format
        self.image = PIL.ImageTk.PhotoImage(self.image)  # to ImageTk format

        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Repeat every 'interval' ms
        self.canvas.after(self.interval, self.update_image)


class EkranRejestracja(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # creating label and buttons
        # TO DO: PUT LABEL IN TK.FRAME SO IT DOESN'T HAVE TO BE CREATED HERE
        label = tk.Label(self, text="e3", font=LARGE_FONT)
        label.pack()
        btn = ttk.Button(self, text="cofnij", command=lambda: controller.show_frame(EkranGlowny))
        btn.pack()

        # TODO: CREATE FUNCTION OF ADDING NEW USER
        #   ADD WIDGET FOR TEXT ENTRY
        #   CREATE NEW FOLDER
        #   SAVE PHOTOS FROM CAMERA OR CHOOSE FILES FROM FILE EXPLORER
        #   SET ACCESS LEVEL


app = AutoryzacjaApp()
app.mainloop()
cv2.destroyAllWindows()

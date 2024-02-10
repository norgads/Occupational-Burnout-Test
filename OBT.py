from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import csv

#TODO implement category check

#dictionary with questions and user answers
data = dict()

data[1,0] = "Test Question 1"
data[2,0] = "Test Question 2"
data[3,0] = "Test Question 3333333333333333"

data[1,1] = None #TODO category
data[2,1] = None
data[3,1] = None

data[1,2] = 1  #TrueAns
data[2,2] = 0
data[3,2] = 1

data[1,3] = 4  #Value
data[2,3] = 3
data[3,3] = 7

data[1,4] = None #Ans
data[2,4] = None
data[3,4] = None

with open("OBTru.csv", newline='') as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)
    reader = csv.reader(file)
    if has_header:
        next(reader)
    i = 1
    for row in reader:
        data[i,0] = row[0]
        data[i,2] = int(row[2])
        data[i,3] = int(row[3])
        i += 1
        


#*Qt GUI'''

app = QApplication([])
app.setStyleSheet("QLabel{font-size: 35pt; text-align: justify;} QPushButton{font-size: 20pt; border: 5px solid black; border-radius: 15px}")
win = QWidget()
win.cur_num = 0
win.score = 0
win.setWindowTitle("Occupational Burnout Test")
win.resize(700, 500)
btn_yes = QPushButton("Yes")
btn_no = QPushButton("No")
lbl_q = QLabel("Question")
lbl_q.setWordWrap(True)

vline = QVBoxLayout()
hline = QHBoxLayout()

hline.addWidget(btn_yes)
hline.addWidget(btn_no)
vline.addWidget(lbl_q, stretch=60, alignment=Qt.AlignCenter)
vline.addLayout(hline, stretch=40)
win.setLayout(vline)

#*Events
def next_q():
    if win.cur_num == len(data)/5: #?add automatic columns count? Maybe remove on release at all
        win.cur_num = 0
    win.cur_num += 1
    lbl_q.setText(data[win.cur_num,0])

def check():
    if data[win.cur_num, 4] == data[win.cur_num, 2]:
        win.score += data[win.cur_num, 3]

def transition():
    #print(data) #check for small size samples
    check()
    print(win.score)
    next_q()

def ans_yes():
    data[win.cur_num, 4] = 1
    transition()
    
def ans_no():
    data[win.cur_num, 4] = 0
    transition()

btn_no.clicked.connect(ans_no)
btn_yes.clicked.connect(ans_yes)

next_q()


win.show()
app.exec()
#'''

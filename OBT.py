from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

#dictionary with questions and user answers
data = dict()
data[1,0] = "Test Question 1"
data[2,0] = "Test Question 2"
data[3,0] = "Test Question 3333333333333333"

data[1,1] = None
data[2,1] = None
data[3,1] = None

#*Qt GUI

app = QApplication([])
app.setStyleSheet("QLabel{font-size: 38pt;}")
win = QWidget()
win.cur_num = 0
win.setWindowTitle("Ocupattional Burnout Test")
win.resize(700, 500)
btn_yes = QPushButton("Yes")
btn_no = QPushButton("No")
lbl_q = QLabel("Question")
lbl_q.setWordWrap(True)

vline = QVBoxLayout()
hline = QHBoxLayout()

hline.addWidget(btn_yes)
hline.addWidget(btn_no)
vline.addWidget(lbl_q, stretch=70, alignment=Qt.AlignCenter)
vline.addLayout(hline, stretch=30)
win.setLayout(vline)

#*Events
def next():
    if win.cur_num == len(data)/2:
        win.cur_num = 0
    win.cur_num += 1
    lbl_q.setText(data[win.cur_num,0])

def ans_yes():
    data[win.cur_num, 1] = 1
    next()
    print(data)

def ans_no():
    data[win.cur_num, 1] = 0
    next()
    print(data)

btn_no.clicked.connect(ans_no)
btn_yes.clicked.connect(ans_yes)

next()


win.show()
app.exec()

################################################################################
#### Made by Thanawat Sukamporn ; President of Return to monkey - Tech Team ####
################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btncreate = QtWidgets.QPushButton(self.centralwidget)
        self.btncreate.setGeometry(QtCore.QRect(30, 140, 731, 31))
        self.btncreate.setObjectName("btncreate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtsetpath = QtWidgets.QTextEdit(self.centralwidget)
        self.txtsetpath.setGeometry(QtCore.QRect(190, 90, 451, 31))
        self.txtsetpath.setObjectName("txtsetpath")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnmakedataset = QtWidgets.QPushButton(self.centralwidget)
        self.btnmakedataset.setGeometry(QtCore.QRect(30, 230, 251, 31))
        self.btnmakedataset.setObjectName("btnmakedataset")
        self.btnaddclass = QtWidgets.QPushButton(self.centralwidget)
        self.btnaddclass.setGeometry(QtCore.QRect(30, 270, 251, 31))
        self.btnaddclass.setObjectName("btnaddclass")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 230, 331, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.btncalllabel = QtWidgets.QPushButton(self.centralwidget)
        self.btncalllabel.setGeometry(QtCore.QRect(290, 230, 131, 71))
        self.btncalllabel.setObjectName("btncalllabel")
        self.btnselect = QtWidgets.QPushButton(self.centralwidget)
        self.btnselect.setGeometry(QtCore.QRect(650, 90, 111, 31))
        self.btnselect.setObjectName("btnselect")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btncreate.clicked.connect(self.create_folder)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect btnselect to the folder selection function
        self.btnselect.clicked.connect(self.select_folder)
        self.btnmakedataset.clicked.connect(self.create_yaml)
        self.btncalllabel.clicked.connect(self.call_labelimg)
        self.btnaddclass.clicked.connect(self.open_yaml_file)
        self.pushButton_4.clicked.connect(self.run_train)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RTM Yolov8 master"))
        self.label.setText(_translate("MainWindow", "Yolov8 Trainer and dataset maker"))
        self.btncreate.setText(_translate("MainWindow", "Click to create workspace"))
        self.label_3.setText(_translate("MainWindow", "Setting the path :"))
        self.label_4.setText(_translate("MainWindow", "Create the dataset.yaml file :"))
        self.btnmakedataset.setText(_translate("MainWindow", "Click to create dataset"))
        self.btnaddclass.setText(_translate("MainWindow", "Click to add class"))
        self.pushButton_4.setText(_translate("MainWindow", "Train Image"))
        self.btncalllabel.setText(_translate("MainWindow", "labelimg"))
        self.btnselect.setText(_translate("MainWindow", "select"))

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder_path:
            self.txtsetpath.setText(folder_path)

    def create_folder(self):
        folder_path = self.txtsetpath.toPlainText()
        if folder_path:
            try:
                os.makedirs(f"{folder_path}/dataset", exist_ok=True)
                os.makedirs(f"{folder_path}/dataset/train", exist_ok=True)
                os.makedirs(f"{folder_path}/dataset/train/images", exist_ok=True)
                os.makedirs(f"{folder_path}/dataset/train/labels", exist_ok=True)
                os.makedirs(f"{folder_path}/dataset/val", exist_ok=True)
                os.makedirs(f"{folder_path}/dataset/val/images", exist_ok=True)
                os.makedirs(f"{folder_path}/dataset/val/labels", exist_ok=True)

                QMessageBox.information(None, "Success", f"Folder created at: {folder_path}")

                os.startfile(f"{folder_path}/dataset")

            except Exception as e:
                QMessageBox.critical(None, "Error", f"Failed to create folder: {str(e)}")

    def create_yaml(self):

        folder_path = self.txtsetpath.toPlainText()
        # Specify the file name
        data = f"""path: {folder_path}/dataset
train: train/images
val: val/images

names:
"""
        file_name = f"{folder_path}/dataset/dataset.yaml"
        QMessageBox.information(None, "Success", f"yaml dataset file created at: {folder_path}/dataset/dataset.yaml")

        # Create the file
        with open(file_name, 'w') as file:
            file.write(data)
            print(f"File '{file_name}' created successfully.")

    def call_labelimg(self):
        try:
            subprocess.Popen(["labelImg"])  # Adjust path if 'labelImg' isn't in PATH
            QMessageBox.information(None, "LabelImg", "LabelImg opened successfully.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to open LabelImg: {str(e)}")

    def open_yaml_file(self):
        folder_path = self.txtsetpath.toPlainText()
        txt_file = os.path.join(f"{folder_path}/dataset/dataset.yaml")  # Specify your .txt file name here

        try:
            subprocess.Popen(["notepad.exe", txt_file])  # Open the .txt file in Notepad
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to open file: {str(e)}")

    def run_train(self):
        import subprocess
        folder_path = self.txtsetpath.toPlainText()
        # Specify the command you want to run
        command = f"""cd {folder_path}/dataset & yolo train data=dataset.yaml model=yolov8n.pt epochs=10 imgsz=640"""

        # Open a new command prompt window and run the command
        subprocess.Popen(f'start cmd /k "{command}"', shell=True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

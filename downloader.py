# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox,QFileDialog
from PySide6.QtUiTools import QUiLoader

import  urllib.request

class downloader(QWidget):
    def __init__(self):
        super(downloader, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_Browse.clicked.connect(self.browse)

    def download(self):
        url= self.ui.lineEdit_url.text()
        file=self.ui.lineEdit_file.text()

        try:
            urllib.request.urlretrieve(url,file,self.report)
        except Exception:
            QMessageBox.warning(self,'Warning','The download failed')
            return

        QMessageBox.information(self,'Information','The download is complete')
        self.ui.progressBar.setValue(0)
        self.ui.lineEdit_url.setText("")
        self.ui.lineEdit_file.setText("")

    def report(self,blocknum,blocksize,totalsize):
        readsofar=blocknum * blocksize
        if blocksize >0 :
            percent=readsofar*100/totalsize
            self.ui.progressBar.setValue(int(percent))
    def browse(self):
        save_file=QFileDialog.getSaveFileName(self,"Save File As",filter="All Files(*.*",dir=".")
        self.ui.lineEdit_file.setText(save_file[0])

if __name__ == "__main__":
    app = QApplication([])
    window = downloader()
    # window.show()
    sys.exit(app.exec_())

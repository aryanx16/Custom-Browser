import os
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialogButtonBox,
    QDialog,
    QVBoxLayout,
    QLabel
)


class AboutDialog(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.layout = QVBoxLayout()

        ok_btn = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(ok_btn)

        self.init_ui()

    def init_ui(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        with open(os.path.join(os.path.dirname(__file__), "..", "..", "..", "utils", "styles", "about_style.css")) as f:
            self.button_box.button(QDialogButtonBox.Ok).setStyleSheet(f.read())

        logo = QLabel()
        pixmap = QPixmap(os.path.join(os.path.dirname(__file__), "..", "..", "..", "utils", "resources", "logos", "browser.png"))
        pixmap = pixmap.scaled(80, 80)
        logo.setPixmap(pixmap)
        self.layout.addWidget(logo)

        title = QLabel("Simple Web Browser")
        title.setFont(QFont("Times", 20))

        self.layout.addWidget(title)

        lbl1 = QLabel(
            '<center>Version 2.4<br>Copyright ©2021 Made with <3 by Akshit.</center>'
        )
        lbl1.setFont(QFont("Times", 10))
        lbl1.setOpenExternalLinks(True)
        self.layout.addWidget(lbl1)

        github_pg = QLabel(
            '<a href="https://github.com/avengers2405/pict-chromium-browser/tree/embedded">Learn More </a>'
        )

        font = QFont("Font Awesome 5 Free Solid", 10)
        github_pg.setFont(font)
        github_pg.setOpenExternalLinks(True)
        self.layout.addWidget(github_pg)

        for i in range(0, self.layout.count()):
            self.layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        self.layout.addWidget(self.button_box)

        self.setLayout(self.layout)

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.resize(400, 250)
        self.setMaximumHeight(300)
        self.setMaximumWidth(500)
        self.setWindowTitle("About")

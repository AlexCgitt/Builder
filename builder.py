import sys
from abc import abstractmethod, ABC

from PyQt5.QtWidgets import (QApplication, QMessageBox, QHBoxLayout, QPushButton,
                             QWidget, QVBoxLayout, QLineEdit, QTextEdit, QLabel)

class DialogBox(QWidget):

    def __init__(self):
        super().__init__()

        v_layout = QVBoxLayout()

        self.__h_layout2 = QHBoxLayout()
        self.__h_layout1 = QHBoxLayout()

        v_layout.addLayout(self.__h_layout1)
        v_layout.addLayout(self.__h_layout2)

        self.setLayout(v_layout)

    def set_title(self, title: str) -> None:
        self.setWindowTitle(title)

    def set_text(self, label: QLabel) -> None:
        self.__h_layout1.addWidget(label)

    """C'est mieux d'utiliser add button plusieurs fois"""
    def set_button_one(self, button: QPushButton) -> None:
        self.__h_layout2.addWidget(button)

    def set_button_two(self, button: QPushButton) -> None:
        self.__h_layout2.addWidget(button)


class DialogBoxBuilder(ABC):
    def __init__(self):
        self._dialog_box = None

    def create_new_dialog_box(self) -> None:
        self._dialog_box = DialogBox()

    def get_dialog_box(self) -> None:
        return self._dialog_box

    @abstractmethod
    def build_title(self) -> None:
        pass

    @abstractmethod
    def build_text(self) -> None:
        pass

    @abstractmethod
    def build_button_one(self) -> None:
        pass

    @abstractmethod
    def build_button_two(self) -> None:
        pass


class DialogBoxOneButtonBuilder(DialogBoxBuilder):

    def build_title(self) -> None:
        self._dialog_box.set_title("Dialog box - one button")

    def build_text(self) -> None:
        self._dialog_box.set_text(QLabel("This is a dialog box with one button"))

    def build_button_one(self) -> None:
        self._dialog_box.set_button_one(QPushButton("Ok"))

    def build_button_two(self) -> None:
        pass


class DialogBoxTwoButtonBuilder(DialogBoxBuilder):

    def build_title(self) -> None:
        self._dialog_box.set_title("Dialog box - one button")

    def build_text(self) -> None:
        self._dialog_box.set_text(QLabel("This is a dialog box with two buttons"))

    def build_button_one(self) -> None:
        self._dialog_box.set_button_one(QPushButton("Ok"))

    def build_button_two(self) -> None:
        self._dialog_box.set_button_two(QPushButton("Cancel"))

class DialogBoxDirector:
    
    def __init__(self):
        self.__dialog_box_builder: DialogBoxBuilder = None
    
    def get_dialog_box(self) -> DialogBox:
        return self.__dialog_box_builder.get_dialog_box()
    
    def set_dialog_box_builder(self, dialog_box_builder: DialogBoxBuilder):
        self.__dialog_box_builder = dialog_box_builder

    def build_dialog_box(self) -> None:
        self.__dialog_box_builder.create_new_dialog_box()
        self.__dialog_box_builder.build_title()
        self.__dialog_box_builder.build_text()
        self.__dialog_box_builder.build_button_one()
        self.__dialog_box_builder.build_button_two()






if __name__ == "__main__":

    app = QApplication(sys.argv)

    dialog_box_director: DialogBoxDirector = DialogBoxDirector()
    #one_button_builder: DialogBoxOneButtonBuilder = DialogBoxOneButtonBuilder()

    #dialog_box.set_title("Mon petit titre")
    #dialog_box.set_text(QLabel("Mon texte"))
    #dialog_box.set_button_one(QPushButton("petit 1"))
    #dialog_box.set_button_two(QPushButton("petit 2"))
    #dialog_box.setMinimumSize(350, 350)

    """one_button_builder.create_new_dialog_box()
    one_button_builder.build_title()
    one_button_builder.build_text()
    one_button_builder.build_button_one()
    one_button_builder.build_button_two()
    dialog_box = one_button_builder.get_dialog_box()
    dialog_box.show()"""

    one_button_builder = DialogBoxTwoButtonBuilder()
    dialog_box_director.set_dialog_box_builder(one_button_builder)
    dialog_box_director.build_dialog_box()
    dialog_box: DialogBox = dialog_box_director.get_dialog_box()
    dialog_box.show()

    sys.exit(app.exec_())





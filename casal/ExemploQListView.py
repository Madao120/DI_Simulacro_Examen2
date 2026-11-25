import sys
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
);
from PyQt6.QtCore import *

from modeloTablaCasal import ModeloTablaCasal


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fiesta Principal")

        self.setMinimumSize(425, 200)
        self.setMaximumSize(1000, 1000)

        caixaV = QVBoxLayout()

        self.datos = [["Nome","DNI","Xenero","Falecimiento"],
                 ["Ana Perez","1111R","Muller",False],
                 ["Paco Porras","2222T","Home",True],
                 ["Roque Vila","3333H","Home",False]]

        self.modelo = ModeloTablaCasal(self.datos)

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setModel(self.modelo)

        # Botón de anadir línea

        self.layoutPersona = QVBoxLayout()

        self.nombrePersona = QLineEdit()
        self.dniPersona = QLineEdit()
        self.sexoPersona = QComboBox()
        self.sexoPersona.addItems(["Muller","Home"])
        self.fallecimientoPersona = QCheckBox()

        self.layoutPersona.addWidget(self.nombrePersona)
        self.layoutPersona.addWidget(self.dniPersona)
        self.layoutPersona.addWidget(self.sexoPersona)
        self.layoutPersona.addWidget(self.fallecimientoPersona)

        self.anadirPersona = QWidget()
        self.anadirPersona.setLayout(self.layoutPersona)

        # Botón Anadir persona

        self.btnAnadirPersona = QPushButton("Anadir")
        self.btnAnadirPersona.clicked.connect(self.fnAnadirPersona)

        caixaV.addWidget(self.tvwTaboa)
        caixaV.addWidget(QLabel("Anadir Persona"))
        caixaV.addWidget(self.anadirPersona)
        caixaV.addWidget(self.btnAnadirPersona)



        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()

    def fnAnadirPersona(self):
        nombre = self.nombrePersona.text()
        dni = self.dniPersona.text()
        sexo = self.sexoPersona.currentText()
        fallecido = self.fallecimientoPersona.isChecked()

        self.datos.append([nombre, dni, sexo, fallecido])
        self.modelo.layoutChanged.emit()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
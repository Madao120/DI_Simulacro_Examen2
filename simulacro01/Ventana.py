import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ModeloTabla import ModeloTabla

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario con páginas")
        self.setMaximumSize(500, 700)
        self.setMinimumSize(300, 500)

        # WIDGET CENTRAL
        central = QWidget()
        self.setCentralWidget(central)

        # GRID PRINCIPAL
        grid = QGridLayout()
        central.setLayout(grid)

        # SELECTOR DE PÁGINAS
        opciones = QComboBox()
        opciones.addItems(["Nombre", "Edad", "Ciudad"])

        # STACK
        stack = QStackedLayout()

        # PÁGINA 1
        pagina1 = QWidget()
        grid1 = QGridLayout()

        self.activar = QCheckBox("Activar")
        self.activar.clicked.connect(self.activarZona)

        grid1.addWidget(self.activar, 0, 0)

        self.nombre = QLineEdit("Nombre de la persona")
        self.btnNombre = QPushButton("Guardar nombre")
        self.btnNombre.clicked.connect(self.guardarNombre)

        grid1.addWidget(self.nombre, 1, 0)
        grid1.addWidget(self.btnNombre, 1, 1)

        self.descricion = QTextEdit("Descripción de la persona")
        grid1.addWidget(self.descricion, 2, 0, 2, 1)


        self.semanal = QRadioButton("Semanal")
        self.diario = QRadioButton("Diario")

        self.frecuencia = QGroupBox("Frecuencia de riego")
        self.frecuenciaLayout = QVBoxLayout()

        self.frecuenciaLayout.addWidget(self.semanal)
        self.frecuenciaLayout.addWidget(self.diario)

        self.frecuencia.setLayout(self.frecuenciaLayout)
        grid1.addWidget(self.frecuencia, 2, 1, 2, 1)


        self.semana = QGroupBox("Semana")

        self.groupBoxH = QHBoxLayout()

        self.lunes = QCheckBox("Lunes")
        self.martes = QCheckBox("Martes")
        self.miercoles = QCheckBox("Miercoles")
        self.jueves = QCheckBox("Jueves")
        self.viernes = QCheckBox("Viernes")
        self.sabado = QCheckBox("Sabado")
        self.domingo = QCheckBox("Domingo")

        self.groupBoxH.addWidget(self.lunes)
        self.groupBoxH.addWidget(self.martes)
        self.groupBoxH.addWidget(self.miercoles)
        self.groupBoxH.addWidget(self.jueves)
        self.groupBoxH.addWidget(self.viernes)
        self.groupBoxH.addWidget(self.sabado)
        self.groupBoxH.addWidget(self.domingo)

        self.semana.setLayout(self.groupBoxH)

        grid1.addWidget(self.semana, 4, 0, 2, 2)

        pagina1.setLayout(grid1)

        # PÁGINA 2: EDAD
        pagina2 = QWidget()
        grid2 = QGridLayout()

        self.historial = QTextEdit()

        grid2.addWidget(QLabel("Historial:"), 0, 0)
        grid2.addWidget(self.historial, 0, 1)

        pagina2.setLayout(grid2)

        # PÁGINA 3: CIUDAD
        pagina3 = QWidget()
        grid3 = QGridLayout()

        # Encabezados de las columnas.
        cabeceras = ["Nombre", "DNI", "Activo"]

        # Cada lista interior representa una fila.
        datos = [
            ["Ana", "1111A", True],
            ["Paco", "2222B", False],
            ["Maria", "3333C", True]
        ]

        # Creamos el modelo y le pasamos encabezados y datos.
        self.modelo = ModeloTabla(cabeceras, datos)

        # Creamos la vista y conectamos el modelo.
        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)

        # Colocamos la tabla en el grid
        grid3.addWidget(QLabel("Tabla de datos:"), 0, 0)
        grid3.addWidget(self.tabla, 1, 0)


        pagina3.setLayout(grid3)

        # AÑADIR PÁGINAS AL STACK
        stack.addWidget(pagina1)
        stack.addWidget(pagina2)
        stack.addWidget(pagina3)

        # AÑADIR ELEMENTOS AL GRID PRINCIPAL
        grid.addWidget(opciones, 0, 0)
        grid.addLayout(stack, 1, 0)

        # CONECTAR SELECTOR CON STACKx
        opciones.currentIndexChanged.connect(stack.setCurrentIndex)

        opciones.setCurrentIndex(2)

        # Desactivar todo
        self.descricion.setEnabled(False)
        self.semana.setEnabled(False)
        self.semanal.setEnabled(False)
        self.diario.setEnabled(False)
        self.lunes.setEnabled(False)
        self.martes.setEnabled(False)
        self.miercoles.setEnabled(False)
        self.jueves.setEnabled(False)
        self.sabado.setEnabled(False)
        self.viernes.setEnabled(False)
        self.domingo.setEnabled(False)


    def activarZona(self):
        if self.activar.isChecked():
            self.descricion.setEnabled(True)
            self.semana.setEnabled(True)
            self.semanal.setEnabled(True)
            self.diario.setEnabled(True)
            self.lunes.setEnabled(True)
            self.martes.setEnabled(True)
            self.miercoles.setEnabled(True)
            self.jueves.setEnabled(True)
            self.sabado.setEnabled(True)
            self.viernes.setEnabled(True)
            self.domingo.setEnabled(True)
            self.historial.insertPlainText("Zona activada \n")
        else:
            self.descricion.setEnabled(False)
            self.semana.setEnabled(False)
            self.semanal.setEnabled(False)
            self.diario.setEnabled(False)
            self.lunes.setEnabled(False)
            self.martes.setEnabled(False)
            self.miercoles.setEnabled(False)
            self.jueves.setEnabled(False)
            self.sabado.setEnabled(False)
            self.viernes.setEnabled(False)
            self.domingo.setEnabled(False)
            self.historial.insertPlainText("Zona desactivada \n")

    def guardarNombre(self):
        self.historial.insertPlainText(self.nombre.text()+"\n")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())
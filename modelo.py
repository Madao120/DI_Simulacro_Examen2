from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QColor


class ModeloTabla(QAbstractTableModel):

    def __init__(self, cabeceras, datos):
        super().__init__()
        self.cabeceras = cabeceras
        self.datos = datos

    def rowCount(self, indice):
        return len(self.datos)

    def columnCount(self, indice):
        return len(self.cabeceras)

    def data(self, indice, rol):

        if not indice.isValid():
            return None

        fila = indice.row()
        columna = indice.column()

        dato = self.datos[fila][columna]

        if rol == Qt.ItemDataRole.DisplayRole:
            if columna != 3:
                return dato

        return None

    def headerData(self, seccion, orientacion, rol):

        if rol == Qt.ItemDataRole.DisplayRole:

            if orientacion == Qt.Orientation.Horizontal:
                return self.cabeceras[seccion]

        return None

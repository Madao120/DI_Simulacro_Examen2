# Guía práctica de tablas con PyQt6

## QTableView + QAbstractTableModel

Esta guía construye una tabla paso a paso, manteniendo el **modelo** y
la **vista** separados.

La estructura del proyecto será:

``` text
Proyecto/
├── modelo.py
└── principal.py
```

-   `modelo.py`: contiene los datos y define cómo se muestran,
    modifican, insertan y eliminan.
-   `principal.py`: crea la ventana, la tabla, los botones y el
    formulario.

Los ejemplos están pensados para copiar y pegar. En cada apartado se
indica qué código debes añadir o sustituir.

------------------------------------------------------------------------

# 1. Tabla genérica: plantilla básica

Esta primera versión solamente muestra datos y encabezados. Todavía no
permite editar celdas ni contiene checkbox.

## Archivo `modelo.py`

``` python
from PyQt6.QtCore import QAbstractTableModel, Qt


class ModeloTabla(QAbstractTableModel):

    # Inicializa el modelo y guarda los encabezados y los datos.
    def __init__(self, cabeceras, datos):
        super().__init__()

        self.cabeceras = cabeceras
        self.datos = datos

    # Devuelve el número de filas que tiene la tabla.
    def rowCount(self, indice):
        return len(self.datos)

    # Devuelve el número de columnas que tiene la tabla.
    def columnCount(self, indice):
        return len(self.cabeceras)

    # Devuelve el contenido que debe mostrarse en una celda.
    def data(self, indice, rol):

        if not indice.isValid():
            return None

        if rol == Qt.ItemDataRole.DisplayRole:
            return self.datos[indice.row()][indice.column()]

        return None

    # Devuelve el texto de los encabezados de las columnas.
    def headerData(self, seccion, orientacion, rol):

        if rol == Qt.ItemDataRole.DisplayRole:

            if orientacion == Qt.Orientation.Horizontal:
                return self.cabeceras[seccion]

        return None
```

## Archivo `principal.py`

Este archivo está completo y se puede ejecutar directamente.

``` python
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTableView
)

from modelo import ModeloTabla


class VentanaPrincipal(QMainWindow):

    # Crea la ventana, los datos, el modelo y la vista de la tabla.
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi tabla PyQt6")
        self.resize(600, 300)

        # Encabezados de las columnas.
        cabeceras = ["Nombre", "DNI", "Edad"]

        # Cada lista interior representa una fila.
        datos = [
            ["Ana", "1111A", 25],
            ["Paco", "2222B", 30],
            ["Maria", "3333C", 28]
        ]

        # Creamos el modelo y le pasamos encabezados y datos.
        self.modelo = ModeloTabla(cabeceras, datos)

        # Creamos la vista y conectamos el modelo.
        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)

        # Colocamos la tabla en el diseño vertical.
        caja = QVBoxLayout()
        caja.addWidget(self.tabla)

        # Creamos el contenedor central de la ventana.
        contenedor = QWidget()
        contenedor.setLayout(caja)
        self.setCentralWidget(contenedor)


# Punto de entrada del programa.
if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
```

Para reutilizar esta plantilla, normalmente solo tendrás que cambiar los
encabezados y los datos:

``` python
cabeceras = ["Nombre", "DNI", "Edad"]

datos = [
    ["Ana", "1111A", 25],
    ["Paco", "2222B", 30]
]
```

------------------------------------------------------------------------

# 2. Funcionalidades paso a paso

A partir de aquí utilizaremos siempre estas columnas:

    Índice Columna   Comportamiento
  -------- --------- ----------------
         0 Nombre    Editable
         1 DNI       No editable
         2 Activo    Checkbox

Recuerda que los índices de las columnas empiezan en cero: la primera
columna es `0`, la segunda es `1` y la tercera es `2`.

## 2.1. Primera columna editable, segunda no editable y tercera checkbox

Sustituye el contenido de `modelo.py` por este modelo:

``` python
from PyQt6.QtCore import QAbstractTableModel, Qt


class ModeloTabla(QAbstractTableModel):

    # Inicializa el modelo y guarda los encabezados y los datos.
    def __init__(self, cabeceras, datos):
        super().__init__()

        self.cabeceras = cabeceras
        self.datos = datos

    # Devuelve el número de filas de datos.
    def rowCount(self, indice):
        return len(self.datos)

    # Devuelve el número de columnas.
    def columnCount(self, indice):
        return len(self.cabeceras)

    # Devuelve el texto o el estado del checkbox de cada celda.
    def data(self, indice, rol):

        if not indice.isValid():
            return None

        fila = indice.row()
        columna = indice.column()

        dato = self.datos[fila][columna]

        # Muestra el contenido como texto, excepto en la columna checkbox.
        if rol == Qt.ItemDataRole.DisplayRole:

            if columna != 2:
                return dato

        # Devuelve el estado del checkbox de la tercera columna.
        if rol == Qt.ItemDataRole.CheckStateRole:

            if columna == 2:

                if dato:
                    return Qt.CheckState.Checked

                return Qt.CheckState.Unchecked

        return None

    # Guarda los cambios realizados al editar texto o marcar un checkbox.
    def setData(self, indice, valor, rol):

        if not indice.isValid():
            return False

        fila = indice.row()
        columna = indice.column()

        # Guarda el texto nuevo en la primera columna.
        if rol == Qt.ItemDataRole.EditRole:

            if columna == 0:

                self.datos[fila][columna] = valor

                self.dataChanged.emit(indice, indice)

                return True

         # Guarda el nuevo estado del checkbox.
        if rol == Qt.ItemDataRole.CheckStateRole:
  
            if columna == 2:
    
                # Comprueba si el checkbox está marcado.
                marcado = (
                    valor == Qt.CheckState.Checked
                    or valor == Qt.CheckState.Checked.value
                )
    
                self.datos[fila][columna] = marcado
    
                # Notifica a Qt que ha cambiado toda la fila.
                primera_celda = self.index(fila, 0)
                ultima_celda = self.index(fila, self.columnCount(indice) - 1)
    
                self.dataChanged.emit(
                    primera_celda,
                    ultima_celda,
                    [
                        Qt.ItemDataRole.CheckStateRole,
                        Qt.ItemDataRole.BackgroundRole
                    ]
                )
    
                return True

        return False

    # Define qué acciones están permitidas en cada celda.
    def flags(self, indice):

        if not indice.isValid():
            return Qt.ItemFlag.NoItemFlags

        # Todas las celdas se pueden activar y seleccionar.
        condiciones = (
            Qt.ItemFlag.ItemIsEnabled |
            Qt.ItemFlag.ItemIsSelectable
        )

        # La primera columna se puede editar.
        if indice.column() == 0:
            condiciones |= Qt.ItemFlag.ItemIsEditable

        # La tercera columna permite marcar y desmarcar el checkbox.
        if indice.column() == 2:
            condiciones |= Qt.ItemFlag.ItemIsUserCheckable

        # La segunda columna no recibe ItemIsEditable, por eso no se edita.
        return condiciones

    # Devuelve los nombres de las columnas.
    def headerData(self, seccion, orientacion, rol):

        if rol == Qt.ItemDataRole.DisplayRole:

            if orientacion == Qt.Orientation.Horizontal:
                return self.cabeceras[seccion]

        return None
```

En `principal.py`, cambia los datos por estos. La vista no necesita más
modificaciones:

``` python
cabeceras = ["Nombre", "DNI", "Activo"]

datos = [
    ["Ana", "1111A", True],
    ["Paco", "2222B", False],
    ["Maria", "3333C", True]
]
```

### ¿Qué controla cada función?

-   `flags()`: decide si una celda se puede editar o marcar.
-   `data()`: indica qué texto o estado debe mostrar.
-   `setData()`: guarda el nuevo texto o el nuevo estado del checkbox.

------------------------------------------------------------------------

## 3. Cambiar el color de la fila según el checkbox

Objetivo:

-   Checkbox marcado: fila verde.
-   Checkbox desmarcado: fila roja.

### Cambio en `modelo.py`

Añade este import al principio:

``` python
from PyQt6.QtGui import QColor
```

Dentro de `data()`, añade este bloque después del bloque de
`CheckStateRole` y antes de `return None`:

``` python
        # Colorea todas las celdas de la fila según el checkbox.
        if rol == Qt.ItemDataRole.BackgroundRole:

          if self.datos[fila][2]:
              return QColor("lightgreen")

        return QColor("red")
```

Ahora modifica el `dataChanged.emit()` que está dentro del bloque del
checkbox en `setData()`.

Sustituye:

``` python
self.dataChanged.emit(indice, indice)
```

Por:

``` python
# Avisa a la vista de que han cambiado el checkbox y el color.
self.dataChanged.emit(
    indice,
    indice,
    [
        Qt.ItemDataRole.CheckStateRole,
        Qt.ItemDataRole.BackgroundRole
    ]
)
```

Así la vista vuelve a consultar el color cuando marcas o desmarcas el
checkbox.

No hay que modificar `principal.py`.

------------------------------------------------------------------------

## 4. Añadir un botón para borrar cada fila

Queremos añadir una cuarta columna llamada `Borrar`, con un botón en
cada fila.

Para colocar botones dentro de las celdas utilizaremos
`setIndexWidget()` desde la vista.

### 4.1. Cambios en `modelo.py`

Primero, importa `QModelIndex`:

``` python
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
```

Añade un método a `ModeloTabla`:

``` python
    # Elimina la fila indicada y avisa a la vista del cambio.
    def eliminar_fila(self, fila):

        self.beginRemoveRows(
            QModelIndex(),
            fila,
            fila
        )

        del self.datos[fila]

        self.endRemoveRows()
```

La función `beginRemoveRows()` avisa de que se va a eliminar una fila.
`endRemoveRows()` avisa de que la eliminación ha terminado.

Cambia los encabezados en `principal.py`:

``` python
cabeceras = ["Nombre", "DNI", "Activo", "Borrar"]
```

La lista `datos` sigue teniendo solamente tres valores por fila. La
cuarta columna es un espacio reservado para los botones.

En `data()`, conserva esta comprobación antes de intentar leer el dato:

``` python
fila = indice.row()
columna = indice.column()

# La cuarta columna está reservada para el botón, no tiene datos.
if columna == 3:
    return None

dato = self.datos[fila][columna]
```

En `flags()`, añade una comprobación para que la columna del botón no
tenga interacción de celda:

``` python
    # Define qué acciones están permitidas en cada celda.
    def flags(self, indice):

        if not indice.isValid():
            return Qt.ItemFlag.NoItemFlags

        # La columna de botones no necesita flags de edición o selección.
        if indice.column() == 3:
            return Qt.ItemFlag.NoItemFlags

        condiciones = (
            Qt.ItemFlag.ItemIsEnabled |
            Qt.ItemFlag.ItemIsSelectable
        )

        if indice.column() == 0:
            condiciones |= Qt.ItemFlag.ItemIsEditable

        if indice.column() == 2:
            condiciones |= Qt.ItemFlag.ItemIsUserCheckable

        return condiciones
```

### 4.2. Cambios en `principal.py`

Añade `QPushButton` a los imports:

``` python
from PyQt6.QtWidgets import QPushButton
```

Después de crear la tabla y asignarle el modelo, conecta las señales:

``` python
# Crea los botones de borrado para todas las filas.
self.actualizar_botones()

# Vuelve a colocar los botones cuando se inserten o eliminen filas.
self.modelo.rowsRemoved.connect(self.actualizar_botones)
self.modelo.rowsInserted.connect(self.actualizar_botones)
```

Añade este método dentro de `VentanaPrincipal`:

``` python
    # Crea un botón Borrar en la cuarta columna de cada fila.
    def actualizar_botones(self):

        for fila in range(self.modelo.rowCount(None)):

            boton = QPushButton("Borrar")

            # f=fila conserva el número de fila correspondiente a este botón.
            boton.clicked.connect(
                lambda checked=False, f=fila:
                    self.modelo.eliminar_fila(f)
            )

            indice = self.modelo.index(fila, 3)

            # Coloca el botón dentro de la celda correspondiente.
            self.tabla.setIndexWidget(indice, boton)
```

La variable `f=fila` es importante: permite que cada botón recuerde qué
fila debe eliminar.

------------------------------------------------------------------------

## 5. Añadir un formulario debajo de la tabla

Por último, añadiremos un formulario para introducir nuevos registros.

El formulario tendrá:

-   Un campo para el nombre.
-   Un campo para el DNI.
-   Un checkbox para indicar si está activo.
-   Un botón para añadir la fila.

### 5.1. Añadir una función al modelo

En `modelo.py`, añade este método a `ModeloTabla`:

``` python
    # Inserta una nueva fila al final de la lista de datos.
    def insertar_fila(self, datos):

        fila = self.rowCount(None)

        self.beginInsertRows(
            QModelIndex(),
            fila,
            fila
        )

        self.datos.append(datos)

        self.endInsertRows()
```

La función recibe una lista con los valores de la nueva fila.

Por ejemplo:

``` python
self.modelo.insertar_fila(["Carlos", "5555E", True])
```

No es necesario actualizar manualmente el número de filas: `rowCount()`
lo calcula a partir de `self.datos`.

### 5.2. Vista completa con tabla, botones y formulario

Sustituye `principal.py` por este archivo completo:

``` python
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableView,
    QPushButton,
    QLineEdit,
    QCheckBox,
    QLabel
)

from modelo import ModeloTabla


class VentanaPrincipal(QMainWindow):

    # Crea la ventana, el modelo, la tabla y el formulario.
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi tabla PyQt6")
        self.resize(750, 400)

        # Encabezados: la cuarta columna se reserva para los botones.
        cabeceras = ["Nombre", "DNI", "Activo", "Borrar"]

        # Cada fila de datos contiene tres valores.
        datos = [
            ["Ana", "1111A", True],
            ["Paco", "2222B", False],
            ["Maria", "3333C", True]
        ]

        # Creamos el modelo.
        self.modelo = ModeloTabla(cabeceras, datos)

        # Creamos la tabla y conectamos el modelo.
        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)

        # Creamos los botones iniciales.
        self.actualizar_botones()

        # Actualizamos los botones cuando cambie el número de filas.
        self.modelo.rowsRemoved.connect(self.actualizar_botones)
        self.modelo.rowsInserted.connect(self.actualizar_botones)

        # Creamos los campos del formulario.
        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Nombre")

        self.dni = QLineEdit()
        self.dni.setPlaceholderText("DNI")

        self.activo = QCheckBox("Activo")

        # Creamos el botón que añadirá el nuevo registro.
        self.botonAnadir = QPushButton("Añadir fila")
        self.botonAnadir.clicked.connect(self.anadir_fila)

        # Colocamos los campos del formulario en horizontal.
        formulario = QHBoxLayout()

        formulario.addWidget(QLabel("Nombre:"))
        formulario.addWidget(self.nombre)

        formulario.addWidget(QLabel("DNI:"))
        formulario.addWidget(self.dni)

        formulario.addWidget(self.activo)
        formulario.addWidget(self.botonAnadir)

        # Colocamos la tabla encima del formulario.
        caja = QVBoxLayout()

        caja.addWidget(self.tabla)
        caja.addLayout(formulario)

        # Creamos el contenedor central.
        contenedor = QWidget()
        contenedor.setLayout(caja)

        self.setCentralWidget(contenedor)

    # Crea un botón Borrar en la cuarta columna de cada fila.
    def actualizar_botones(self):

        for fila in range(self.modelo.rowCount(None)):

            boton = QPushButton("Borrar")

            # f=fila conserva la fila asociada a cada botón.
            boton.clicked.connect(
                lambda checked=False, f=fila:
                    self.modelo.eliminar_fila(f)
            )

            indice = self.modelo.index(fila, 3)

            # Coloca el botón dentro de la celda.
            self.tabla.setIndexWidget(indice, boton)

    # Recoge los valores del formulario y los añade al modelo.
    def anadir_fila(self):

        nombre = self.nombre.text().strip()
        dni = self.dni.text().strip()
        activo = self.activo.isChecked()

        # No añade la fila si falta el nombre o el DNI.
        if nombre == "" or dni == "":
            return

        # Inserta los datos en el modelo.
        self.modelo.insertar_fila([
            nombre,
            dni,
            activo
        ])

        # Limpia los campos para introducir otro registro.
        self.nombre.clear()
        self.dni.clear()
        self.activo.setChecked(False)


# Punto de entrada del programa.
if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
```

------------------------------------------------------------------------

# 6. Chuleta rápida de funciones

  Quiero...                       Función o propiedad
  ------------------------------- -----------------------------------------
  Mostrar el contenido            `data()`
  Mostrar encabezados             `headerData()`
  Permitir editar una celda       `ItemIsEditable`
  Guardar cambios de texto        `setData()` + `EditRole`
  Mostrar un checkbox             `CheckStateRole`
  Permitir marcar un checkbox     `ItemIsUserCheckable`
  Colorear una celda o fila       `BackgroundRole`
  Avisar de cambios en celdas     `dataChanged.emit()`
  Eliminar una fila               `beginRemoveRows()` / `endRemoveRows()`
  Insertar una fila               `beginInsertRows()` / `endInsertRows()`
  Colocar un botón en una celda   `setIndexWidget()`

## 7. Idea fundamental para recordar

Las tres funciones más importantes para controlar las celdas son:

-   **`data()`**: qué muestra la celda.
-   **`setData()`**: cómo se guarda lo que cambia el usuario.
-   **`flags()`**: qué puede hacer el usuario en esa celda.

Y para cambiar la estructura de la tabla (añadir o quitar filas), hay
que avisar al modelo mediante `begin...` y `end...`.

Con esta base puedes reutilizar el modelo en otros proyectos cambiando
los encabezados, los datos y las condiciones de cada columna.

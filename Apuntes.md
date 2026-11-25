# Apuntes de PyQt6 --- Guía de estudio

------------------------------------------------------------------------

# 1. Cómo empezar un proyecto con PyQt6

## 1.1. Importar las herramientas

``` python
import sys
from PyQt6.QtWidgets import *
```

## 1.2. Crear una clase para la ventana

``` python
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")
        self.setMinimumSize(400, 600)
        self.setMaximumSize(600, 800)
```

## 1.3. Crear un widget central para los layouts

Cuando se utiliza `QMainWindow`, normalmente los layouts se colocan
dentro de un `QWidget` central. No se asigna directamente un layout a
`QMainWindow`.

``` python
central = QWidget()
self.setCentralWidget(central)

grid = QGridLayout()
central.setLayout(grid)
```

-   `QWidget()` crea un widget que servirá como zona central.
-   `setCentralWidget(central)` coloca ese widget en el centro de la
    ventana.
-   `QGridLayout()` crea un layout de cuadrícula.
-   `central.setLayout(grid)` asigna el layout al widget central.

Más adelante veremos que también podemos usar `QVBoxLayout` o
`QHBoxLayout`.

## 1.4. Mostrar la ventana y ejecutar la aplicación

Al final del archivo se suele escribir:

``` python
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())
```

Explicación:

-   `if __name__ == "__main__":` comprueba que el archivo se está
    ejecutando directamente.
-   `QApplication(sys.argv)` crea la aplicación PyQt6. Normalmente se
    crea una sola vez.
-   `ventana = Ventana()` crea un objeto de nuestra clase.
-   `ventana.show()` muestra la ventana.
-   `app.exec()` inicia el bucle de eventos, que permite que la ventana
    responda a clics y otras acciones.
-   `sys.exit(...)` termina el programa correctamente cuando se cierra
    la aplicación.

## 1.5. Estructura básica completa

Este es un punto de partida que puedes reutilizar:

``` python
import sys
from PyQt6.QtWidgets import *


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")
        self.setMinimumSize(400, 600)
        self.setMaximumSize(600, 800)
        central = QWidget()
        self.setCentralWidget(central)

        grid = QGridLayout()
        central.setLayout(grid)

        # Aquí añadiremos los widgets al layout.

    def...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
```

**Importante:** dentro de los métodos de la clase, los widgets y
atributos que quieras utilizar desde otras funciones suelen guardarse
con `self`, por ejemplo `self.nombre = QLineEdit()`.

------------------------------------------------------------------------

# 2. Widgets y sus métodos importantes

Un *widget* es un elemento de la interfaz: una etiqueta, un campo de
texto, un botón, una lista desplegable, etc.

## 2.1. QLabel --- Mostrar texto

Sirve para mostrar texto en la ventana.

``` python
etiqueta = QLabel("Hola")
```

Métodos importantes:

  Método                      Para qué sirve
  --------------------------- --------------------------------------
  `QLabel("Texto")`           Crear una etiqueta con texto inicial
  `.text()`                   Obtener el texto actual
  `.setText("Nuevo texto")`   Cambiar el texto

Ejemplo:

``` python
etiqueta = QLabel("Texto inicial")
etiqueta.setText("Texto nuevo")
```

## 2.2. QLineEdit --- Escribir una línea de texto

Sirve para que el usuario escriba una línea, por ejemplo un nombre o un
correo.

``` python
nombre = QLineEdit()
```

Métodos importantes:
 -------------------------------------------- -----------------------------------
  `QLineEdit()`                                Crear un campo de texto

  `.text()`                                    Obtener lo que ha escrito el
                                               usuario

  `.setText("Ana")`                            Escribir o sustituir el contenido

  `.clear()`                                   Borrar el contenido

  `.setPlaceholderText("Escribe tu nombre")`   Mostrar una indicación cuando está
                                               vacío
  --------------------------------------------------------------------------------

Ejemplo:

``` python
nombre = QLineEdit()
nombre.setPlaceholderText("Escribe tu nombre")

texto = nombre.text()
nombre.clear()
```

## 2.3. QTextEdit --- Escribir varias líneas

Sirve para introducir textos más largos, como una descripción o
comentarios.

``` python
descripcion = QTextEdit()
```

Métodos importantes:

  Método                     Para qué sirve
  -------------------------- -------------------------------------
  `QTextEdit()`              Crear un cuadro de texto multilínea<br>
  `.toPlainText()`           Obtener el texto escrito<br>
  `.setPlainText("Texto")`   Establecer el contenido<br>
  `.clear()`                 Borrar el contenido<br>

Ejemplo:

``` python
descripcion = QTextEdit()
texto = descripcion.toPlainText()
descripcion.setPlainText("Una descripción")
descripcion.clear()
```

**Ojo:** `QTextEdit` utiliza `.toPlainText()` para obtener el contenido,
no `.text()`.

## 2.4. QPushButton --- Crear un botón

Sirve para que el usuario pueda ejecutar una acción al pulsarlo.

``` python
boton = QPushButton("Enviar")
//boton.clicked.connect(self.metodo())
```

La conexión con una función se explica en el apartado 4.

## 2.5. QComboBox --- Lista desplegable

Permite seleccionar una opción de una lista.

``` python
ciudad = QComboBox()
ciudad.addItems(["Vigo", "Madrid", "Sevilla"])
```

Métodos importantes:
  ----------------------- ---------------------------------------------
  `.addItem("Vigo")`      Añadir una opción<br>
  `.addItems([...])`      Añadir varias opciones<br>
  `.currentText()`        Obtener el texto de la opción seleccionada<br>
  `.currentIndex()`       Obtener el índice de la opción seleccionada<br>
  `.setCurrentIndex(1)`   Seleccionar la opción con índice 1<br>
  `.clear()`              Eliminar todas las opciones<br>

Los índices empiezan en **0**. En el ejemplo, Vigo tiene índice 0,
Madrid índice 1 y Sevilla índice 2.

Ejemplo:

``` python
ciudad = QComboBox()
ciudad.addItems(["Vigo", "Madrid", "Sevilla"])

seleccion = ciudad.currentText()
indice = ciudad.currentIndex()
```

## 2.6. QRadioButton --- Elegir una opción

Sirve para elegir una opción entre varias. Por ejemplo, Sí o No.

``` python
radio_si = QRadioButton("Sí")
radio_no = QRadioButton("No")
```

Métodos importantes:

  Método                    Para qué sirve
  ------------------------- --------------------------------
  `QRadioButton("Texto")`   Crear un botón de opción<br>
  `.isChecked()`            Comprobar si está seleccionado<br>
  `.setChecked(True)`       Marcarlo<br>
  `.setChecked(False)`      Desmarcarlo<br>
  `.text()`                 Obtener el texto que muestra<br>

Ejemplo:

``` python
if radio_si.isChecked():
    respuesta = "Sí"
elif radio_no.isChecked():
    respuesta = "No"
else:
    respuesta = "No seleccionado"
```

Cuando varios `QRadioButton` deben ser opciones excluyentes, normalmente
se colocan dentro del mismo grupo o contenedor adecuado. Así, al
seleccionar uno, se desmarca el otro.

## 2.7. QCheckBox --- Casilla de selección

Permite marcar o desmarcar una casilla. A diferencia de un grupo de
opciones de radio, se pueden marcar varias casillas independientes.

``` python
acepto = QCheckBox("Acepto las condiciones")
```

Métodos importantes:

  Método                 Para qué sirve
  ---------------------- --------------------------------
  `.isChecked()`         Comprobar si está marcada<br>
  `.setChecked(True)`    Marcar la casilla<br>
  `.setChecked(False)`   Desmarcarla<br>
  `.text()`              Obtener el texto de la casilla<br>

Ejemplo:

``` python
if acepto.isChecked():
    print("Aceptado")
else:
    print("No aceptado")
```

## 2.8. QSpinBox y QDoubleSpinBox --- Introducir números

`QSpinBox` permite seleccionar números enteros. `QDoubleSpinBox` permite
números decimales.

``` python
edad = QSpinBox()
precio = QDoubleSpinBox()
```

Métodos habituales:

  Método                        Para qué sirve
  ----------------------------- ---------------------
  `.value()`                    Obtener el número<br>
  `.setValue(18)`               Establecer el valor<br>
  `.setRange(minimo, maximo)`   Establecer límites<br>

Ejemplo:

``` python
edad = QSpinBox()
edad.setRange(0, 120)
edad.setValue(18)

numero = edad.value()
```

## 2.9. Tabla rápida: cómo obtener el contenido

Esta tabla es especialmente útil para memorizar:

  Widget             Método para obtener el contenido
  ------------------ ----------------------------------
  `QLabel`           `.text()`<br>
  `QLineEdit`        `.text()`<br>
  `QTextEdit`        `.toPlainText()`<br>
  `QComboBox`        `.currentText()`<br>
  `QRadioButton`     `.isChecked()`<br>
  `QCheckBox`        `.isChecked()`<br>
  `QSpinBox`         `.value()`<br>
  `QDoubleSpinBox`   `.value()`<br>

------------------------------------------------------------------------

# 3. Disposición de los elementos: Layouts

Los *layouts* organizan los widgets dentro de una ventana o de otro
contenedor.

Los tres layouts básicos son:

-   `QVBoxLayout`: coloca los elementos verticalmente.
-   `QHBoxLayout`: coloca los elementos horizontalmente.
-   `QGridLayout`: coloca los elementos en filas y columnas.

## 3.1. QVBoxLayout --- Disposición vertical

Los elementos se colocan uno debajo de otro.

``` python
layout = QVBoxLayout()

layout.addWidget(QLabel("Nombre"))
layout.addWidget(QLineEdit())
layout.addWidget(QPushButton("Enviar"))
```

Representación aproximada:

``` text
Nombre
[ campo de texto ]
[     Enviar     ]
```

## 3.2. QHBoxLayout --- Disposición horizontal

Los elementos se colocan uno al lado del otro.

``` python
layout = QHBoxLayout()

layout.addWidget(QLabel("Nombre"))
layout.addWidget(QLineEdit())
layout.addWidget(QPushButton("Enviar"))
```

Representación aproximada:

``` text
Nombre   [ campo de texto ]   [ Enviar ]
```

## 3.3. QGridLayout --- Filas y columnas

Organiza los widgets en una cuadrícula. Es especialmente útil para
formularios.

``` python
grid = QGridLayout()

grid.addWidget(QLabel("Nombre:"), 0, 0)
grid.addWidget(QLineEdit(), 0, 1)

grid.addWidget(QLabel("Edad:"), 1, 0)
grid.addWidget(QLineEdit(), 1, 1)
```

La forma general es:

``` python
grid.addWidget(widget, fila, columna)
```

Las filas y columnas empiezan en **0**:

``` text
             Columna 0       Columna 1
Fila 0       Nombre:         [ campo ]
Fila 1       Edad:           [ campo ]
```

### Ocupar varias filas o columnas

También se puede indicar cuánto espacio debe ocupar un widget:

``` python
grid.addWidget(widget, fila, columna, filas, columnas)
```

Ejemplos:

``` python
grid.addWidget(widget, 0, 0, 1, 2)
```

Ocupa 1 fila y 2 columnas.

``` python
grid.addWidget(widget, 0, 0, 2, 1)
```

Ocupa 2 filas y 1 columna.

``` python
grid.addWidget(widget, 0, 0, 2, 2)
```

Ocupa 2 filas y 2 columnas.

## 3.4. Diferencia entre addWidget() y addLayout()

Esta diferencia es importante:

-   `addWidget()` añade un widget, como un `QLabel`, `QLineEdit` o
    `QPushButton`.
-   `addLayout()` añade un layout dentro de otro layout.

Ejemplo:

``` python
grid = QGridLayout()
fila = QHBoxLayout()

fila.addWidget(QLabel("Nombre"))
fila.addWidget(QLineEdit())

grid.addLayout(fila, 0, 0)
```

Aquí se crea un layout horizontal y se introduce dentro de la primera
posición del Grid.

## 3.5. Asignar un layout

Si utilizas un `QWidget` normal:

``` python
ventana = QWidget()
grid = QGridLayout()

ventana.setLayout(grid)
```

Si utilizas `QMainWindow`, recuerda crear un widget central:

``` python
central = QWidget()
self.setCentralWidget(central)

grid = QGridLayout()
central.setLayout(grid)
```

------------------------------------------------------------------------

# 4. Botones, funciones y señales

Un botón puede ejecutar una función cuando el usuario hace clic en él.

## 4.1. Crear un botón

``` python
boton = QPushButton("Enviar")
```

## 4.2. Crear una función

Una función contiene las instrucciones que queremos ejecutar.

``` python
def saludar():
    print("Hola")
```

## 4.3. Conectar el botón con la función

``` python
boton.clicked.connect(saludar)
```

Esto significa: cuando se haga clic en el botón, se ejecutará la función
`saludar`.

**Importante:** al conectar la función se escribe su nombre sin
paréntesis:

``` python
boton.clicked.connect(saludar)
```

No así:

``` python
boton.clicked.connect(saludar())
```

Sin paréntesis, se pasa la función para que se ejecute al producirse el
clic. Con paréntesis, se estaría llamando a la función inmediatamente.

## 4.4. Recoger texto de un QLineEdit y mostrarlo en un QLabel

``` python
nombre = QLineEdit()
resultado = QLabel()
boton = QPushButton("Mostrar")


def mostrar():
    texto = nombre.text()
    resultado.setText(texto)


boton.clicked.connect(mostrar)
```

Paso a paso:

1.  El usuario escribe en `nombre`.
2.  Pulsa el botón.
3.  Se ejecuta `mostrar()`.
4.  `nombre.text()` obtiene lo escrito.
5.  `resultado.setText(texto)` muestra ese contenido en el QLabel.

## 4.5. Ejemplo con varios tipos de widgets

Este ejemplo recoge un dato de cada elemento y muestra el resultado en
una etiqueta.

``` python
nombre = QLineEdit()

descripcion = QTextEdit()

ciudad = QComboBox()
ciudad.addItems(["Vigo", "Madrid", "Sevilla"])

radio_si = QRadioButton("Sí")
radio_no = QRadioButton("No")

boton = QPushButton("Mostrar datos")
resultado = QLabel("Aquí aparecerán los datos")


def mostrar_datos():
    n = nombre.text()
    d = descripcion.toPlainText()
    c = ciudad.currentText()

    if radio_si.isChecked():
        estudio = "Sí"
    elif radio_no.isChecked():
        estudio = "No"
    else:
        estudio = "No seleccionado"

    resultado.setText(
        f"Nombre: {n}\n"
        f"Descripción: {d}\n"
        f"Ciudad: {c}\n"
        f"¿Estudias?: {estudio}"
    )


boton.clicked.connect(mostrar_datos)
```

Observa los métodos:

-   `nombre.text()` obtiene el contenido del QLineEdit.
-   `descripcion.toPlainText()` obtiene el contenido del QTextEdit.
-   `ciudad.currentText()` obtiene la opción seleccionada.
-   `radio_si.isChecked()` comprueba si el primer radio está marcado.
-   `resultado.setText(...)` cambia el texto del QLabel.

## 4.6. Limpiar los campos con un botón

El método `.clear()` borra el contenido de muchos widgets de entrada.

``` python
def limpiar():
    nombre.clear()
    descripcion.clear()
```

Conectar el botón:

``` python
boton_limpiar.clicked.connect(limpiar)
```

Si también quieres restablecer un `QComboBox` a su primera opción:

``` python
ciudad.setCurrentIndex(0)
```

Para desmarcar opciones:

``` python
radio_si.setChecked(False)
radio_no.setChecked(False)
```

En un grupo de radio, normalmente puedes seleccionar otra opción o
gestionar la selección desde el grupo. No siempre es posible dejar todos
los botones de un grupo exclusivo desmarcados simplemente desmarcando
uno.

## 4.7. Qué son las señales (CurrentIndexChanged)

Una señal es un aviso que emite un widget cuando sucede algo.

Ejemplos:

  Señal                   Cuándo se produce
  ----------------------- -----------------------------------------------
  `clicked`               Al hacer clic en un botón
  `currentIndexChanged`   Al cambiar la selección de un QComboBox
  `textChanged`           Cuando cambia el texto de un campo compatible

Se conectan mediante `.connect()`:

``` python
boton.clicked.connect(mi_funcion)
combo.currentIndexChanged.connect(mi_funcion)
```

La señal `currentIndexChanged` de un QComboBox puede conectarse
directamente a un método que reciba el índice, como veremos con
`QStackedLayout`.

------------------------------------------------------------------------

# 5. Cambiar vistas con QStackedLayout

`QStackedLayout` permite tener varias páginas o vistas en el mismo
espacio y mostrar una cada vez.

Por ejemplo, un `QComboBox` puede permitir elegir entre las páginas
Nombre, Edad y Ciudad.

## 5.1. Crear el QStackedLayout

``` python
stack = QStackedLayout()
```

Este layout será el encargado de contener las diferentes páginas.

## 5.2. Crear las páginas

Cada página será un `QWidget`.

``` python
pagina1 = QWidget()
pagina2 = QWidget()
pagina3 = QWidget()
```

Cada página puede tener sus propios widgets y su propio layout.

## 5.3. Crear un layout para cada página

Por ejemplo, la primera página tendrá un campo para el nombre:

``` python
grid1 = QGridLayout()

nombre = QLineEdit()

grid1.addWidget(QLabel("Nombre:"), 0, 0)
grid1.addWidget(nombre, 0, 1)

pagina1.setLayout(grid1)
```

La segunda página tendrá un campo para la edad:

``` python
grid2 = QGridLayout()

edad = QLineEdit()

grid2.addWidget(QLabel("Edad:"), 0, 0)
grid2.addWidget(edad, 0, 1)

pagina2.setLayout(grid2)
```

La tercera página tendrá un campo para la ciudad:

``` python
grid3 = QGridLayout()

ciudad = QLineEdit()

grid3.addWidget(QLabel("Ciudad:"), 0, 0)
grid3.addWidget(ciudad, 0, 1)

pagina3.setLayout(grid3)
```

## 5.4. Añadir las páginas al Stack

``` python
stack.addWidget(pagina1)
stack.addWidget(pagina2)
stack.addWidget(pagina3)
```

El orden determina el índice de cada página:

  Página        Índice
  ----------- --------
  `pagina1`          0
  `pagina2`          1
  `pagina3`          2

La primera página, índice 0, se muestra inicialmente.

## 5.5. Cambiar de página manualmente

Puedes indicar qué página quieres mostrar:

``` python
stack.setCurrentIndex(1)
```

Esto muestra la segunda página, porque los índices empiezan en 0.

## 5.6. Crear un QComboBox para elegir la página

``` python
opciones = QComboBox()
opciones.addItems(["Nombre", "Edad", "Ciudad"])
```

Las opciones tienen el mismo orden que las páginas del Stack:

-   Nombre → índice 0.
-   Edad → índice 1.
-   Ciudad → índice 2.

## 5.7. Conectar el QComboBox con el Stack

La conexión es:

``` python
opciones.currentIndexChanged.connect(stack.setCurrentIndex)
```

¿Qué ocurre?

1.  El usuario selecciona una opción del QComboBox.
2.  `currentIndexChanged` emite el índice de la opción seleccionada.
3.  `stack.setCurrentIndex` recibe ese índice.
4.  QStackedLayout muestra la página correspondiente.

No necesitamos crear una función intermedia porque la señal ya
proporciona el índice que necesita `setCurrentIndex()`.

## 5.8. Introducir el Stack en el layout principal

Si el layout principal es un Grid, se añade así:

``` python
grid.addWidget(opciones, 0, 0)
grid.addLayout(stack, 1, 0)
```

Recuerda:

-   El QComboBox es un widget, por eso usamos `addWidget()`.
-   El QStackedLayout es un layout, por eso usamos `addLayout()`.

------------------------------------------------------------------------

# 6. Ejemplo completo: formulario con QStackedLayout

Este ejemplo reúne lo anterior:

-   Una ventana `QMainWindow`.
-   Un `QGridLayout` principal.
-   Un `QComboBox` para cambiar de página.
-   Un `QStackedLayout` con tres páginas.
-   Un `QLineEdit` en cada página.
-   Un botón que muestra los datos en un `QLabel`.
-   Un botón que limpia los campos.

``` python
import sys
from PyQt6.QtWidgets import *


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario con páginas")
        self.setGeometry(100, 100, 500, 400)

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

        # PÁGINA 1: NOMBRE
        pagina1 = QWidget()
        grid1 = QGridLayout()

        self.nombre = QLineEdit()

        grid1.addWidget(QLabel("Nombre:"), 0, 0)
        grid1.addWidget(self.nombre, 0, 1)

        pagina1.setLayout(grid1)

        # PÁGINA 2: EDAD
        pagina2 = QWidget()
        grid2 = QGridLayout()

        self.edad = QLineEdit()

        grid2.addWidget(QLabel("Edad:"), 0, 0)
        grid2.addWidget(self.edad, 0, 1)

        pagina2.setLayout(grid2)

        # PÁGINA 3: CIUDAD
        pagina3 = QWidget()
        grid3 = QGridLayout()

        self.ciudad = QLineEdit()

        grid3.addWidget(QLabel("Ciudad:"), 0, 0)
        grid3.addWidget(self.ciudad, 0, 1)

        pagina3.setLayout(grid3)

        # AÑADIR PÁGINAS AL STACK
        stack.addWidget(pagina1)
        stack.addWidget(pagina2)
        stack.addWidget(pagina3)

        # BOTONES Y RESULTADO
        boton_mostrar = QPushButton("Mostrar datos")
        boton_limpiar = QPushButton("Limpiar")

        self.resultado = QLabel("Aquí aparecerán los datos")

        # AÑADIR ELEMENTOS AL GRID PRINCIPAL
        grid.addWidget(opciones, 0, 0)
        grid.addLayout(stack, 1, 0)
        grid.addWidget(boton_mostrar, 2, 0)
        grid.addWidget(boton_limpiar, 3, 0)
        grid.addWidget(self.resultado, 4, 0)

        # CONECTAR SELECTOR CON STACK
        opciones.currentIndexChanged.connect(stack.setCurrentIndex)

        # CONECTAR BOTONES CON FUNCIONES
        boton_mostrar.clicked.connect(self.mostrar_datos)
        boton_limpiar.clicked.connect(self.limpiar)


    def mostrar_datos(self):
        n = self.nombre.text()
        e = self.edad.text()
        c = self.ciudad.text()

        self.resultado.setText(
            f"Nombre: {n}\n"
            f"Edad: {e}\n"
            f"Ciudad: {c}"
        )


    def limpiar(self):
        self.nombre.clear()
        self.edad.clear()
        self.ciudad.clear()
        self.resultado.setText("Aquí aparecerán los datos")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())
```

**Fíjate en dos detalles importantes del ejemplo:**

1.  Los campos se crean con `self.nombre`, `self.edad` y `self.ciudad`
    para que los métodos `mostrar_datos()` y `limpiar()` puedan acceder
    a ellos.
2.  Aunque una página del Stack esté oculta, sus widgets siguen
    existiendo. Por eso el botón puede leer o limpiar los campos de las
    tres páginas.

# 7. Tablas
Esta guía amplía el ejemplo de clase. La tabla permitirá: - Mostrar
datos en filas y columnas. - Seleccionar filas completas. - Editar
nombre, DNI y género directamente en las celdas. - Marcar o desmarcar
una casilla en la columna de fallecimiento. - Añadir una persona con un
botón. - Eliminar la fila seleccionada con otro botón.

Los cambios se guardan en la lista del modelo; no se envían a ningún
servidor.

## 1. Modelo y vista

En este tipo de tabla separamos dos partes:

  -----------------------------------------------------------------------
  Elemento                            Función
  ----------------------------------- -----------------------------------
  `QAbstractTableModel`               Guarda los datos y define cómo se
                                      muestran y modifican.

  `QTableView`                        Es la tabla visual que ve el
                                      usuario.
  -----------------------------------------------------------------------

Se conectan así:

``` python
self.modelo = ModeloTabla(datos)
self.tabla = QTableView()
self.tabla.setModel(self.modelo)
```

`setModel()` conecta la vista con el modelo.

## 2. Datos de ejemplo

``` python
datos = [
    ["Nome", "DNI", "Xenero", "Falecimiento"],
    ["Ana Perez", "1111R", "Muller", False],
    ["Paco Porras", "2222T", "Home", True],
    ["Roque Vila", "3333H", "Home", False]
]
```

La primera lista contiene los encabezados. Las demás contienen los
registros. Por eso, al consultar una fila desde la vista, sumamos 1 para
acceder a la lista: `indice.row() + 1`.

## 3. Métodos básicos del modelo

### `__init__()`

``` python
def __init__(self, tabla):
    super().__init__()
    self.tabla = tabla
```

Recibe los datos y los guarda en el modelo.

### `rowCount()` y `columnCount()`

``` python
def rowCount(self, indice):
    return len(self.tabla) - 1

def columnCount(self, indice):
    return len(self.tabla[0])
```

-   `rowCount()` devuelve el número de registros, sin contar la fila de
    encabezados.
-   `columnCount()` devuelve el número de columnas.

### `data()`

Este método devuelve el contenido que se mostrará en una celda.

``` python
def data(self, indice, rol):

    if not indice.isValid():
        return None

    if rol == Qt.ItemDataRole.DisplayRole:
        dato = self.tabla[indice.row() + 1][indice.column()]

        if indice.column() == 3:
            return "✓" if dato else "✗"

        return str(dato)

    return None
```

-   `indice.row()` indica la fila solicitada.
-   `indice.column()` indica la columna.
-   `DisplayRole` pide el contenido que se verá en pantalla.
-   En la cuarta columna convertimos `True` y `False` en símbolos.

### `headerData()`

``` python
def headerData(self, seccion, orientacion, rol):

    if rol == Qt.ItemDataRole.DisplayRole:
        if orientacion == Qt.Orientation.Horizontal:
            return self.tabla[0][seccion]

    return None
```

Devuelve los nombres de las columnas. `seccion` indica qué encabezado se
está solicitando.

### `flags()`

Los flags indican qué se puede hacer en cada celda.

Para una tabla que solo permite seleccionar, pero no editar:

``` python
def flags(self, indice):
    return (
        Qt.ItemFlag.ItemIsEnabled |
        Qt.ItemFlag.ItemIsSelectable
    )
```

Para permitir editar las celdas de texto:

``` python
def flags(self, indice):

    if not indice.isValid():
        return Qt.ItemFlag.NoItemFlags

    return (
        Qt.ItemFlag.ItemIsEnabled |
        Qt.ItemFlag.ItemIsSelectable |
        Qt.ItemFlag.ItemIsEditable
    )
```

**Importante:** incluir `ItemIsEditable` permite iniciar la edición,
pero para guardar el cambio también necesitamos `setData()`.

## 4. Guardar cambios con `setData()`

Cuando el usuario edita una celda, `setData()` recibe el nuevo valor.
Hay que guardarlo en nuestra lista y avisar a la vista.

``` python
def setData(self, indice, valor, rol):

    if not indice.isValid():
        return False

    if rol == Qt.ItemDataRole.EditRole:

        fila = indice.row() + 1
        columna = indice.column()

        self.tabla[fila][columna] = str(valor)

        self.dataChanged.emit(indice, indice)

        return True

    return False
```

Pasos: 1. Comprobamos que el índice sea válido. 2. Comprobamos que el
rol sea `EditRole`. 3. Calculamos la posición real en la lista. 4.
Guardamos el nuevo valor. 5. Emitimos `dataChanged` para avisar a la
vista. 6. Devolvemos `True` para indicar que se ha aceptado.

## 5. Convertir una columna booleana en casillas

En lugar de mostrar una cruz o un visto, podemos permitir que el usuario
marque y desmarque una casilla.

En `data()` añadimos el tratamiento de `CheckStateRole`:

``` python
if indice.column() == 3:
    if rol == Qt.ItemDataRole.CheckStateRole:
        if dato:
            return Qt.CheckState.Checked
        else:
            return Qt.CheckState.Unchecked
```

En `flags()` indicamos que esa columna admite casillas:

``` python
def flags(self, indice):

    if not indice.isValid():
        return Qt.ItemFlag.NoItemFlags

    flags = (
        Qt.ItemFlag.ItemIsEnabled |
        Qt.ItemFlag.ItemIsSelectable
    )

    if indice.column() == 3:
        flags |= Qt.ItemFlag.ItemIsUserCheckable
    else:
        flags |= Qt.ItemFlag.ItemIsEditable

    return flags
```

Y en `setData()` guardamos el estado de la casilla:

``` python
if (
    indice.column() == 3 and
    rol == Qt.ItemDataRole.CheckStateRole
):
    self.tabla[fila][columna] = (
        valor == Qt.CheckState.Checked
    )

    self.dataChanged.emit(indice, indice)
    return True
```

Así la lista sigue guardando `True` o `False`, aunque la tabla muestre
una casilla.

## 6. Código completo de una tabla interactiva

El ejemplo reúne la edición de texto, las casillas, la selección de
filas y dos botones para añadir y eliminar registros.

``` python
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class ModeloTabla(QAbstractTableModel):

    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    def rowCount(self, indice):
        return len(self.tabla) - 1

    def columnCount(self, indice):
        return len(self.tabla[0])

    # Devuelve el contenido de las celdas
    def data(self, indice, rol):

        if not indice.isValid():
            return None

        fila = indice.row() + 1
        columna = indice.column()
        dato = self.tabla[fila][columna]

        # Columna booleana: mostrar una casilla
        if columna == 3 and rol == Qt.ItemDataRole.CheckStateRole:
            if dato:
                return Qt.CheckState.Checked
            return Qt.CheckState.Unchecked

        # Las otras columnas muestran texto
        if rol == Qt.ItemDataRole.DisplayRole:
            if columna == 3:
                return None
            return str(dato)

        return None

    # Encabezados horizontales
    def headerData(self, seccion, orientacion, rol):

        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.tabla[0][seccion]

        return None

    # Permisos de las celdas
    def flags(self, indice):

        if not indice.isValid():
            return Qt.ItemFlag.NoItemFlags

        flags = (
            Qt.ItemFlag.ItemIsEnabled |
            Qt.ItemFlag.ItemIsSelectable
        )

        if indice.column() == 3:
            flags |= Qt.ItemFlag.ItemIsUserCheckable
        else:
            flags |= Qt.ItemFlag.ItemIsEditable

        return flags

    # Guardar cambios de texto o de casillas
    def setData(self, indice, valor, rol):

        if not indice.isValid():
            return False

        fila = indice.row() + 1
        columna = indice.column()

        # Casilla marcada o desmarcada
        if (
            columna == 3 and
            rol == Qt.ItemDataRole.CheckStateRole
        ):
            self.tabla[fila][columna] = (
                valor == Qt.CheckState.Checked
            )

            self.dataChanged.emit(indice, indice)
            return True

        # Texto editado
        if (
            columna != 3 and
            rol == Qt.ItemDataRole.EditRole
        ):
            self.tabla[fila][columna] = str(valor)

            self.dataChanged.emit(indice, indice)
            return True

        return False

    # Añadir un registro
    def añadir_fila(self, persona):

        fila_nueva = len(self.tabla) - 1

        self.beginInsertRows(
            QModelIndex(),
            fila_nueva,
            fila_nueva
        )

        self.tabla.append(persona)

        self.endInsertRows()

    # Eliminar un registro
    def eliminar_fila(self, fila):

        if fila < 0 or fila >= self.rowCount(QModelIndex()):
            return

        self.beginRemoveRows(
            QModelIndex(),
            fila,
            fila
        )

        self.tabla.pop(fila + 1)

        self.endRemoveRows()


class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabla interactiva")
        self.setMinimumSize(650, 300)

        datos = [
            ["Nome", "DNI", "Xenero", "Falecimiento"],
            ["Ana Perez", "1111R", "Muller", False],
            ["Paco Porras", "2222T", "Home", True],
            ["Roque Vila", "3333H", "Home", False]
        ]

        # Crear modelo y vista
        self.modelo = ModeloTabla(datos)

        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)

        # Seleccionar filas completas
        self.tabla.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        # Layout principal
        grid = QGridLayout()
        grid.addWidget(self.tabla, 0, 0, 1, 2)

        # Botones
        boton_añadir = QPushButton("Añadir persona")
        boton_eliminar = QPushButton("Eliminar seleccionada")

        grid.addWidget(boton_añadir, 1, 0)
        grid.addWidget(boton_eliminar, 1, 1)

        boton_añadir.clicked.connect(self.añadir_persona)
        boton_eliminar.clicked.connect(self.eliminar_persona)

        contenedor = QWidget()
        contenedor.setLayout(grid)
        self.setCentralWidget(contenedor)

    def añadir_persona(self):

        persona = ["Nueva persona", "0000X", "Muller", False]

        self.modelo.añadir_fila(persona)

    def eliminar_persona(self):

        seleccion = self.tabla.selectionModel().selectedRows()

        if seleccion:
            fila = seleccion[0].row()
            self.modelo.eliminar_fila(fila)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())
```

## 7. Cómo funciona cada interacción

### Editar una celda

1.  Haz doble clic en una celda de `Nome`, `DNI` o `Xenero`.
2.  Escribe el nuevo valor.
3.  Pulsa Enter.
4.  `setData()` guarda el valor en la lista.
5.  `dataChanged.emit()` avisa a la tabla para que actualice la celda.

Para editar hacen falta dos cosas: - `ItemIsEditable` en `flags()`. -
`setData()` para guardar el cambio.

### Marcar o desmarcar una casilla

1.  Haz clic en una casilla de `Falecimiento`.
2.  Cambia su estado.
3.  `setData()` guarda `True` o `False`.

Para ello se utilizan: - `ItemIsUserCheckable` en `flags()`. -
`CheckStateRole` en `data()`. - `CheckStateRole` en `setData()`.

### Añadir una fila

El botón llama al método del modelo:

``` python
self.modelo.añadir_fila(persona)
```

El modelo utiliza:

``` python
self.beginInsertRows(...)
self.tabla.append(persona)
self.endInsertRows()
```

Estos métodos notifican a la vista que se ha insertado una fila, para
que se actualice correctamente.

### Eliminar una fila

Primero obtenemos la selección:

``` python
seleccion = self.tabla.selectionModel().selectedRows()

if seleccion:
    fila = seleccion[0].row()
```

Después pedimos al modelo que elimine esa fila:

``` python
self.modelo.eliminar_fila(fila)
```

Dentro del modelo se utiliza `pop(fila + 1)` porque la posición 0 de la
lista contiene los encabezados.

### Seleccionar filas completas

``` python
self.tabla.setSelectionBehavior(
    QAbstractItemView.SelectionBehavior.SelectRows
)
```

Así, al seleccionar una celda, se selecciona visualmente toda su fila.

------------------------------------------------------------------------

## 8. Chuleta para el examen

  -----------------------------------------------------------------------
  Método o flag                       Para qué sirve
  ----------------------------------- -----------------------------------
  `rowCount()`                        Número de filas.

  `columnCount()`                     Número de columnas.

  `data()`                            Devuelve el contenido de una celda.

  `headerData()`                      Devuelve los encabezados.

  `flags()`                           Define qué acciones se permiten en
                                      las celdas.

  `setData()`                         Guarda una modificación.

  `dataChanged.emit()`                Avisa de que una celda ha cambiado.

  `setModel()`                        Conecta modelo y vista.

  `ItemIsEnabled`                     Celda habilitada.

  `ItemIsSelectable`                  Celda seleccionable.

  `ItemIsEditable`                    Celda editable.

  `ItemIsUserCheckable`               Celda con casilla interactiva.

  `DisplayRole`                       Contenido que se muestra.

  `EditRole`                          Valor que se está editando.

  `CheckStateRole`                    Estado de una casilla.

  `selectedRows()`                    Obtiene las filas seleccionadas.

  `beginInsertRows()` /               Notifican que se añade una fila.
  `endInsertRows()`                   

  `beginRemoveRows()` /               Notifican que se elimina una fila.
  `endRemoveRows()`                   
  -----------------------------------------------------------------------

## 9. Orden recomendado para el examen

Si te piden una tabla como la de clase, constrúyela en este orden:

1.  Crear `ModeloTabla(QAbstractTableModel)`.
2.  Guardar los datos en `__init__()`.
3.  Programar `rowCount()` y `columnCount()`.
4.  Programar `data()`.
5.  Programar `headerData()`.
6.  Programar `flags()`.
7.  Si la tabla debe ser editable, añadir `setData()`.
8.  Crear la ventana y la lista de datos.
9.  Crear `QTableView()` y conectarlo con `setModel()`.
10. Colocar la tabla en un layout y asignar el widget central.

**Consejo de estudio:** domina primero la tabla básica de tu profesor.
Después añade las funciones interactivas una por una: selección,
edición, casillas, insertar y eliminar. Así podrás reconocer qué parte
del código necesitas según lo que te pidan.


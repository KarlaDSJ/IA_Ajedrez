## Inteligencia Artificial y Ajedrez por computadora
Profesor - Manuel Cristóbal López Michelone

### Instalación 
```
git clone https://github.com/KarlaDSJ/IA_Ajedrez.git
cd IA_Ajedrez
pip3 install -r requirements.txt
mysql -u root -p < DDL.sql
```

El usuario y contraseña utilizados para acceder a la base de datos pueden modificarse en el archivo src/common/config.py 

### Ejecución 
```
python3 main.py
```
___
<a id="tareas"></a>
### Tareas:
1. [**Programa generador de diagramas de ajedrez**](#tarea-1)
   
2. [**Calculadora de rating (Elo)**](#tarea-2)

3. [**Tarjetero electrónico de posiciones de ajedrez**](#tarea-3)+

4. [**PGN**](#tarea-4)

___

<a id="tarea-1"></a>
#### Tarea 1. Programa generador de diagramas de ajedrez <small>[[Top](#tareas)]</small>
<p align="center">
  <img src="https://github.com/KarlaDSJ/IA_Ajedrez/blob/Tarea_3/assets/images/chess.png" alt="vistaTarea1"/>
</p>

- Seleccionar la opción jugar
- Recrear jugada: despliega el menú con las piezas y 3 botones del lado superior derecho
    + Para poner una pieza en el tablero  dar click en:
      1. El botón de la mano
      2. La pieza deseada
      3. La casilla del tablero en donde se colocará la pieza
    + Para borrar una pieza dar click en:
      1. El botón de bote de basura
      1. La casilla en la cual deseamos quitar la pieza
    + Para cerrar el menú con las piezas dar click en el botón con un tache azul 
- Limpiar tablero: quita todas las piezas del tablero
- Guardar jugada: guardará el diagrama del tablero de ajedrez, en ese momento, en chess.pdf, el pdf se sobrescribe cada que seleccionamos esta opción
- Jugar: pondrá en el tablero las piezas en el lugar correspondiente para iniciar una partida
- Ver jugadas: (tarea 3) nos muestra las jugadas guardadas en la base de datos
- Icono de home: nos regresa a la página principal
- Los otros botones por el momento no hacen nada 

___
<a id="tarea-2"></a>
#### Tarea 2. Calculadora de rating (Elo) <small>[[Top](#tareas)]</small>
<p align="center">
  <img src="https://github.com/KarlaDSJ/IA_Ajedrez/blob/Tarea_3/assets/images/elo.png" alt="vistaTarea2"/>
</p>

- Seleccionar la opción calcular Elo
- LLenar los campos:
  + Rating actual 
  + Número de juegos
  + Resultado del torneo (juegos ganados)
  + k (constante asignada según el número de partidas y el rating)
-  Dar click en la flecha (parte superior derecha)
-  Ingresar el rating de los oponentes
-  Calcular: muestra en la parte superior derecha el nuevo rating, el promedio del rating de los jugadores y el desempeño
-  Limpiar: limpia las casillas donde se ingresa la información
-  Icono de home: nos regresa a la página principal

<a id="tarea-3"></a>
#### Tarea 3. Tarjetero electrónico de posiciones de ajedrez <small>[[Top](#tareas)]</small>
<p align="center">
  <img src="https://github.com/KarlaDSJ/IA_Ajedrez/blob/Tarea_3/assets/images/tarjetero.png" alt="vistaTarea3"/>
</p>

- La fechas de la parte inferior nos ayudan a movernos entre todas las tarjetas
- Al dar clik en ver o en agregar se muestra la pantalla del lado derecho, en ella se puede hacer:
   + Dar click en guardar: actualiza o crea la información de la tarjeta
   + Dar click en editar: despliega fichas para recrear una jugada en el tablero de ajedrez
   + Dar click en descargar: crea un pdf con la información de la ficha 
   + Dar click en  eliminar: borra la tarjeta de la base de datos 

<a id="tarea-4"></a>
#### Tarea 4. PGN <small>[[Top](#tareas)]</small>
<p align="center">
  <img src="https://github.com/KarlaDSJ/IA_Ajedrez/blob/Tarea_4/assets/images/PGN.png" alt="vistaTarea4"/>
</p>

- Flechas parte inferior - para moverse entre las tiradas de un juego
- Flechas parte superior - para moverse entre los juegos del archivo
- Botón de información - muestra la información de la partida

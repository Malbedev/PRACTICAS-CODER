
# Proyecto Final Coder House - Python
#### Comisión: 27615
#### Alumno: Johannes Pérez

## Nombre del Proyecto
Venta y Permuta de Instrumentos Musicales

## Versión
1.0

## Descripción del Proyecto
Página Web destinada a usuarios que deseen vender o permutar instrumentos musicales.

A fin de navegar por las secciones de la página web, el usuario será requerido iniciar sesión o registrarse en caso de no contar con usuario o contraseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio de la página web.

Los usuarios pueden realizar las siguientes accciones:
- Publicar instrumentos musicales
- Visualizar instrumentos musicales publicados, los cuales están distribuidos en las secciones "Guitarras", "Bajos", "Pedales", "Amplificadores", "Teclados" y "Otros"
- Comentar instrumentos musicales
- Editar el perfil de Usuario
- Cambiar la contraseña de Usuario
- Cerrar Sesión
- Login en caso de haber cerrado sesión

Nota: La opción de editar y eliminar instrumentos musicales solo le está permitido al autor de la publicación del instrumento.

## Tecnología Utilizada

##### Front-End
- HTML 5
- CSS 3
- Javascript ES6
- Bootstrap 5.2

##### Back-End
- Python 3.10.4
- Django 4.0

## Pruebas Realizadas

Ver archivo titulado "Pruebas Proyecto Python CH.xlsx" el cual se encuentra en el presente repositorio https://github.com/johannesgperez/ProyectoFinalMain.git

## Video Demostración

https://youtu.be/O3tgo0Txl9Q



PROYECTO FINAL - TERCERA ENTREGA -MAURO ALBERELLI

Es una web de reseñas de peliculas y series.La idea es Contar con curadores que pueden ser los usuarios tambien, con su respectivo login lo que flata desarrolar todavia.
ES UNA WEB EN CONSTRUCION, faltan funcionalidades.
Recomiendo istalar Pillow , crispy form y embed-video:
pipénv install pillow
pipenv install django-crispy-forms
pipenv install crispy-bootstrap5 
pipenv install django-embed-video


#Hasta el momento sae crearon los modelos pricipales (PELICULAS, SERIES Y DIRECTORES) y sus respectivos formularios.
El usuario puede cargar desde la pestaña Post , la informacion de los campos basado en el modelo. Que son Renderizados por vistas por funciones que ejecutan el request.POST de los datos desde Las siguientes URLS: series-formulario/
                                        peliculas-formulario/
                                        diectores-formulario/
En caso de ser valido, el resultado se puede ver reflejado en las pestañas respectivas del navbar de cada model(PELICULAS, SERIES Y DIRECTORES)AQUI SE AGREGAN TUS POST RESPECTIVAMENTE; que a su vez tienen el from html de busqueda.En este caso el request.GET de los 'titulos' de las peliculas y series.
Tambien la pagina de inicio Cuenta con un form de busqueda.(TODO ESTO PUEDE CAMBIAR, sigo desarrolando la experiencia del usuario)

LOS TEMPLATES tienen modularizado su html , Su Base y NAvbar por un lado y el resto heredando de ellos.







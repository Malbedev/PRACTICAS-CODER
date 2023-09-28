
# Proyecto Final Coder House - Python
#### Comisión: 43875
#### Alumno: Mauro Alberelli

## Nombre del Proyecto
Blog de reseñas de películas y series.

## Versión
1.0

## Descripción del Proyecto
Pagina Web destinada a usuarios que deseen recomendar a travez de sus reseñas material audiovisual, películas, series.

A fin de navegar por las secciones de la página web, el usuario será requerido iniciar sesión o registrarse en caso de no contar con usuario o contraseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al la pgina de informacion del proyecto, nuestro about.Donde cuenta con un link a un video tutorial,donde se explica cómo  generar el contenido.

Los usuarios pueden realizar las siguientes accciones:
- Rergistrarse
- Login 
- Publicar reseñas de películas, series y biografías de directores.
-La opción de editar y eliminar Posteos,  solo permitido al autor de la publicación.
- Visualizar la lista de los posteos /reseñas,biografías creado por cada usuario , los cuales están distribuidos en las secciones "Películas", "Series", "Directores".
- Comentar dichos posteos.
- Buscar por título en la barra de navegación o por género en cada sección.
- Editar el perfil de Usuario, personalizar sus datos-avatar-imagenes-bio , etc
- Cambiar la contraseña y el nombre de Usuario.
- Logout


## Tecnología Utilizada

##### Front-End
- HTML 5
- CSS 3
- Bootstrap 5.2

##### Back-End
- Python 3.10.4
- Django 4.0

## Pruebas Realizadas

Ver archivo Adjunto "Pruebas Proyecto Python-Django"

## Video Demostración





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







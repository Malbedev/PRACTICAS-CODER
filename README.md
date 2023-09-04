PROYECTO FINAL - TERCERA ENTREGA -MAURO ALBERELLI

Es una web de reseñas de peliculas y series.La idea es Contar con curadores que pueden ser los usuarios tambien, con su respectivo login lo que flata desarrolar todavia.
ES UNA WEB EN CONSTRUCION, faltan funcionalidades.

#Hasta el momento sae crearon los modelos pricipales (PELICULAS, SERIES Y DIRECTORES) y sus respectivos formularios.
El usuario puede cargar desde la pestaña Post , la informacion de los campos basado en el modelo. Que son Renderizados por vistas por funciones que ejecutan el request.POST de los datos desde Las siguientes URLS: series-formulario/
                                        peliculas-formulario/
                                        diectores-formulario/
En caso de ser valido, el resultado se puede ver reflejado en las pestañas respectivas del navbar de cada model(PELICULAS, SERIES Y DIRECTORES)AQUI SE AGREGAN TUS POST RESPECTIVAMENTE; que a su vez tienen el from html de busqueda.En este caso el request.GET de los 'titulos' de las peliculas y series.
Tambien la pagina de inicio Cuenta con un form de busqueda.(TODO ESTO PUEDE CAMBIAR, sigo desarrolando la experiencia del usuario)

LOS TEMPLATES tienen modularizado su html , Su Base y NAvbar por un lado y el resto heredando de ellos.







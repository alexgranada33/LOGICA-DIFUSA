# Función de Membresia Triangular

importar  numpy  como  np
importar  skfuzzy  como  sk
importar  matplotlib . pyplot  como  plt

# Se define un array x para el manejo del factor de calidad en un restaurante 

x  =  np . arange ( 0 , 11 , 1 )

# Se define un array para la función miembro de tipo triangular

calidad  =  sk . trimf ( x , [ 0 , 0 , 0 ])

# Se grafica la función de membresía 
plt . figura ()
plt . plot ( x , calidad , 'b' , linewidth  =  1.5 , label = 'Servicio' )

plt . título ( 'Calidad del Servicio en un Restaurante' )
plt . ylabel ( 'Membresía' )
plt . xlabel ( "Nivel de Servicio" )
plt . leyenda ( loc = 'centro derecho' , bbox_to_anchor = ( 1.25 , 0.5 ), ncol  =  1 , fancybox  =  True , shadow  =  True )

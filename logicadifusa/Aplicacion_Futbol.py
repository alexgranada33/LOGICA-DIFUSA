# Paquetes requeridos
importar  numpy  como  np
importar  skfuzzy  como  fuzz
importar  matplotlib . pyplot  como  plt
% matplotlib en  línea

# Definiendo los rangos de velocidad de 0 a 80
x  =  np . arango ( 30 , 80 , 0,1 )

# Definiedo las funciones miembro triangulares 
lento  =  fuzz . trimf ( x , [ 30 , 30 , 50 ])
medio  =  fuzz . trimf ( x , [ 30 , 50 , 70 ])
medio_rapido  =  fuzz . trimf ( x , [ 50 , 60 , 80 ])
rapido  =  pelusa . trimf ( x , [ 60 , 80 , 80 ])

# Dibujando las funciones de membresía 
plt . figura ()
plt . plot ( x , rapido , 'b' , linewidth  =  1.5 , label  =  'Rapido' )
plt . plot ( x , medio_rapido , 'k' , linewidth  =  1.5 , label  =  'Medio-Rapido' )
plt . plot ( x , medio , 'm' , linewidth  =  1.5 , label  =  'Medio' )
plt . plot ( x , lento , 'r' , linewidth  =  1.5 , label  =  'Lento' )
plt . título ( 'Penalti Difuso' )
plt . ylabel ( 'Membresía' )
plt . xlabel ( "Velocidad (Kilometros por hora)" )
plt . leyenda ( loc = 'centro derecho' , bbox_to_anchor = ( 1.25 , 0.5 ), ncol = 1 , fancybox = True , shadow = True )

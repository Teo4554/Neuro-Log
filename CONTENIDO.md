# CONTENIDO — escribí acá TODO tu texto

Reglas:
- No toques los títulos `##`. Son los marcadores que usa el script.
- Escribí debajo de cada título. Podés usar saltos de línea, `**negrita**` y enlaces `[texto](https://...)`.
- Si un bloque lo dejás vacío o con el corchete inicial, el script no lo reemplaza y queda el aviso pendiente.
- Guardá el archivo y ejecutá `python3 insertar_contenido.py`.

Cada módulo tiene 4 bloques, en el orden que pide la rúbrica:
1. `Fundamentos neurofisiológicos de las vías aferentes/eferentes`
2. `Diseño metodológico y muestra`
3. `Tablas de datos cuantitativos, representación gráfica y evidencia fotográfica original`
4. `Discusión de resultados fundada en los principios de procesamiento sensorial y plasticidad neuronal`

---

## m1_fundamentos

Se entienden los conceptos de vía aferente y vía eferente como dos tipos de vías nerviosas, orientadas a la transmisión de información del sistema nervioso central a la periferia, o viceversa, entendiendo que las vías aferentes transmiten información sensorial al sistema nervioso central, y las vías eferentes envían información motora desde el sistema nervioso central hacia la periferia.

## m1_metodo

En el primer módulo presentado, se ocuparon agujas y una muestra de un solo individuo (N = 1), en distintas zonas del cuerpo, incluyendo la zona de yema del dedo índice, dorso de la mano, cara medial del antebrazo, mentón y nuca, de forma secuencial, interrogando al sujeto sobre la intensidad percibida en cada ensayo en una escala del 1 al 10.

## m1_discusion

Se entiende, basado en los datos obtenidos, que los resultados de zonas como las yemas de los dedos y el dorso de la mano concentran altas cantidades de mecanorreceptores, entendidos como receptores sensoriales que procesan estímulos mecánicos como presión, estiramiento, vibración o sonido.

Cabe aclarar que el registro de 6/10 en el dorso de la mano corresponde al valor final de una percepción que bajó de forma gradual durante el ensayo.

En comparación con la zona de la nuca y mentón, regiones con presencia reducida de mecanorreceptores especializados en comparación con las estructuras previamente mencionadas.

También se tiene en cuenta la variación en el espacio receptivo de las células neuronales de cada región; varían, entendiendo el espacio receptivo como el radio de espacio habilitado en el cual cada neurona es capaz de captar información, siendo que el espacio receptivo de las neuronas es notablemente menor en la yema del dedo índice y en el dorso de la mano en comparación con la nuca y el mentón. Eso también aumenta la precisión para distinguir la intensidad de los estímulos sensoriales en una región.

## m2_fundamentos

Para una tarea de tiempos de reacción tras estímulos auditivos y visuales, deben entenderse los procesos completos de cada índole.

En las reacciones tras estímulos auditivos, se entiende que las ondas sonoras entran por el oído interno, produciendo vibración en el tímpano y en los huesos de la cadena osicular, llegando al oído interno, donde las células ciliadas del órgano de Corti procesan el movimiento y lo convierten en una señal eléctrica.

Posteriormente, la señal viaja a través de la rama coclear del octavo par craneal, el par craneal vestibulococlear; el impulso sube haciendo sinapsis en los núcleos cocleares, el complejo olivar superior y el colículo inferior.

Finalizando el proceso aferente, la señal pasa por el cuerpo geniculado medial del tálamo y llega a la corteza auditiva primaria en el lóbulo temporal, estructura que identifica el sonido. Si este es el proceso dado, la información pasa a zonas como el área de Wernicke y la corteza prefrontal.

Sin embargo, si el sonido es muy fuerte o repentino, el colículo inferior y la formación reticular envían una señal de alarma inmediata antes de la llegada de la señal eléctrica, lo que provoca un reflejo motor de sobresalto o de movimiento para observar de dónde proviene el sonido, a través de la médula espinal y los nervios motores.

En cuanto a las vías nerviosas en la índole de estímulos visuales, el recorrido comúnmente inicia en la retina, donde el estímulo visual viaja por el nervio óptico, el quiasma óptico y el tracto óptico hasta hacer relevo en el cuerpo geniculado lateral del tálamo.

Posteriormente, la señal pasa por las radiaciones ópticas hacia la corteza visual en el lóbulo occipital y se integra en el giro angular y el área de Wernicke para comprender el texto. Tras esta interpretación, se activa el sistema límbico para generar la reacción emocional y la corteza prefrontal toma la decisión de actuar, enviando la orden a la corteza motora primaria bajo la regulación del cerebelo y los ganglios basales.

Finalmente, el impulso desciende por el tracto corticoespinal, cruza en la decusación de las pirámides y llega al asta anterior de la médula espinal, desde donde sale por el nervio periférico hacia la unión neuromuscular para ejecutar el movimiento.

## m2_metodo

Para el segundo módulo, se ocupó una instancia experimental construida en la herramienta gráfica Psychopy Builder, herramienta digital especializada en la experimentación psicológica basada en estímulos, con una muestra N = 1, donde el participante realizó 20 ensayos de forma aleatorizada, constando de 10 estímulos no variables visuales y 10 estímulos auditivos no variables. Cada vez que escuchase el estímulo sonoro o viese el estímulo textual, debía presionar la tecla “Espacio” en el teclado para saltar al siguiente estímulo aleatorio hasta completar los 20 ensayos correspondientes.

La herramienta guarda múltiples datos de forma automática una vez finalizado el experimento, llegando al fin de la secuencia, y los guarda en archivos de hojas de cálculo, que suelen contener muchas variables no necesarias para el estudio, pero que el programa igual registra. Para esto, se ocupó un programa de tipo “Script” de autoría propia construido en el lenguaje de programación Python 3 y documentado por la inteligencia artificial “Opencode”, especializada en programación, para eliminar las variables innecesarias y anomalías, permaneciendo los datos relevantes previamente obtenidos. En la entrega de esta actividad, estarán presentes tanto la hoja de cálculo previa a la limpieza a través de scripts, el script ocupado para la limpieza de datos y la hoja de cálculo “Limpia” obtenida posteriormente.

## m2_discusion

Teniendo en cuenta que el promedio de tiempo de respuesta visual es menor, siendo un promedio de 446,00 milisegundos en 10 ensayos válidos en comparación con el promedio de 503,22 en 9 ensayos válidos de los estímulos auditivos, con una anomalía de más de 1000 milisegundos en un ensayo auditivo, se postula un resultado anómalo, dado que en la mayoría de pruebas aplicadas a muestras y documentadas, los procesos de reacción auditivos suelen ser más rápidos que los visuales. Esto se sustenta teniendo en cuenta que la información auditiva se procesa en una vía más corta, y que analizar estímulos visuales requiere procesar información como color, profundidad, distancia y movimiento.

## m3_fundamentos

Se entiende que la vía aferente visual comienza en la retina, donde los bastones y los conos transforman la luz en una señal eléctrica mediante la fototransducción. Los pigmentos sensibles a la luz cambian su conformación cuando reciben los fotones y ese cambio pone en marcha la respuesta del fotorreceptor. La señal pasa luego a las células bipolares y a las células ganglionares, cuyos axones forman el nervio óptico. Después del quiasma y del tracto óptico, la información hace relevo en el cuerpo geniculado lateral del tálamo y llega a la corteza visual del lóbulo occipital por las radiaciones ópticas.

También se entiende que la exposición continua a la luz disminuye la sensibilidad de los fotorreceptores y que esa sensibilidad se recupera de forma gradual cuando la estimulación termina. Esa recuperación no es inmediata y puede prolongarse durante un tiempo incluso después de que la respuesta eléctrica del fotorreceptor haya vuelto a su nivel inicial.

Cuando la fuente luminosa desaparece y los ojos permanecen cerrados, puede persistir una imagen retenida. Si la imagen conserva la luminancia del estímulo se trata de una postimagen positiva, y si aparece invertida o con colores complementarios se trata de una postimagen negativa. En este último caso se explica por la desensibilización de los conos que fueron estimulados, de modo que los conos no adaptados responden con más fuerza y el percepto resultante tiende al color opuesto. Como en este registro no se informó un color complementario, el análisis se limita a la persistencia de la imagen y a la recuperación de la sensibilidad.

La vía eferente interviene al final del proceso, porque el participante informa verbalmente lo que percibe y detiene el cronómetro con el dedo. Esa respuesta motora desciende desde la corteza por la vía corticoespinal hasta el nervio periférico y la unión neuromuscular.

## m3_metodo

Para el tercer módulo se ocupó una muestra de un solo individuo, en la que el estudiante realizó el rol de participante y de experimentador. Se utilizó la linterna del teléfono como fuente luminosa, manteniendo una distancia mínima de treinta centímetros y exposiciones de entre dos y cinco segundos. Después de cada exposición el participante cerraba los ojos y ponía en marcha un cronómetro manual, que detenía en el momento en que la imagen retenida desaparecía. Se realizaron cinco ensayos.

Las medidas de seguridad consistieron en no acercar la fuente a menos de treinta centímetros, no mantener la mirada fija más tiempo del necesario y suspender la sesión ante cualquier molestia o antecedente de fotosensibilidad. No se usaron pantallas ni programas, ya que el registro fue manual y luego se volcó a una tabla con la exposición, la duración de la postimagen y las observaciones.

## m3_discusion

Los cinco ensayos dieron duraciones de diez, seis, seis, ocho y cero segundos. La media fue de seis segundos, la mediana de seis segundos y la desviación estándar de tres segundos con siete décimas. El rango fue amplio, entre cero y diez segundos, lo que muestra una variabilidad considerable para un mismo estímulo.

La persistencia de la imagen se explica porque la señal retinal sigue activa durante un breve intervalo después de que cesa la luz y porque la sensibilidad de los fotorreceptores se recupera de manera gradual. Esa recuperación no se limita a que la respuesta eléctrica vuelva a su nivel inicial, sino que la sensibilidad puede permanecer reducida durante un tiempo adicional por el blanqueo del pigmento y por los mecanismos que regulan la ganancia de la cascada de fototransducción.

La relación entre el tiempo de exposición y la duración de la postimagen no fue uniforme. El primer ensayo, con cuatro segundos de exposición, produjo la postimagen más larga, de diez segundos. El cuarto ensayo, con cinco segundos de exposición, dio ocho segundos y además se describió como de menor intensidad que el primero. Con solo cinco observaciones no es posible establecer una tendencia. La fatiga atencional, el estado de adaptación previo de la retina, la distancia real al flash y la precisión del cronómetro manual pudieron influir más que la duración nominal de la exposición. Para repetir el ensayo conviene aleatorizar el orden, calibrar la intensidad luminosa y dejar un período de adaptación a la oscuridad entre ensayos.

El quinto ensayo, con dos segundos de exposición y cero segundos de postimagen, se conservó como dato válido. Que no se observara imagen no significa que el procedimiento fallara, sino que en esa condición no se manifestó una imagen retenida mensurable. Su inclusión evita elevar artificialmente la media y resulta coherente con la variabilidad esperable en un fenómeno perceptivo subjetivo. Como no se informó un color complementario, no corresponde usar la teoría oponente como explicación directa de estos datos. El análisis se apoya en la persistencia retinal y en la adaptación de los fotorreceptores.

Desde la neuroplasticidad aplicada, este protocolo muestra una plasticidad de corto plazo. El sistema visual modula su sensibilidad según la historia reciente de estimulación y la recupera de forma progresiva. Comprender estos mecanismos ayuda a pensar estrategias de rehabilitación y entrenamiento perceptivo, aunque el tamaño de la muestra y la falta de calibración instrumental limitan cualquier generalización.

## conclusiones

Finalizada la experimentación, se considera el concepto de neuroplasticidad aplicada como un proceso automático del sistema nervioso en actividades repetitivas pero cognitiva o motormente exigentes, postulando que, por ejemplo, en ensayos más extensos orientados a medir tiempos de reacción ante estímulos visuales, sin estímulos auditivos, una muestra grande en general mostraría una mejoría a largo plazo de los procesos de reacción ante estímulos visuales en comparación con los auditivos, considerando que la neuroplasticidad es un proceso fundamental no solo en el entrenamiento de capacidades, sino en la rehabilitación o reorientación de las mismas.

Se considera un proceso fundamental para el entrenamiento cognitivo, la rehabilitación, y procesos psicoterapéuticos.

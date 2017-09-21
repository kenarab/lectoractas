# Lector de Actas y/o Telegramas electorales

La idea es hacer un lector de actas electorales y/o telegramas. 

Va a recibir la imagen de un acta y debe leer las cantidades consignadas (en forma manuscrita) en el acta. 

Análisis top-down de los pasos para reconocer las cantidades en un acta:

1. Reconocer las líneas verticales y horizonales de la grilla, y los cuadros donde los presidentes de mesa escriben las cifras. Según lo que vi, el algoritmo a usar sería Hough Lines (https://es.wikipedia.org/wiki/Transformada_de_Hough#Detectando_l.C3.ADneas_rectas)

2. Identificar cada cuadro con la lista/categoría correspondiente. Esto podría hacerse con OCR sobre el texto preimpreso de las actas, o teniendo precargadas las grillas y qué valor esperar en cada celda. Tener en cuenta que de acuerdo a la circunscripción, las grillas cambian. La complejidad de este punto, además de precargar los diseños de grillas para cada jurisdicción, estaría en matchear una grilla "teórica" con la grilla real de una foto que podría estar deformada o no haber detectado todas las líneas.

3. A partir del recorte de un cuadro, que debería tener un número manuscrito de hasta 3 cifras, es necesario separar en dígitos. Para esto habría que aplicar identificación de contornos y encontrar la división de los números.

4. Preparar las imágenes de cada dígito para llevarlas al formato que lo recibe el siguiente paso: imágenes de 28x28 pixeles, formato PNG sin transparencia y en escala de grises, con el número en blanco y el fondo en negro (invertido).

5. Procesar cada imagen con la red de deep-learning entrenada con la base MNIST (http://yann.lecun.com/exdb/mnist/). La forma más sencilla que encontré es con este proyecto: https://github.com/JoelKronander/TensorFlask 

6. Finalmente se deberían integrar los resultados, formando a partir de los dígitos individuales las cifras para cada lista/categoría. Y finalmente analizar la consistencia del acta. Si el acta resulta consistente, seguramente quiere decir que los datos se interpretaron bien y se puede dar por válida. Sino requeriría intervención humana para corregir la lectura de todas o algunas de las celdas de la grilla. 


Este proyecto trabajaría solamente con la decodificación de un acta. Para que tenga sentido debería integrarse con otros que reciban las actas por diversas vías (ejemplo BOT de Telegram y/o Whatsapp).


# Links

* https://stackoverflow.com/questions/39752235/python-how-to-detect-vertical-and-horizontal-lines-in-an-image-with-houghlines-w

* https://web.stanford.edu/class/cs231m/projects/final-report-yang-pu.pdf (Paper donde explica el enforque para detección multi-dígito)

* https://github.com/JoelKronander/TensorFlask ("web service" para reconocimiento de dígitos individuales)


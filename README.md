# 14 Kg de CO2: Análisis de la Huella de Carbono y Rendimiento en Algoritmos de Recomendación Basados en Sesiones

Repositorio oficial del estudio realizado para el proyecto del curso Sistemas Recomendadores 2024-1 de la Pontificia Universidad Católica de Chile.

**Alumnos**
- Juan Carlos Gil
- Alejandro Plaza

<br>

Este proyecto está fuertemente basado en el estudio *The Effect of Third Party Implementations on Reproducibility* de  Balázs Hidasi y Ádám Tibor Czapp. Se puede encontrar más información sobre las implementaciones utilizadas en el [repositorio oficial](https://github.com/hidasib/gru4rec_third_party_comparison) de dicha investigación.

**Índice**
1. [Estructura del repositorio](#estructura)
2. [Datasets](#datasets)
3. [Ejecución local](#local)
4. [Modificaciones a submodulos](#submodulos)
5. [Consideraciones adicionales](#consideraciones)


<br>

<div id='estructura' />

## Estructura del repositorio

### datasets/
En esta carpeta hay que agregar los set de datos a utilizar en sus respectivas carpetas. En dichas carpetas se agregan los sets de datos tras su preprocesamiento.

### submodulos
El repositorio hace referencia a los repositorios oficilas de las implementaciones utilizadas. El detalle de los repositorios utilizados se encuentra en el archivo ```.gitmodules``` y para poder usarlos de manera local es necesario ejecutar el siguiente comando:

``` 
git submodule update --init --recursive 
``` 

### Preprocess/
En esta carpeta se encuentra el preprocesado utilizado para cada uno de los datasets. En caso de querer utilizar datos nuevos es necesario agregar su procesamiento en esta carpeta con el nombre ```<dataset>_preproc.py```

### Train_Test_Best_Models/
En esta carpeta se encuentran los cuadernillos con los experimentos realizados. El nombre de cada Jupyter Notebook hace referencia a la implementación usada en dicho experimento.

### trained_models/
En esta carpeta se generan los modelos entrenados y se guardan los resultados de CO2 entregados por CodeCarbon. Los resultados para cada implementación y dataset se encuentran en archivos ```trainingData.json```. Dependiendo del notebook utilizado los resultados pueden estar en un único archivo con detalles o guardados en una carpeta específica del dataset (más detalle en en el incido de Consideraciones adicionales).


<br>

<div id='datasets' />

## Datasets


<br>

<div id='local' />

## Ejecución local
- Incluir comando para submodulos

git submodule update --init --recursive


<br>

<div id='submodulos' />

## Modificaciones a submodulos

En KerasGRU4Rec/model/gru4rec.py 
``` 
# Linea 191
# gru_layer.reset_states(states=hidden_states)
gru_layer.reset_states()

# Linea 236
# gru_layer.reset_states(states=hidden_states)
gru_layer.reset_states()
```

<br>

<div id='consideraciones' />

## Consideraciones adicionales

En caso de que se quiera utilizar un dataset u modelo no utilizado en el experimento, es necesario crear su respectiva carpeta con el formato ```<nombre modelo>_<función de pérdida>``` en la carpeta de los modelos entrenados. En dicha carpeta, por cada dataset hay que crear una carpeta con el nombre de este y un archivo ```trainingData.json``` vacio.
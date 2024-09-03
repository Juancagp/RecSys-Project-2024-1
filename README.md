# 14 Kg of CO2: Analyzing the Carbon Footprint and Performance of Session-Based Recommendation Algorithms
**Note:** This documentation is currently in Spanish, but an English version will be available soon.

Repositorio oficial del estudio realizado para el proyecto del curso Sistemas Recomendadores 2024-1 de la Pontificia Universidad Católica de Chile.

**Alumnos**
- Alejandro Plaza
- Juan Gil

**Profesor**
- Denis Parra

<br>

Este proyecto está fuertemente basado en el paper *The Effect of Third Party Implementations on Reproducibility* de  Balázs Hidasi y Ádám Tibor Czapp. Se puede encontrar más información sobre las implementaciones utilizadas en el [repositorio oficial](https://github.com/hidasib/gru4rec_third_party_comparison) de dicha investigación.

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
Los datasets utilizados para la realización de los experimentos pueden encontrase en los siguientes enlaces:

- [Yoochoose](https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015/data)
- [Rees46](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- [Coveo](https://github.com/coveooss/shopper-intent-prediction-nature-2020)
- [RetailRocket](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)
- [Diginetica](https://competitions.codalab.org/competitions/11161#learn_the_details-data2)

<br>

<div id='local' />

## Ejecución local
Para ejecutar los archivos hay que modificar el nombre de los modelos, función de pérdida a usar y datasets a utilizar en el experimento. Dependiendo del notebook dichos parámetros se colocan al inicio o en los strings ingresados a las funciones. Una vez seleccionados, ejecutar las celdas en orden. Para algunos notebooks el test_script generado debe usarse en consola en lugar de entregar las métricas directamente (más detalle en en el incido de Consideraciones adicionales).

En caso de que se quiera utilizar un dataset u modelo no utilizado en el experimento, es necesario crear su respectiva carpeta con el formato ```<nombre modelo>_<función de pérdida>``` en la carpeta de los modelos entrenados. En dicha carpeta, por cada dataset hay que crear una carpeta con el nombre de este y un archivo ```trainingData.json``` vacío.

<br>

<div id='submodulos' />

## Modificaciones a submodulos
Actualizaciones y modificaciones en los repositorios de las implementaciones podrían generar problemas para su uso a futuro. En este caso, no se logró hacer uso de GRU4Rec y para poder utilizar KerasGRU4Rec, se realizan los siguientes cambios al archivo ```KerasGRU4Rec/model/gru4rec.py``` en las líneas 191 y 236.

<pre>
<code>
190 ...
191 # gru_layer.reset_states(states=hidden_states)
192 gru_layer.reset_states()
---

235...
236 # gru_layer.reset_states(states=hidden_states)
237 gru_layer.reset_states()
</code>
</pre>


<br>

<div id='consideraciones' />

## Consideraciones adicionales
Como los experimentos fueron realizados en paralelo en branches diferentes, existen variaciones en el formato de algunos Jupyter Notebooks y sus respectivos archivos ```trainingData.json```. Específicamente, es posible distinguir dos grupos de formato:

- Experimentos de Torch-GRU4Rec y GRU4Rec-pytorch
- Experimentos de KerasGRU4Rec, GRU4Rec-TensorFlow y Recpack.


No obstamte lo anterior, la estructura general de cada experimento es la misma. Los resultados del primer grupo de experimentos se encuentran en un mismo archivo con detalles del dataset y función de pérdida utilizado, mientras que los del segundo grupo se encuentras por separado en una carpeta específica para el dataset y función de pérdida. 

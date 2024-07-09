# RecSys-Project
Repositorio para proyecto del curso Sistemas Recomendadores de la PUC 2024-1

Alumnos:
- Juan Carlos Gil
- Alejandro Plaza

Proyecto basado en la investigación de Hidasi. Se pueden encontrar más detalles en el [repositorio oficial](https://github.com/hidasib/gru4rec_third_party_comparison) de su investigación.

# Hacer índice de readme

# Estructura repositorio

# Links datasets

# Ejecución local
- Incluir comando para submodulos

# Modificaciones a submodulos

En KerasGRU4Rec/model/gru4rec.py 
``` 
# Linea 191
# gru_layer.reset_states(states=hidden_states)
gru_layer.reset_states()

# Linea 236
# gru_layer.reset_states(states=hidden_states)
gru_layer.reset_states()
```

# Consideraciones Adicionales

En caso de que se quiera utilizar un dataset u modelo no utilizado en el experimento, es necesario crear su respectiva carpeta con el formato ```<nombre modelo>_<función de pérdida>``` en la carpeta de los modelos entrenados. En dicha carpeta, por cada dataset hay que crear una carpeta con el nombre de este y un archivo ```trainingData.json``` vacio.
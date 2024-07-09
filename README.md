# RecSys-Project
Repositorio para proyecto del curso Sistemas Recomendadores de la PUC 2024-1

Alumnos:
- Juan Carlos Gil
- Alejandro Plaza


Proyecto basado en la investigación de Hidasi. Se pueden encontrar más detalles en el [repositorio oficial](https://github.com/hidasib/gru4rec_third_party_comparison) de su investigación.

En KerasGRU4Rec/model/gru4rec.py 
``` 
# Linea 191
# gru_layer.reset_states(states=hidden_states)
gru_layer.reset_states()

# Linea 236
# gru_layer.reset_states(states=hidden_states)
gru_layer.reset_states()
```
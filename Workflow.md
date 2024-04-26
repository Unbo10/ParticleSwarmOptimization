# Flujo de trabajo

## Flujo de GitHub Local

Para empezar a hacer cambios dentro del repositorio local se deben traer todos los cambios hechos en el repositorio remoto:

```bash
git pull origin branch_name
```

Para realizar cualquier cambio se debe crear una nueva rama que tenga un nombre descriptivo corto y hacer el cambio: 

```bash
git checkout -b new_branch_name
```

Y para alternar entre ramas se pueden usar:

```bash
git switch branch_name

# Less error-prone
```

```bash
git checkout branch_name
```

Antes de cualquier commit se debe verificar el estado del repositorio: 

```bash
git status
```

Si existen archivos que no están siendo rastreados por Git o, lo que es lo mismo, archivos nuevos, modificados o eliminados se deben añadir al repositorio: 

```bash
git add file_name.ext
```

Si son muchos archivos y se desea agregarlos todos de una sola vez: 

```bash
git add .
```

Al momento de realizar commits de los cambios se debe seguir el siguiente formato: 

```bash
git commit -am "Header:Description"
```

El encabezado hace referencia al cambio especifico realizado. La descripción no puede ser muy grande o aparecerá cortada en GitHub. 50 caracteres deberían ser suficientes.

## Flujo de GitHub Remoto

Para subir el contenido al repositorio remoto: 

```bash
git push origin new_branch_name
```

Esto implica que el cambio realizado en ``new_branch_name`` fue realizado correctamente y está listo para ser incorporado a ``master`` o a una rama 'padre'.

En el servidor de GitHub se programa el *Pull Request* (PR) de la rama “new_branch_name” a la rama de “master” con la etiqueta adecuada y se debe revisar por los otros dos miembros del equipo, quienes harán comentarios y/o correciones o aprobarán el PR.
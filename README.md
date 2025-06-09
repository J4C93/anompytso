# 🧪 anompytso

Este script permite calcular **anomalías de Temperatura, Salinidad y Oxígeno disuelto** a partir de datos CTD almacenados en un archivo Excel, usando climatologías mensuales de referencia.

---

## 📦 Requisitos

- Python 3.7 o superior
- Paquetes necesarios:
  - `numpy`
  - `pandas`
  - `argparse`

---

## 📂 Archivos requeridos

El script carga los siguientes archivos `.mat`, que deben estar en la ruta:

```
C:\jactools\anompytso\database\
```

- `TEMP_TOTAL_1991_2020_V2.mat`
- `PSAL_TOTAL_1991_2020_V2.mat`
- `MonthlyTSOClimatology.mat`
- `lon.mat`
- `lat.mat`

---

## 🚀 Cómo usar

```bash
python anompy.py --archivo "ruta/datos.xlsx" --hoja "Hoja1" --columnas A,B,C,D,E,F,G
```

### 🔠 Argumentos

| Opción        | Descripción                                                   |
|---------------|---------------------------------------------------------------|
| `--archivo`   | Ruta al archivo Excel con los datos CTD                       |
| `--hoja`      | Nombre de la hoja dentro del archivo Excel                    |
| `--columnas`  | Letras de columnas (en orden): `lon,lat,prof,mes,temp,sali,oxi` |

📌 **Ejemplo:**
```bash
python anompy.py --archivo "data cruda.xlsx" --hoja "CTD" --columnas A,B,C,D,E,F,G
```

---

## 📤 Salida

Se genera un archivo Excel llamado:

```
animaladas.xlsx
```

Este archivo contiene tres nuevas columnas con las anomalías:

- `T_anom` → Anomalía de temperatura  
- `S_anom` → Anomalía de salinidad  
- `O_anom` → Anomalía de oxígeno disuelto  

---

## 🧠 Notas

- La profundidad (`z`) debe estar en valores positivos hacia el fondo.
- La columna `mes` debe contener valores enteros del 1 al 12.
- Las coordenadas de latitud y longitud deben estar en grados decimales.

---

## ✍️ Autor

Desarrollado por **J4C93**  

---

## 🪪 Licencia

MIT License

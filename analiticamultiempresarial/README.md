# Integrador Multiempresarial

Proyecto integrador para aprender un **flujo completo de datos**: desde la simulación y
limpieza de datos con Python, pasando por una API REST con Spring Boot, hasta un frontend
en React que permite gestionar la información.

El proyecto se construye sobre dos entidades: **usuarios** y **gastos**.
La entidad **usuarios** está **resuelta como ejemplo guía**. La entidad **gastos** es la que
**el estudiante debe completar** replicando lo que ya se hizo con usuarios.

---

## 📁 Estructura

```
integradormultiempresarial/
├── analiticamultiempresarial/   →  Python + pandas (análisis de datos)
├── backendmultiempresarial/     →  Spring Boot + JPA (API REST)
└── fronmultiempresarial/        →  React + Vite + Tailwind (interfaz)
```

| Carpeta | Tecnología | Qué hace |
|---------|------------|----------|
| `analiticamultiempresarial` | Python, pandas, matplotlib | Simula, limpia, transforma y grafica datos |
| `backendmultiempresarial` | Spring Boot 3, JPA, H2 | CRUD REST de usuarios y gastos (CORS abierto) |
| `fronmultiempresarial` | React, Vite, TailwindCSS | Landing + panel CRUD conectado al backend |

---

## 🎯 Objetivo pedagógico

Al terminar el proyecto, el estudiante debe ser capaz de:

1. **Simular** una fuente de datos realista (con errores controlados) usando Python.
2. **Generar** fuentes de datos en distintos formatos (CSV, JSON).
3. **Limpiar** los datos (textos, números y fechas) para garantizar calidad.
4. **Transformar** los datos limpios usando `query` (filtros) y `groupby` (agrupaciones
   con `sum`, `count`, `mean`) para obtener información útil.
5. **Visualizar** los resultados con gráficas de línea, barras y torta.
6. Entender una **API REST por capas** (model → repository → service → controller)
   y exponer un **CRUD** completo.
7. **Conectar** un frontend con un backend (consumo de API, CORS).

> La entidad **usuarios** funciona como **modelo de referencia**: está implementada de
> principio a fin. El estudiante aprende leyéndola y luego **completa la entidad gastos**.

---

## ✅ Lo que el estudiante debe completar (todo lo de GASTOS)

Replicar, para **gastos**, lo que ya existe para **usuarios**. La entidad gasto tiene los
campos: `id`, `fecha`, `monto`, `descripcion`.

### En `analiticamultiempresarial/` (Python)

| Archivo | Tarea a completar |
|---------|-------------------|
| `notebook/simulaciones/simulacionGasto.py` | Función que simule N gastos e **inyecte errores controlados** en `id`, `fecha`, `monto`, `descripcion`. |
| `notebook/simulaciones/generacionGasto.py` | Función que convierta la lista de gastos en fuentes **CSV y JSON**. |
| `notebook/limpieza/limpiezaGasto.py` | Función `limpiar_datos_gasto(...)`: validar texto, números (`monto > 0`), fecha, y eliminar registros con campos obligatorios vacíos. |
| `notebook/transformacion/transformacionGasto.py` | Resolver los **5 ejercicios** de `query` + `groupby` (sum, count, mean) ya planteados en el archivo. |
| `notebook/descripcion/descripcionGasto.py` | Describir el set de gastos (`.describe()`, `.info()`, conteos, etc.). |
| `notebook/reportes/reportesGasto.py` | Usar las **gráficas genéricas** (`graficasGenericas.py`) para graficar resultados de gastos. |
| `main.py` | Integrar todo el flujo de gastos (simular → generar → limpiar → transformar → graficar). |

### En `backendmultiempresarial/` y `fronmultiempresarial/`
El CRUD de gastos ya está implementado como referencia. El reto opcional es **extenderlo**:
agregar filtros, validaciones o endpoints de analítica (por ejemplo, total de gastos por
categoría) y mostrarlos en el frontend.

---

## 📊 Evaluación

Nota total: **100 puntos**.

| # | Criterio | Qué se evalúa | Puntos |
|---|----------|---------------|:------:|
| 1 | **Simulación de gastos** | Genera N gastos y inyecta errores controlados realistas. | 15 |
| 2 | **Generación de fuentes** | Exporta correctamente a CSV y JSON. | 10 |
| 3 | **Limpieza de gastos** | Valida textos, números y fechas; elimina registros inválidos. | 20 |
| 4 | **Transformación** | Resuelve los 5 ejercicios con `query` + `groupby` (sum, count, mean). | 25 |
| 5 | **Gráficas** | Usa las funciones genéricas para línea, barras y torta con datos de gastos. | 15 |
| 6 | **Integración en `main.py`** | El flujo completo de gastos corre sin errores. | 10 |
| 7 | **Calidad y documentación** | Código en español, ordenado, comentado y funcional. | 5 |

**Criterios transversales (descuentan si fallan):**
- El código debe **ejecutarse sin errores**.
- Comentarios y nombres **en español**.
- Respetar la **estructura por carpetas/capas** existente.

---

## ▶️ Cómo ejecutar cada parte

**1. Análisis (Python)**
```bash
cd analiticamultiempresarial
python main.py
```
Requiere `pandas` y `matplotlib` (`pip install pandas matplotlib`).

**2. Backend (Spring Boot)**
```bash
cd backendmultiempresarial
mvn spring-boot:run          # o ejecutar desde el IDE
```
API en `http://localhost:8080` · precarga 500 usuarios y 500 gastos al arrancar.

**3. Frontend (React)**
```bash
cd fronmultiempresarial
npm install
npm run dev                  # http://localhost:5173
```
El backend debe estar corriendo para ver y gestionar datos reales.

---

## 💡 Recomendación
Versionar el proyecto con **git** (`git init` + commits frecuentes) para no perder el trabajo.

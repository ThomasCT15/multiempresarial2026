# backendmultiempresarial

Backend REST con **Spring Boot + JPA**, organizado **por capas**, para las tablas
`usuarios` y `gastos`. Incluye **CRUD básico** en cada una y **CORS genérico** (todo cliente).

## Arquitectura por capas

```
controller  ->  service  ->  repository  ->  (base de datos)
                                model (entidades JPA)
```

| Capa        | Paquete                              | Qué hace                                  |
|-------------|--------------------------------------|-------------------------------------------|
| model       | `com.multiempresarial.backend.model` | Entidades JPA (tablas)                    |
| repository  | `...repository`                      | Acceso a datos (hereda de JpaRepository)  |
| service     | `...service`                         | Lógica de negocio                         |
| controller  | `...controller`                      | Endpoints REST                            |
| config      | `...config`                          | `CorsConfig` (CORS genérico)              |

## Cómo ejecutar

```bash
cd backendmultiempresarial
./mvnw spring-boot:run        # Linux/Mac
mvnw.cmd spring-boot:run      # Windows (o:  mvn spring-boot:run)
```

Arranca en `http://localhost:8080`.
Base de datos en memoria **H2** (no requiere instalar nada).
Consola H2: `http://localhost:8080/h2-console` (JDBC URL `jdbc:h2:mem:multiempresarial`, user `sa`, sin password).

## Endpoints CRUD

### Usuarios — `/api/usuarios`
| Método | Ruta                 | Acción          |
|--------|----------------------|-----------------|
| GET    | `/api/usuarios`      | Listar todos    |
| GET    | `/api/usuarios/{id}` | Buscar por id   |
| POST   | `/api/usuarios`      | Crear           |
| PUT    | `/api/usuarios/{id}` | Actualizar      |
| DELETE | `/api/usuarios/{id}` | Eliminar        |

Ejemplo body (POST/PUT):
```json
{ "nombres": "juan jimenez", "contrasena": "admin123", "edad": 24, "correo": "ju@correo.com" }
```

### Gastos — `/api/gastos`
| Método | Ruta               | Acción          |
|--------|--------------------|-----------------|
| GET    | `/api/gastos`      | Listar todos    |
| GET    | `/api/gastos/{id}` | Buscar por id   |
| POST   | `/api/gastos`      | Crear           |
| PUT    | `/api/gastos/{id}` | Actualizar      |
| DELETE | `/api/gastos/{id}` | Eliminar        |

Ejemplo body (POST/PUT):
```json
{ "fecha": "2026-05-06", "monto": 150000.0, "descripcion": "transporte" }
```

## CORS
Habilitado de forma genérica en `config/CorsConfig.java` (`/**`, `allowedOrigins("*")`,
todos los métodos y cabeceras), reforzado con `@CrossOrigin(origins = "*")` en cada controlador.
Cualquier front-end puede consumir la API sin bloqueo del navegador.

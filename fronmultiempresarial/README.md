# fronmultiempresarial

Frontend en **React + Vite + TailwindCSS** para la plataforma Multiempresarial.
Landing atractiva en tonos **morados** con degradados y difuminados (glassmorphism),
iconos (`lucide-react`), tipografía profesional (**Poppins** + **Inter**) y un
**panel CRUD** que se conecta al backend Spring Boot.

## Requisitos
- Node.js 18+ y npm

## Instalación y ejecución
```bash
cd fronmultiempresarial
npm install
npm run dev
```
Abre en `http://localhost:5173`.

## Conexión con el backend
Por defecto consume la API en `http://localhost:8080/api`.
Para cambiarla, crea un archivo `.env` con:
```
VITE_API_URL=http://localhost:8080/api
```
> El backend (`backendmultiempresarial`) debe estar corriendo y tiene CORS habilitado
> para cualquier origen, así que el navegador no bloqueará las peticiones.

## Estructura
```
src/
├── api/client.js          Cliente fetch (usuariosApi, gastosApi)
├── components/
│   ├── Navbar.jsx          Barra de navegación
│   ├── Hero.jsx            Portada con blobs difuminados e imagen
│   ├── Features.jsx        Tarjetas de características con iconos
│   ├── GestionCrud.jsx     Sección con pestañas Usuarios / Gastos
│   ├── CrudPanel.jsx       Tabla + formulario CRUD genérico
│   └── Footer.jsx
└── App.jsx
```

## Funcionalidad CRUD
- **Usuarios** (`nombres, contraseña, edad, correo`) y **Gastos** (`fecha, monto, descripción`).
- Crear, listar, editar y eliminar, sincronizado con la base de datos vía API REST.

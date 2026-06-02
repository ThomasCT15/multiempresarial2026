// Cliente de API que se conecta con el backend Spring Boot.
// Se puede cambiar la URL con la variable de entorno VITE_API_URL.
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8080/api";

async function pedir(ruta, opciones = {}) {
  const respuesta = await fetch(`${API_URL}${ruta}`, {
    headers: { "Content-Type": "application/json" },
    ...opciones,
  });

  if (!respuesta.ok) {
    throw new Error(`Error ${respuesta.status}: ${respuesta.statusText}`);
  }

  // DELETE responde 204 (sin cuerpo)
  if (respuesta.status === 204) return null;
  return respuesta.json();
}

// Fabrica un CRUD generico para un recurso (usuarios | gastos)
function crearRecurso(recurso) {
  return {
    listar: () => pedir(`/${recurso}`),
    obtener: (id) => pedir(`/${recurso}/${id}`),
    crear: (datos) =>
      pedir(`/${recurso}`, { method: "POST", body: JSON.stringify(datos) }),
    actualizar: (id, datos) =>
      pedir(`/${recurso}/${id}`, { method: "PUT", body: JSON.stringify(datos) }),
    eliminar: (id) => pedir(`/${recurso}/${id}`, { method: "DELETE" }),
  };
}

export const usuariosApi = crearRecurso("usuarios");
export const gastosApi = crearRecurso("gastos");
export { API_URL };

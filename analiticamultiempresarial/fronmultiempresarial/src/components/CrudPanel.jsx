import { useEffect, useState } from "react";
import { Plus, Pencil, Trash2, X, RefreshCw, AlertTriangle } from "lucide-react";

/**
 * Panel CRUD generico.
 * props:
 *  - api: objeto con { listar, crear, actualizar, eliminar }
 *  - campos: [{ nombre, etiqueta, tipo, placeholder }]
 *  - titulo: texto
 */
export default function CrudPanel({ api, campos, titulo }) {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState(estadoInicial(campos));
  const [editandoId, setEditandoId] = useState(null);
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState(null);

  function estadoInicialLocal() {
    return estadoInicial(campos);
  }

  async function cargar() {
    setCargando(true);
    setError(null);
    try {
      setItems(await api.listar());
    } catch (e) {
      setError(`No se pudo conectar con el backend. ${e.message}`);
    } finally {
      setCargando(false);
    }
  }

  useEffect(() => {
    cargar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function cambiar(nombre, valor) {
    setForm((f) => ({ ...f, [nombre]: valor }));
  }

  async function guardar(e) {
    e.preventDefault();
    setError(null);
    try {
      const datos = normalizar(form, campos);
      if (editandoId == null) {
        await api.crear(datos);
      } else {
        await api.actualizar(editandoId, datos);
      }
      cancelarEdicion();
      await cargar();
    } catch (e) {
      setError(`No se pudo guardar. ${e.message}`);
    }
  }

  function editar(item) {
    const datos = {};
    campos.forEach((c) => (datos[c.nombre] = item[c.nombre] ?? ""));
    setForm(datos);
    setEditandoId(item.id);
  }

  function cancelarEdicion() {
    setForm(estadoInicialLocal());
    setEditandoId(null);
  }

  async function borrar(id) {
    if (!confirm("¿Eliminar este registro?")) return;
    setError(null);
    try {
      await api.eliminar(id);
      await cargar();
    } catch (e) {
      setError(`No se pudo eliminar. ${e.message}`);
    }
  }

  return (
    <div className="grid gap-6 lg:grid-cols-[360px_1fr]">
      {/* Formulario */}
      <form onSubmit={guardar} className="glass h-fit rounded-2xl p-6">
        <h3 className="font-display text-lg font-semibold">
          {editandoId == null ? `Nuevo ${titulo}` : `Editar ${titulo}`}
        </h3>
        <div className="mt-4 space-y-3">
          {campos.map((c) => (
            <div key={c.nombre}>
              <label className="mb-1 block text-sm text-slate-300">{c.etiqueta}</label>
              <input
                className="campo"
                type={c.tipo}
                value={form[c.nombre]}
                placeholder={c.placeholder}
                onChange={(e) => cambiar(c.nombre, e.target.value)}
                required={c.requerido !== false}
              />
            </div>
          ))}
        </div>
        <div className="mt-5 flex gap-3">
          <button type="submit" className="btn-marca flex-1">
            {editandoId == null ? (<><Plus className="h-4 w-4" /> Crear</>) : (<><Pencil className="h-4 w-4" /> Actualizar</>)}
          </button>
          {editandoId != null && (
            <button type="button" onClick={cancelarEdicion} className="btn-ghost">
              <X className="h-4 w-4" /> Cancelar
            </button>
          )}
        </div>
      </form>

      {/* Tabla */}
      <div className="glass overflow-hidden rounded-2xl">
        <div className="flex items-center justify-between border-b border-white/10 px-5 py-4">
          <h3 className="font-display text-lg font-semibold">Listado de {titulo}s</h3>
          <button onClick={cargar} className="btn-ghost px-3 py-1.5 text-sm">
            <RefreshCw className={`h-4 w-4 ${cargando ? "animate-spin" : ""}`} /> Refrescar
          </button>
        </div>

        {error && (
          <div className="m-4 flex items-start gap-3 rounded-xl border border-amber-400/30 bg-amber-400/10 p-3 text-sm text-amber-200">
            <AlertTriangle className="mt-0.5 h-4 w-4 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="bg-white/5 text-slate-300">
              <tr>
                <th className="px-5 py-3 font-medium">ID</th>
                {campos.map((c) => (
                  <th key={c.nombre} className="px-5 py-3 font-medium">{c.etiqueta}</th>
                ))}
                <th className="px-5 py-3 text-right font-medium">Acciones</th>
              </tr>
            </thead>
            <tbody>
              {items.length === 0 && !cargando && (
                <tr>
                  <td colSpan={campos.length + 2} className="px-5 py-10 text-center text-slate-400">
                    Sin registros todavía.
                  </td>
                </tr>
              )}
              {items.map((item) => (
                <tr key={item.id} className="border-t border-white/5 transition hover:bg-white/5">
                  <td className="px-5 py-3 text-slate-400">{item.id}</td>
                  {campos.map((c) => (
                    <td key={c.nombre} className="px-5 py-3 text-slate-100">{String(item[c.nombre] ?? "")}</td>
                  ))}
                  <td className="px-5 py-3">
                    <div className="flex justify-end gap-2">
                      <button onClick={() => editar(item)} className="rounded-lg border border-white/10 bg-white/5 p-2 transition hover:bg-white/10" title="Editar">
                        <Pencil className="h-4 w-4 text-fuchsia-300" />
                      </button>
                      <button onClick={() => borrar(item.id)} className="rounded-lg border border-white/10 bg-white/5 p-2 transition hover:bg-red-500/20" title="Eliminar">
                        <Trash2 className="h-4 w-4 text-red-300" />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

function estadoInicial(campos) {
  const estado = {};
  campos.forEach((c) => (estado[c.nombre] = ""));
  return estado;
}

// Convierte los campos numericos de texto a numero antes de enviar al backend
function normalizar(form, campos) {
  const datos = { ...form };
  campos.forEach((c) => {
    if (c.tipo === "number") {
      datos[c.nombre] = datos[c.nombre] === "" ? null : Number(datos[c.nombre]);
    }
  });
  return datos;
}

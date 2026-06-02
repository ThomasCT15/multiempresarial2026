import { useState } from "react";
import { Users, Wallet } from "lucide-react";
import CrudPanel from "./CrudPanel.jsx";
import { usuariosApi, gastosApi, API_URL } from "../api/client.js";

const camposUsuario = [
  { nombre: "nombres", etiqueta: "Nombres", tipo: "text", placeholder: "Juan Jimenez" },
  { nombre: "contrasena", etiqueta: "Contraseña", tipo: "text", placeholder: "admin123" },
  { nombre: "edad", etiqueta: "Edad", tipo: "number", placeholder: "24" },
  { nombre: "correo", etiqueta: "Correo", tipo: "email", placeholder: "ju@correo.com" },
];

const camposGasto = [
  { nombre: "fecha", etiqueta: "Fecha", tipo: "date", placeholder: "" },
  { nombre: "monto", etiqueta: "Monto", tipo: "number", placeholder: "150000" },
  { nombre: "descripcion", etiqueta: "Descripción", tipo: "text", placeholder: "transporte" },
];

const pestanas = [
  { clave: "usuarios", etiqueta: "Usuarios", icono: Users, api: usuariosApi, campos: camposUsuario, titulo: "usuario" },
  { clave: "gastos", etiqueta: "Gastos", icono: Wallet, api: gastosApi, campos: camposGasto, titulo: "gasto" },
];

export default function GestionCrud() {
  const [activa, setActiva] = useState("usuarios");
  const actual = pestanas.find((p) => p.clave === activa);

  return (
    <section id="gestion" className="relative py-24">
      {/* difuminado morado de fondo */}
      <div className="pointer-events-none absolute left-1/2 top-20 -z-10 h-80 w-[40rem] -translate-x-1/2 rounded-full bg-purple-700/20 blur-3xl" />

      <div className="mx-auto max-w-6xl px-6">
        <div className="text-center">
          <h2 className="font-display text-4xl font-bold tracking-tight">
            Panel de <span className="text-degradado">gestión</span>
          </h2>
          <p className="mt-3 text-slate-300">
            Administra usuarios y gastos. Conectado a{" "}
            <code className="rounded bg-white/10 px-2 py-0.5 text-fuchsia-200">{API_URL}</code>
          </p>
        </div>

        {/* Pestañas */}
        <div className="mt-10 flex justify-center gap-3">
          {pestanas.map(({ clave, etiqueta, icono: Icono }) => (
            <button
              key={clave}
              onClick={() => setActiva(clave)}
              className={
                activa === clave
                  ? "btn-marca px-6"
                  : "btn-ghost px-6"
              }
            >
              <Icono className="h-4 w-4" /> {etiqueta}
            </button>
          ))}
        </div>

        <div className="mt-10">
          <CrudPanel
            key={actual.clave}
            api={actual.api}
            campos={actual.campos}
            titulo={actual.titulo}
          />
        </div>
      </div>
    </section>
  );
}

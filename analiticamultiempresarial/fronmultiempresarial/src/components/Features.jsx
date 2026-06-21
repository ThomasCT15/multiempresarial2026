import { Users, Wallet, BarChart3, ShieldCheck, Filter, RefreshCw } from "lucide-react";

const caracteristicas = [
  {
    icono: Users,
    titulo: "Gestión de usuarios",
    texto: "CRUD completo de usuarios: crear, listar, editar y eliminar en segundos.",
  },
  {
    icono: Wallet,
    titulo: "Control de gastos",
    texto: "Registra y administra los gastos con fecha, monto y descripción.",
  },
  {
    icono: BarChart3,
    titulo: "Analítica con Python",
    texto: "Datos limpios y transformados con pandas (query y groupby) listos para analizar.",
  },
  {
    icono: Filter,
    titulo: "Limpieza de datos",
    texto: "Rutinas que validan textos, números y fechas para un análisis de calidad.",
  },
  {
    icono: ShieldCheck,
    titulo: "API segura y abierta",
    texto: "Backend Spring Boot con CORS habilitado para cualquier cliente.",
  },
  {
    icono: RefreshCw,
    titulo: "Tiempo real",
    texto: "El frontend se sincroniza con la base de datos a través de la API REST.",
  },
];

export default function Features() {
  return (
    <section id="caracteristicas" className="relative py-24">
      <div className="mx-auto max-w-6xl px-6">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="font-display text-4xl font-bold tracking-tight">
            Todo lo que tu negocio <span className="text-degradado">necesita</span>
          </h2>
          <p className="mt-4 text-slate-300">
            Una solución integral que une ciencia de datos y gestión empresarial.
          </p>
        </div>

        <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {caracteristicas.map(({ icono: Icono, titulo, texto }) => (
            <article
              key={titulo}
              className="group glass rounded-2xl p-6 transition hover:-translate-y-1 hover:border-fuchsia-400/30"
            >
              <span className="grid h-12 w-12 place-items-center rounded-xl bg-gradient-to-br from-purple-500/80 to-fuchsia-600/80 shadow-lg shadow-purple-900/40">
                <Icono className="h-6 w-6 text-white" />
              </span>
              <h3 className="mt-5 font-display text-xl font-semibold">{titulo}</h3>
              <p className="mt-2 text-sm leading-relaxed text-slate-300">{texto}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

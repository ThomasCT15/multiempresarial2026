import { Sparkles, ArrowRight, Database } from "lucide-react";

export default function Hero() {
  return (
    <section id="inicio" className="relative overflow-hidden pt-36 pb-24">
      {/* Blobs morados difuminados de fondo */}
      <div className="pointer-events-none absolute inset-0 -z-10">
        <div className="absolute -left-20 top-10 h-72 w-72 animate-blob rounded-full bg-purple-600/30 blur-3xl" />
        <div className="absolute right-0 top-0 h-80 w-80 animate-blob rounded-full bg-fuchsia-500/30 blur-3xl [animation-delay:2s]" />
        <div className="absolute bottom-0 left-1/3 h-72 w-72 animate-blob rounded-full bg-indigo-600/30 blur-3xl [animation-delay:4s]" />
      </div>

      <div className="mx-auto grid max-w-6xl items-center gap-12 px-6 md:grid-cols-2">
        <div>
          <span className="inline-flex items-center gap-2 rounded-full glass px-4 py-1.5 text-sm text-fuchsia-200">
            <Sparkles className="h-4 w-4" />
            Analítica de datos empresarial
          </span>

          <h1 className="mt-6 font-display text-5xl font-extrabold leading-tight tracking-tight md:text-6xl">
            Decisiones <span className="text-degradado">inteligentes</span> con tus datos
          </h1>

          <p className="mt-5 max-w-md text-lg text-slate-300">
            Plataforma para simular, limpiar, transformar y gestionar la información de
            <span className="font-semibold text-white"> usuarios </span> y
            <span className="font-semibold text-white"> gastos</span>. Todo conectado en tiempo real con tu backend.
          </p>

          <div className="mt-8 flex flex-wrap items-center gap-4">
            <a href="#gestion" className="btn-marca">
              Gestionar datos <ArrowRight className="h-4 w-4" />
            </a>
            <a href="#caracteristicas" className="btn-ghost">
              <Database className="h-4 w-4" /> Ver características
            </a>
          </div>

          <div className="mt-10 flex gap-8">
            <Stat valor="2" etiqueta="Módulos CRUD" />
            <Stat valor="100%" etiqueta="API REST" />
            <Stat valor="∞" etiqueta="Clientes (CORS)" />
          </div>
        </div>

        {/* Imagen asociada con marco de vidrio */}
        <div className="relative">
          <div className="absolute -inset-4 -z-10 rounded-3xl bg-gradient-to-tr from-purple-600/40 to-fuchsia-500/40 blur-2xl" />
          <div className="animate-floaty overflow-hidden rounded-3xl glass p-2">
            <img
              src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80"
              alt="Dashboard de analítica de datos"
              className="h-full w-full rounded-2xl object-cover"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </section>
  );
}

function Stat({ valor, etiqueta }) {
  return (
    <div>
      <p className="font-display text-3xl font-bold text-degradado">{valor}</p>
      <p className="text-sm text-slate-400">{etiqueta}</p>
    </div>
  );
}

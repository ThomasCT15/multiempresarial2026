import { BarChart3 } from "lucide-react";

export default function Navbar() {
  return (
    <header className="fixed inset-x-0 top-0 z-50">
      <nav className="mx-auto mt-4 flex max-w-6xl items-center justify-between rounded-2xl glass px-5 py-3">
        <a href="#inicio" className="flex items-center gap-2">
          <span className="grid h-9 w-9 place-items-center rounded-xl bg-gradient-to-br from-purple-500 to-fuchsia-600 shadow-lg shadow-purple-900/40">
            <BarChart3 className="h-5 w-5 text-white" />
          </span>
          <span className="font-display text-lg font-bold tracking-tight">
            Multi<span className="text-degradado">empresarial</span>
          </span>
        </a>

        <ul className="hidden items-center gap-8 text-sm font-medium text-slate-300 md:flex">
          <li><a href="#inicio" className="transition hover:text-white">Inicio</a></li>
          <li><a href="#caracteristicas" className="transition hover:text-white">Características</a></li>
          <li><a href="#gestion" className="transition hover:text-white">Gestión</a></li>
          <li><a href="#dashboard" className="transition hover:text-white">Dashboard</a></li>
        </ul>

        <a href="#gestion" className="btn-marca px-4 py-2 text-sm">
          Ir al panel
        </a>
      </nav>
    </header>
  );
}

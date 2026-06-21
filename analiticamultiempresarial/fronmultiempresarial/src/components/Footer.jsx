import { BarChart3 } from "lucide-react";

export default function Footer() {
  return (
    <footer className="border-t border-white/10 py-10">
      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-6 text-sm text-slate-400 sm:flex-row">
        <div className="flex items-center gap-2">
          <span className="grid h-8 w-8 place-items-center rounded-lg bg-gradient-to-br from-purple-500 to-fuchsia-600">
            <BarChart3 className="h-4 w-4 text-white" />
          </span>
          <span className="font-display font-semibold text-slate-200">Multiempresarial</span>
        </div>
        <p>Hecho con React + Tailwind · Analítica con Python · API Spring Boot</p>
      </div>
    </footer>
  );
}

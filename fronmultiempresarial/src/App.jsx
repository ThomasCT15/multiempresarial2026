import Navbar from "./components/Navbar.jsx";
import Hero from "./components/Hero.jsx";
import Features from "./components/Features.jsx";
import GestionCrud from "./components/GestionCrud.jsx";
import Footer from "./components/Footer.jsx";

export default function App() {
  return (
    <div className="relative min-h-screen overflow-x-hidden">
      {/* Fondo con degradado morado general */}
      <div className="pointer-events-none fixed inset-0 -z-20 bg-gradient-to-b from-slate-950 via-[#1a0b2e] to-slate-950" />

      <Navbar />
      <main>
        <Hero />
        <Features />
        <GestionCrud />
      </main>
      <Footer />
    </div>
  );
}

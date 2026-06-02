package com.multiempresarial.backend.config;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.multiempresarial.backend.model.Gasto;
import com.multiempresarial.backend.model.Usuario;
import com.multiempresarial.backend.repository.GastoRepository;
import com.multiempresarial.backend.repository.UsuarioRepository;

/**
 * Precarga de datos: al arrancar la aplicacion inserta 500 usuarios y 500 gastos.
 *
 * Implementa CommandLineRunner, asi que el metodo run() se ejecuta UNA VEZ
 * justo despues de que el backend termina de levantar.
 *
 * Solo carga si la tabla esta vacia (para no duplicar datos en cada reinicio).
 * Las "semillas" son las mismas del simulador de Python, para que sea coherente.
 */
@Component
public class CargaDatosInicial implements CommandLineRunner {

    private final UsuarioRepository usuarioRepository;
    private final GastoRepository gastoRepository;

    public CargaDatosInicial(UsuarioRepository usuarioRepository, GastoRepository gastoRepository) {
        this.usuarioRepository = usuarioRepository;
        this.gastoRepository = gastoRepository;
    }

    @Override
    public void run(String... args) {
        // random con semilla fija -> siempre genera los mismos datos (util para clase)
        Random random = new Random(42);

        if (usuarioRepository.count() == 0) {
            cargarUsuarios(random);
            System.out.println(">> Precargados 500 usuarios.");
        }

        if (gastoRepository.count() == 0) {
            cargarGastos(random);
            System.out.println(">> Precargados 500 gastos.");
        }
    }

    private void cargarUsuarios(Random random) {
        String[] nombres = {
                "Pedro Perez", "Fernanda Fernandez", "Rocio Rua", "Juan Jimenez", "Carlos Cuesta",
                "Maria Martinez", "Luisa Lopez", "Gaston Galeano", "Laura Lopez", "Miguel Montoya"
        };
        String[] contrasenas = {
                "admin123", "admin987", "user123", "user987", "person123",
                "person987", "gap123", "gap987", "love123", "love987"
        };
        int[] edades = {20, 19, 22, 24, 25, 30, 29, 37, 40, 65};
        String[] correos = {
                "jl@correo.com", "ad@correo.com", "lu@correo.com", "km@correo.com", "ju@correo.com",
                "yu@correo.com", "hr@correo.com", "ew@correo.com", "gb@correo.com", "mm@correo.com"
        };

        List<Usuario> usuarios = new ArrayList<>();
        for (int i = 0; i < 500; i++) {
            Usuario usuario = new Usuario(
                    nombres[random.nextInt(nombres.length)],
                    contrasenas[random.nextInt(contrasenas.length)],
                    edades[random.nextInt(edades.length)],
                    correos[random.nextInt(correos.length)]
            );
            usuarios.add(usuario);
        }
        // saveAll inserta toda la lista de una vez (mas eficiente que uno por uno)
        usuarioRepository.saveAll(usuarios);
    }

    private void cargarGastos(Random random) {
        String[] descripciones = {
                "transporte", "comida", "arriendo", "servicios", "entretenimiento",
                "salud", "educacion", "ropa", "mercado", "otros"
        };

        List<Gasto> gastos = new ArrayList<>();
        for (int i = 0; i < 500; i++) {
            // fecha aleatoria del anio 2026
            LocalDate fecha = LocalDate.of(2026, 1, 1).plusDays(random.nextInt(365));
            // monto aleatorio entre 1.000 y 500.000
            double monto = 1000 + random.nextInt(499001);
            String descripcion = descripciones[random.nextInt(descripciones.length)];

            gastos.add(new Gasto(fecha, monto, descripcion));
        }
        gastoRepository.saveAll(gastos);
    }
}

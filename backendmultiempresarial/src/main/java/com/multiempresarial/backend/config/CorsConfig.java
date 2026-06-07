package com.multiempresarial.backend.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * CORS generico: habilita el acceso desde CUALQUIER cliente (origen),
 * con cualquier metodo (GET, POST, PUT, DELETE...) y cualquier cabecera.
 *
 * Asi cualquier front-end (React, Angular, un .html, Postman, etc.)
 * puede consumir esta API sin ser bloqueado por el navegador.
 */
@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")          // aplica a todas las rutas
                .allowedOrigins("*")        // cualquier cliente / dominio
                .allowedMethods("*")        // todos los metodos HTTP
                .allowedHeaders("*");       // todas las cabeceras
    }
}

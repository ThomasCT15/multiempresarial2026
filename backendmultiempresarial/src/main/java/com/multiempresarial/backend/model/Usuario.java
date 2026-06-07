package com.multiempresarial.backend.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * Entidad Usuario -> tabla "usuarios".
 * Campos basados en el set de datos de Python: id, nombres, contrasena, edad, correo.
 */
@Entity
@Table(name = "usuarios")
public class Usuario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String nombres;

    // Se evita la "n" con tilde en el codigo Java; en BD la columna se llama "contrasena"
    @Column(name = "contrasena", nullable = false)
    private String contrasena;

    private Integer edad;

    @Column(nullable = false)
    private String correo;

    public Usuario() {
    }

    public Usuario(String nombres, String contrasena, Integer edad, String correo) {
        this.nombres = nombres;
        this.contrasena = contrasena;
        this.edad = edad;
        this.correo = correo;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    public String getContrasena() {
        return contrasena;
    }

    public void setContrasena(String contrasena) {
        this.contrasena = contrasena;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }
}

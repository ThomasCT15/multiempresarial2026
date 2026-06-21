package com.multiempresarial.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.multiempresarial.backend.model.Usuario;

/**
 * Repositorio de Usuario.
 * Al heredar de JpaRepository ya tenemos gratis: save, findById, findAll, deleteById...
 */
@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
}

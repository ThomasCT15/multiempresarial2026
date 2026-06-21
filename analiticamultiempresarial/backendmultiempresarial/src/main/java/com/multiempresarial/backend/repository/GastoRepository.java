package com.multiempresarial.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.multiempresarial.backend.model.Gasto;

/**
 * Repositorio de Gasto.
 * Al heredar de JpaRepository ya tenemos gratis: save, findById, findAll, deleteById...
 */
@Repository
public interface GastoRepository extends JpaRepository<Gasto, Long> {
}

package com.multiempresarial.backend.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.multiempresarial.backend.model.Gasto;
import com.multiempresarial.backend.repository.GastoRepository;

/**
 * Capa de servicio de Gasto: contiene la logica del negocio
 * y habla con el repositorio. El controlador NUNCA usa el repositorio directo.
 */
@Service
public class GastoService {

    private final GastoRepository gastoRepository;

    public GastoService(GastoRepository gastoRepository) {
        this.gastoRepository = gastoRepository;
    }

    // READ: listar todos
    public List<Gasto> listar() {
        return gastoRepository.findAll();
    }

    // READ: buscar uno por id
    public Optional<Gasto> buscarPorId(Long id) {
        return gastoRepository.findById(id);
    }

    // CREATE: guardar uno nuevo
    public Gasto crear(Gasto gasto) {
        return gastoRepository.save(gasto);
    }

    // UPDATE: actualizar uno existente
    public Optional<Gasto> actualizar(Long id, Gasto datos) {
        return gastoRepository.findById(id).map(gasto -> {
            gasto.setFecha(datos.getFecha());
            gasto.setMonto(datos.getMonto());
            gasto.setDescripcion(datos.getDescripcion());
            return gastoRepository.save(gasto);
        });
    }

    // DELETE: eliminar por id (retorna true si existia)
    public boolean eliminar(Long id) {
        if (gastoRepository.existsById(id)) {
            gastoRepository.deleteById(id);
            return true;
        }
        return false;
    }
}

package com.multiempresarial.backend.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.multiempresarial.backend.model.Gasto;
import com.multiempresarial.backend.service.GastoService;

/**
 * CRUD REST de Gasto.
 * Rutas base: /api/gastos
 *
 * @CrossOrigin("*") refuerza el CORS generico tambien a nivel de controlador.
 */
@RestController
@RequestMapping("/api/gastos")
@CrossOrigin(origins = "*")
public class GastoController {

    private final GastoService gastoService;

    public GastoController(GastoService gastoService) {
        this.gastoService = gastoService;
    }

    // GET /api/gastos  -> listar todos
    @GetMapping
    public List<Gasto> listar() {
        return gastoService.listar();
    }

    // GET /api/gastos/{id}  -> buscar por id
    @GetMapping("/{id}")
    public ResponseEntity<Gasto> buscarPorId(@PathVariable Long id) {
        return gastoService.buscarPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // POST /api/gastos  -> crear
    @PostMapping
    public ResponseEntity<Gasto> crear(@RequestBody Gasto gasto) {
        Gasto creado = gastoService.crear(gasto);
        return ResponseEntity.status(HttpStatus.CREATED).body(creado);
    }

    // PUT /api/gastos/{id}  -> actualizar
    @PutMapping("/{id}")
    public ResponseEntity<Gasto> actualizar(@PathVariable Long id, @RequestBody Gasto gasto) {
        return gastoService.actualizar(id, gasto)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // DELETE /api/gastos/{id}  -> eliminar
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (gastoService.eliminar(id)) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}

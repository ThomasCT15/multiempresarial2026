package com.multiempresarial.backend.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.multiempresarial.backend.model.Usuario;
import com.multiempresarial.backend.repository.UsuarioRepository;

/**
 * Capa de servicio de Usuario: contiene la logica del negocio
 * y habla con el repositorio. El controlador NUNCA usa el repositorio directo.
 */
@Service
public class UsuarioService {

    private final UsuarioRepository usuarioRepository;

    public UsuarioService(UsuarioRepository usuarioRepository) {
        this.usuarioRepository = usuarioRepository;
    }

    // READ: listar todos
    public List<Usuario> listar() {
        return usuarioRepository.findAll();
    }

    // READ: buscar uno por id
    public Optional<Usuario> buscarPorId(Long id) {
        return usuarioRepository.findById(id);
    }

    // CREATE: guardar uno nuevo
    public Usuario crear(Usuario usuario) {
        return usuarioRepository.save(usuario);
    }

    // UPDATE: actualizar uno existente
    public Optional<Usuario> actualizar(Long id, Usuario datos) {
        return usuarioRepository.findById(id).map(usuario -> {
            usuario.setNombres(datos.getNombres());
            usuario.setContrasena(datos.getContrasena());
            usuario.setEdad(datos.getEdad());
            usuario.setCorreo(datos.getCorreo());
            return usuarioRepository.save(usuario);
        });
    }

    // DELETE: eliminar por id (retorna true si existia)
    public boolean eliminar(Long id) {
        if (usuarioRepository.existsById(id)) {
            usuarioRepository.deleteById(id);
            return true;
        }
        return false;
    }
}

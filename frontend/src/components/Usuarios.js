import React, { useState, useEffect } from 'react';
import './Usuarios.css';

const Usuarios = () => {
  const [usuarios, setUsuarios] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/usuarios/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setUsuarios(data);
        setIsLoading(false);
      })
      .catch(error => {
        console.error("Error al obtener los usuarios:", error);
        setError('Failed to load user data');
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return <div className="loading">Cargando...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  // Ordenar los usuarios por nombre
  const usuariosOrdenados = [...usuarios].sort((a, b) => a.nombre.localeCompare(b.nombre));

  return (
    <div className="usuarios-container">
      <h1>Usuarios y sus Equipos</h1>
      <table className="usuarios-table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Equipo (Número)</th>
          </tr>
        </thead>
        <tbody>
          {usuariosOrdenados.map((usuario, index) => (
            <tr key={index}>
              <td>{usuario.nombre}</td>
              <td>{usuario.equipo.numero}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Usuarios;

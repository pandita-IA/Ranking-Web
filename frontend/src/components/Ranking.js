import React, { useState, useEffect } from 'react';
import './Ranking.css';

const EpicRanking = () => {
  const [ranking, setRanking] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/ranking/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // Sort the ranking by total_score (puntaje_total) in descending order
        const sortedData = data.sort((a, b) => b.puntaje_total - a.puntaje_total);
        setRanking(sortedData);
        setIsLoading(false);
      })
      .catch(error => {
        console.error("Error fetching the ranking:", error);
        setError('Failed to load ranking data');
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return <div className="loading">Loading the Hall of Champions...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="epic-ranking-container">
      <header className="epic-header">
        <h1 className="epic-title">Hall of Champions</h1>
      </header>
      <main className="epic-main">
        <table className="epic-table">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Team</th>
              <th>Exercise</th>
              <th>Total Score</th>
              <th>Champions</th>
            </tr>
          </thead>
          <tbody>
            {ranking.map((item, index) => (
              <tr key={index} className="epic-row" style={{animationDelay: `${index * 0.1}s`}}>
                <td className="epic-rank">
                  <span className="rank-number">{index + 1}</span>
                  {index < 3 && <span className={`trophy trophy-${index + 1}`}></span>}
                </td>
                <td>{item.equipo_numero}</td>
                <td>
                  {/* Mostrar todos los ejercicios resueltos */}
                  {item.ejercicios_resueltos.map((ejercicio, idx) => (
                    <div key={idx}>
                      <span>{ejercicio.ejercicio}</span>
                    </div>
                  ))}
                </td>
                <td className="epic-score">{item.puntaje_total}</td>
                <td>
                  <ul className="champions-list">
                    {item.integrantes.map((integrante, idx) => (
                      <li key={idx} className="champion-name" style={{animationDelay: `${(index * 0.1) + (idx * 0.05)}s`}}>{integrante}</li>
                    ))}
                  </ul>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </div>
  );
};

export default EpicRanking;

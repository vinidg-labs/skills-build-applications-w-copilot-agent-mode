import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [modalData, setModalData] = useState(null);
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;  
  const baseUrl = codespaceName  
    ? `https://${codespaceName}-8000.app.github.dev`  
    : 'http://localhost:8000';  
  const endpoint = `${baseUrl}/api/teams/`;

  useEffect(() => {
    console.log('Fetching Teams from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched Teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err))
      .finally(() => setLoading(false));
  }, [endpoint]);

  if (loading) return <div className="text-center my-4">Carregando equipes...</div>;

  const handleShowModal = (team) => {
    setModalData(team);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setModalData(null);
  };

  return (
    <>
      <div className="card mb-4">
        <div className="card-header bg-warning text-dark">
          <h2 className="h4 mb-0">Equipes</h2>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Nome</th>
                  <th>Detalhes</th>
                </tr>
              </thead>
              <tbody>
                {teams.map((team, idx) => (
                  <tr key={team.id || idx}>
                    <td>{team.id || idx + 1}</td>
                    <td>{team.name || '-'}</td>
                    <td>
                      <button className="btn btn-outline-info btn-sm" onClick={() => handleShowModal(team)}>
                        <i className="bi bi-eye"></i> Ver detalhes
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Modal Bootstrap */}
      {showModal && (
        <>
          <div className="modal fade show" style={{display:'block'}} tabIndex="-1" role="dialog">
            <div className="modal-dialog modal-dialog-centered" role="document">
              <div className="modal-content">
                <div className="modal-header bg-warning text-dark">
                  <h5 className="modal-title">Detalhes da Equipe</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={handleCloseModal}></button>
                </div>
                <div className="modal-body">
                  <pre style={{whiteSpace:'pre-wrap', wordBreak:'break-word'}}>{JSON.stringify(modalData, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={handleCloseModal}>Fechar</button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show" style={{zIndex:1040}} onClick={handleCloseModal}></div>
        </>
      )}
    </>
  );
};

export default Teams;

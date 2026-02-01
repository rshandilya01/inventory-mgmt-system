import React from "react";

function ServerList({ servers }) {
  if (servers.length === 0) return <p>No results</p>;

  return (
    <table border="1" cellPadding="5">
      <thead>
        <tr>
          <th>Server Name</th>
          <th>IP</th>
          <th>Owner</th>
          <th>License Expiry</th>
          <th>Application</th>
          <th>Database</th>
          <th>Purpose</th>
          <th>Environment</th>
        </tr>
      </thead>
      <tbody>
        {servers.map((s) => (
          <tr key={s.id}>
            <td>{s.server_name}</td>
            <td>{s.ip}</td>
            <td>{s.owner}</td>
            <td>{s.license_expiry}</td>
            <td>{s.application}</td>
            <td>{s.database}</td>
            <td>{s.purpose}</td>
            <td>{s.environment}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ServerList;

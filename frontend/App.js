import React, { useState } from "react";
import Login from "./Login";
import SearchBar from "./SearchBar";
import ServerList from "./ServerList";

function App() {
  const [token, setToken] = useState(null);
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleLogin = (token) => {
    setToken(token);
  };

  const handleSearch = async (query) => {
    setLoading(true);
    const res = await fetch(`/api/servers?query=${encodeURIComponent(query)}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await res.json();
    setSearchResults(data);
    setLoading(false);
  };

  if (!token) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <div>
      <h1>Inventory Management System</h1>
      <SearchBar onSearch={handleSearch} />
      {loading ? <p>Loading...</p> : <ServerList servers={searchResults} />}
    </div>
  );
}

export default App;

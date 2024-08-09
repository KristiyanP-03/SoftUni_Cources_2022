import { useState } from 'react';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [username, setUsername] = useState('');
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState('');
  const [newPrice, setNewPrice] = useState('');
  const [newCategory, setNewCategory] = useState('buy');

  function handleLogin() {
    if (username.trim()) {
      setIsAuthenticated(true);
    }
  }

  function handleLogout() {
    setIsAuthenticated(false);
    setUsername('');
  }

  function addItem() {
    if (newItem.trim() && newPrice.trim()) {
      setItems(items.concat({ name: newItem, price: newPrice, category: newCategory }));
      setNewItem('');
      setNewPrice('');
    }
  }

  function handleUsernameChange(event) {
    setUsername(event.target.value);
  }

  function handleNewItemChange(event) {
    setNewItem(event.target.value);
  }

  function handleNewPriceChange(event) {
    setNewPrice(event.target.value);
  }

  function handleNewCategoryChange(event) {
    setNewCategory(event.target.value);
  }

  return (
    <div className="app">
      <h1>Marketplace</h1>

      {!isAuthenticated ? (
        <div className="login-form">
          <input
            type="text"
            placeholder="Enter your username"
            value={username}
            onChange={handleUsernameChange}
          />
          <button onClick={handleLogin}>Login</button>
        </div>
      ) : (
        <>
          <div className="logout-section">
            <p>Welcome, {username}!</p>
            <button onClick={handleLogout}>Logout</button>
          </div>

          <div className="form">
            <input
              type="text"
              placeholder="Item name"
              value={newItem}
              onChange={handleNewItemChange}
            />
            <input
              type="text"
              placeholder="Price"
              value={newPrice}
              onChange={handleNewPriceChange}
            />
            <select
              value={newCategory}
              onChange={handleNewCategoryChange}
            >
              <option value="buy">Buy</option>
              <option value="sell">Sell</option>
            </select>
            <button onClick={addItem}>Add Item</button>
          </div>

          <div className="item-list">
            <h2>Items List</h2>
            {items.length === 0 ? (
              <p>No items listed yet.</p>
            ) : (
              items.map(function(item, index) {
                return (
                  <div key={index} className={`item ${item.category}`}>
                    <span>{item.name}</span>
                    <span>${item.price}</span>
                    <span>({item.category})</span>
                  </div>
                );
              })
            )}
          </div>
        </>
      )}
    </div>
  );
}

export default App;

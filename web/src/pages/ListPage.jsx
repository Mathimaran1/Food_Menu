import { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '../components/Card';

function ListPage() {
  const [categories, setCategories] = useState([]);
  const [menuItems, setMenuItems] = useState([]);
  const [currentCategory, setCurrentCategory] = useState('all');
  const [searchIdInput, setSearchIdInput] = useState('');

  useEffect(() => {
    const fetchCategories = async () => {
      const response = await axios.get('http://localhost:8000/categories');
      setCategories(response.data);
    };
    fetchCategories();
  }, []);

  useEffect(() => {
    const fetchItems = async () => {
      if (currentCategory === 'all') {
        const response = await axios.get('http://localhost:8000/menu');
        setMenuItems(response.data);
      } else {
        const response = await axios.get(`http://localhost:8000/menu/category/${currentCategory}`);
        setMenuItems(response.data);
      }
    };
    fetchItems();
  }, [currentCategory]);

  const handleSearchById = async () => {
    if (!searchIdInput) return;
    try {
      const response = await axios.get(`http://localhost:8000/menu/${searchIdInput}`);
      const itemData = response.data;

      if (currentCategory !== 'all') {
        const categoryData = categories.find(c => String(c.id) === String(currentCategory));
        
        if (categoryData && itemData.category !== categoryData.name) {
           alert(`Oops! This item belongs to the '${itemData.category}' menu, not '${categoryData.name}'. Please click the '${itemData.category}' tab or 'All Items' to search for it!`);
           setMenuItems([]);
           return;
        }
      }

      setMenuItems([itemData]);
    } catch (error) {
      alert("Item not found!");
      setMenuItems([]);
    }
  };

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
        <h1>Our Menu</h1>
        
        <div>
          <input 
            type="text" 
            placeholder="Enter ID..." 
            value={searchIdInput}
            onChange={(e) => setSearchIdInput(e.target.value)}
            style={{ padding: '8px', borderRadius: '10px', marginRight: '5px' }}
          />
          <button onClick={handleSearchById} style={{ padding: '8px 15px', borderRadius: '10px' }}>
            Search ID
          </button>
        </div>
      </div>

      <div className="tabs-container">
        <button 
          className={currentCategory === 'all' ? 'tab-button active' : 'tab-button'}
          onClick={() => setCurrentCategory('all')}
        >
          All Items
        </button>
        
        {categories.map((cat) => (
          <button 
            key={cat.id} 
            className={currentCategory === cat.id ? 'tab-button active' : 'tab-button'}
            onClick={() => setCurrentCategory(cat.id)}
          >
            {cat.name}
          </button>
        ))}
      </div>
      <hr />

      <ul className="simple-grid">
        {menuItems.map((item) => (
          <Card key={item.id} item={item} />
        ))}
      </ul>
    </div>
  );
}

export default ListPage;

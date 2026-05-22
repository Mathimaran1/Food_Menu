import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="container" style={{ marginBottom: '30px' }}>
      <Link to="/menu" style={{ textDecoration: 'none' }}>
        <h2 style={{ margin: 0, color: '#e63946' }}>🍔 FoodieExpress</h2>
      </Link>
      <div style={{ display: 'flex', gap: '20px' }}>
        <Link to="/menu" style={{ textDecoration: 'none', color: '#e63946', fontWeight: 'bold' }}>Menu</Link>
      </div>
    </nav>
  );
}

export default Navbar;

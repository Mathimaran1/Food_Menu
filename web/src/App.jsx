import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import ListPage from './pages/ListPage';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <main className="container">
          <Routes>
            <Route path="/" element={<Navigate to="/menu" replace />} />
            <Route path="/menu" element={<ListPage />} />
            {/* Fallback route */}
            <Route path="*" element={<Navigate to="/menu" replace />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

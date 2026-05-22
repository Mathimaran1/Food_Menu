function Card({ item }) {
  return (
    <li className="simple-card" style={{ padding: '20px', color: '#000' }}>
      <div style={{ flex: 1 }}>
        {/* Top Row: ID and Tags */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px', gap: '10px' }}>
          <p style={{ margin: 0, color: '#000', fontSize: '0.85rem', fontWeight: 'bold', wordBreak: 'break-word', flex: 1 }}>ID: {item.id}</p>
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexShrink: 0 }}>
            {item.veg !== undefined && (
              <span className="tag" style={{ margin: 0, color: '#000', backgroundColor: 'transparent', border: '1px solid #000', whiteSpace: 'nowrap', display: 'flex', alignItems: 'center' }}>
                {item.veg ? '🟢 Veg' : '🔴 Non-Veg'}
              </span>
            )}
            {item.spicy && (
              <span title="Spicy" style={{ fontSize: '1.2rem', display: 'flex', alignItems: 'center' }}>🌶️</span>
            )}
          </div>
        </div>
        
        {/* Dish Name */}
        <h3 style={{ margin: '0 0 10px 0', color: '#000' }}>{item.name}</h3>

        {/* Description */}
        <p style={{ margin: '0 0 15px 0', color: '#000', fontSize: '0.95rem', lineHeight: '1.5' }}>
          {item.description || 'No description available for this item.'}
        </p>
      </div>
        
      {/* Price & Rating */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 'auto', paddingTop: '15px' }}>
        <span className="price" style={{ color: '#000' }}>${Number(item.price).toFixed(2)}</span>
        {item.rating && (
          <span style={{ fontWeight: 'bold', color: '#000' }}>⭐ {item.rating}</span>
        )}
      </div>
    </li>
  );
}

export default Card;

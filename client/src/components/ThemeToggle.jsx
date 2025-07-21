import React from 'react';

const ThemeToggle = ({ toggleTheme, isDarkMode }) => {
  return (
    <button onClick={toggleTheme} style={{ marginLeft: '1rem' }}>
      {isDarkMode ? '🌞 Light Mode' : '🌙 Dark Mode'}
    </button>
  );
};

export default ThemeToggle;
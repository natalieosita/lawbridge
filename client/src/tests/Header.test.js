import { render, screen } from '@testing-library/react';
import Header from '../components/Header';
import { BrowserRouter } from 'react-router-dom';

describe('Header component', () => {
  test('renders navigation links', () => {
    render(
      <BrowserRouter>
        <Header toggleTheme={() => {}} isDarkMode={false} />
      </BrowserRouter>
    );

    expect(screen.getByText(/Cases/i)).toBeInTheDocument();
    expect(screen.getByText(/Login/i)).toBeInTheDocument();
    expect(screen.getByText(/Register/i)).toBeInTheDocument();
    expect(screen.getByText(/Dark Mode/i)).toBeInTheDocument();
  });

  test('theme toggle updates text', () => {
    render(
      <BrowserRouter>
        <Header toggleTheme={() => {}} isDarkMode={true} />
      </BrowserRouter>
    );

    expect(screen.getByText(/Light Mode/i)).toBeInTheDocument();
  });
});
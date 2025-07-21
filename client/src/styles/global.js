import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background-color: ${({ theme }) => theme.colors.background};
    color: ${({ theme }) => theme.colors.text};
    transition: background-color 0.3s ease, color 0.3s ease;
  }

  * {
    box-sizing: border-box;
  }

  a {
    color: ${({ theme }) => theme.colors.link};
    text-decoration: none;
  }

  button {
    font-family: inherit;
  }
`;

export default GlobalStyle;
import React from 'react';
import styled from 'styled-components';

const Container = styled.footer`
  padding: 1rem;
  background: ${({ theme }) => theme.colors.primary};
  color: white;
  text-align: center;
`;

const Footer = () => (
  <Container>
    <small>© {new Date().getFullYear()} LawBridge Kenya. All rights reserved.</small>
  </Container>
);

export default Footer;
import React from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer';

const Container = styled.div`
  padding: 3rem 2rem;
  text-align: center;
`;

const Home = () => (
  <>
    <Container>
      <h1>Welcome to LawBridge</h1>
      <p>Your gateway to legal support across Kenya</p>
      <a href="/cases" style={{ background: '#0b5ed7', color: 'white', padding: '0.5rem 1rem', borderRadius: '4px' }}>
        Explore Cases
      </a>
    </Container>
    <Footer />
  </>
);

export default Home;
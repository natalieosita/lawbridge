import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import Footer from '../components/Footer';

const Container = styled.div`
  padding: 4rem 2rem;
  text-align: center;
  background-color: ${({ theme }) => theme.colors.background};
  color: ${({ theme }) => theme.colors.text};
`;

const HeroImage = styled.img`
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
`;

const Title = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 1rem;
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
  max-width: 600px;
  margin: 0 auto 2rem;
`;

const CTA = styled.div`
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
`;

const Button = styled(Link)`
  background-color: ${({ theme }) => theme.colors.primary};
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  transition: background 0.3s ease;

  &:hover {
    background-color: ${({ theme }) => theme.colors.secondary};
  }
`;

const Home = () => (
  <>
    <Container>
      <HeroImage src="/assets/hero.jpg" alt="LawBridge hero" />
      <Title>Welcome to LawBridge</Title>
      <Subtitle>
        LawBridge is a secure platform that helps Kenyans access, manage, and track legal cases online.
        Whether you're seeking justice, legal support, or simply organizing your case records — LawBridge
        empowers you with clarity, privacy, and control.
      </Subtitle>
      <CTA>
        <Button to="/register">Get Started</Button>
        <Button to="/login">Already Registered?</Button>
      </CTA>
    </Container>
    <Footer />
  </>
);

export default Home;
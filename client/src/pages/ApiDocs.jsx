import React from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer';

const Container = styled.div`
  padding: 3rem 2rem;
  max-width: 900px;
  margin: 0 auto;
  color: ${({ theme }) => theme.colors.text};
`;

const Title = styled.h1`
  font-size: 2rem;
  margin-bottom: 1rem;
`;

const Endpoint = styled.div`
  margin-bottom: 2rem;
  padding: 1rem;
  border-left: 4px solid ${({ theme }) => theme.colors.primary};
  background-color: ${({ theme }) => theme.colors.background};
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
`;

const Method = styled.span`
  font-weight: bold;
  color: ${({ theme }) => theme.colors.primary};
`;

const Path = styled.code`
  background: ${({ theme }) => theme.colors.secondary};
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
`;

const Description = styled.p`
  margin: 0.5rem 0;
`;

const ApiDocs = () => (
  <>
    <Container>
      <Title>📡 LawBridge API Reference</Title>

      <Endpoint>
        <Method>POST</Method> <Path>/auth/register</Path>
        <Description>Registers a new user and returns a JWT token.</Description>
      </Endpoint>

      <Endpoint>
        <Method>POST</Method> <Path>/auth/login</Path>
        <Description>Authenticates a user and returns a JWT token.</Description>
      </Endpoint>

      <Endpoint>
        <Method>GET</Method> <Path>/cases</Path>
        <Description>Returns all cases for the authenticated user.</Description>
      </Endpoint>

      <Endpoint>
        <Method>POST</Method> <Path>/cases</Path>
        <Description>Creates a new case for the authenticated user.</Description>
      </Endpoint>

      <Endpoint>
        <Method>GET</Method> <Path>/health</Path>
        <Description>Returns server status for monitoring.</Description>
      </Endpoint>
    </Container>
    <Footer />
  </>
);

export default ApiDocs;
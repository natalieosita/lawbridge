import React from 'react';
import useFetchCases from '../api/useFetchCases';
import CaseForm from '../components/CaseForm';
import Loading from '../components/Loading';
import ErrorMessage from '../components/ErrorMessage';

const Cases = () => {
  const { data, error, isLoading } = useFetchCases();

  return (
    <div style={{ padding: '2rem' }}>
      <h2>My Cases</h2>
      <CaseForm />
      {isLoading && <Loading />}
      {error && <ErrorMessage message="Failed to load cases." />}
      <ul>
        {data?.map((item) => (
          <li key={item._id}><strong>{item.title}</strong>: {item.description}</li>
        ))}
      </ul>
    </div>
  );
};

export default Cases;
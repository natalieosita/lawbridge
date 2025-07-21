import React, { useState } from 'react';
import useCreateCase from '../api/useCreateCase';

const CaseForm = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const { mutate, isLoading, isError } = useCreateCase();

  const handleSubmit = (e) => {
    e.preventDefault();
    mutate({ title, description });
    setTitle('');
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
      <h2>Create a New Case</h2>
      {isError && <p style={{ color: 'red' }}>Error submitting case.</p>}
      <input
        type="text"
        placeholder="Case Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      /><br /><br />
      <textarea
        placeholder="Case Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        required
        rows={4}
        style={{ width: '100%' }}
      /><br /><br />
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Submitting...' : 'Submit Case'}
      </button>
    </form>
  );
};

export default CaseForm;
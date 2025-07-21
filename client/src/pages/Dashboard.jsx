import React from 'react';

const Dashboard = () => {
  const userToken = localStorage.getItem('token');

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Dashboard</h2>
      {userToken ? (
        <p>Welcome back! You’re logged in and can view secure data here.</p>
      ) : (
        <p>You must log in to see this page.</p>
      )}
    </div>
  );
};

export default Dashboard;
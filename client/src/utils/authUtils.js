const logoutUser = () => {
  localStorage.removeItem('token');
  window.location.href = '/login';
};

export default logoutUser;
import jwtDecode from 'jwt-decode';

const isTokenExpired = (token) => {
  try {
    const { exp } = jwtDecode(token);
    return exp * 1000 < Date.now();
  } catch {
    return true;
  }
};

export default isTokenExpired;
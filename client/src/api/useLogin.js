import { useMutation } from 'react-query';
import api from './client';

const useLogin = () =>
  useMutation((data) => api.post('/auth/login', data));

export default useLogin;
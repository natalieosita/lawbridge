import { useMutation } from 'react-query';
import api from './client';

const useRegister = () =>
  useMutation((data) => api.post('/auth/register', data));

export default useRegister;
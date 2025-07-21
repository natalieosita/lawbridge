import { useQuery } from 'react-query';
import api from './client';

const fetchCases = async () => {
  const response = await api.get('/cases');
  return response.data;
};

const useFetchCases = () => useQuery('cases', fetchCases);

export default useFetchCases;
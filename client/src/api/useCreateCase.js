import { useMutation, useQueryClient } from 'react-query';
import api from './client';

const useCreateCase = () => {
  const queryClient = useQueryClient();

  return useMutation(
    (data) => api.post('/cases', data),
    {
      onSuccess: () => queryClient.invalidateQueries('cases'),
    }
  );
};

export default useCreateCase;
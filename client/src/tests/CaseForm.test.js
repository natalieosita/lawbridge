import { render, screen, fireEvent } from '@testing-library/react';
import CaseForm from '../components/CaseForm';

jest.mock('../api/useCreateCase', () => () => ({
  mutate: jest.fn(),
  isLoading: false,
  isError: false
}));

describe('CaseForm component', () => {
  test('renders input fields and submit button', () => {
    render(<CaseForm />);
    expect(screen.getByPlaceholderText(/Case Title/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Case Description/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /submit case/i })).toBeInTheDocument();
  });

  test('submits form and resets fields', () => {
    render(<CaseForm />);
    fireEvent.change(screen.getByPlaceholderText(/Case Title/i), {
      target: { value: 'Test Case' }
    });
    fireEvent.change(screen.getByPlaceholderText(/Case Description/i), {
      target: { value: 'Description text' }
    });
    fireEvent.click(screen.getByRole('button'));

    // Can add assertions for cleared fields if mutate mocked to trigger success
  });
});
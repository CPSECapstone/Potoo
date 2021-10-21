import React from 'react';
import { render, screen } from '@testing-library/react';
import AdminPanel from './AdminPanel';

test('renders learn react link', () => {
  render(<AdminPanel />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

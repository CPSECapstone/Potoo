import React from 'react';
import { render, screen } from '@testing-library/react';
import AgentPanel from './AgentPanel';

test('renders learn react link', () => {
  render(<AgentPanel />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

import React from 'react';

import { Container } from './styles';

const Layout: React.FC = ({ children }) => {
  return <Container>{children}</Container>;
};

export default Layout;

import React from 'react';

import image from '../../assets/images/db-logo.png';
import {
  Container,
  Language,
  Logo,
  Title,
  Row,
  Column,
  Quantity
} from './styles';

const Header: React.FC = () => {
  return (
    <Container>
      <Row>
        <Column>
          <Logo src={image} alt="Dragon Ball Z" />
        </Column>
        <Column>
          <Title>Dragon Ball Z</Title>
          <Quantity>2,621,054 Miembros</Quantity>
          <Language>Español</Language>
        </Column>
      </Row>
    </Container>
  );
};

export default Header;

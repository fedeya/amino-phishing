import styled from '@emotion/styled';

export const Container = styled.header`
  padding: 2rem 1.5rem 1rem;
`;

export const Title = styled.h1`
  color: #fff;
  font-weight: bold;
  font-size: 2rem;
`;

export const Row = styled.div`
  display: flex;
  flex-direction: row;
`;

export const Column = styled.div`
  margin: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
`;

export const Quantity = styled.p`
  color: #fff;
  font-size: 16px;
  margin: 2px 0;
`;

export const Language = styled.p`
  color: white;
  background-color: rgba(200, 200, 200, 0.5);
  padding: 0.5rem;
  border-radius: 5px;
  font-size: 12px;
  margin: 2px 0;
`;

export const Logo = styled.img`
  width: 10rem;
  height: 10rem;
  border-radius: 2rem;
`;

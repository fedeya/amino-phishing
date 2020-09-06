import React from 'react';
import { Global, css } from '@emotion/core';

const GlobalStyles: React.FC = () => (
  <Global
    styles={css`
      *::after,
      *::before,
      * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
      }

      body {
        font-family: sans-serif;
        background-color: #222;
      }

      img {
        max-width: 100%;
      }
    `}
  />
);

export default GlobalStyles;

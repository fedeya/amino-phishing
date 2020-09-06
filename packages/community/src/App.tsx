import React from 'react';

import Layout from './components/Layout';
import Header from './components/Header';
import Global from './styles/global';

function App() {
  return (
    <>
      <Global />
      <Layout>
        <Header />
      </Layout>
    </>
  );
}

export default App;

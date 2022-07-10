import React from 'react';
import ReactDOM from 'react-dom/client';
import MainFunc from './common';
import {setApiBaseUrl} from './library';

// setApiBaseUrl("http://localhost:5504")

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <MainFunc />
);

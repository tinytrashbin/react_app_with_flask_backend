import {Header} from './header';
import React from 'react';
import Button from '@mui/material/Button';
import AcUnitIcon from '@mui/icons-material/AcUnit';

function Example3() {
  return (
    <div >
      <Header/>
      <Button variant="contained">Hello World</Button>;
      <div>
        Example3...
      </div>
      Icon = <AcUnitIcon/>
    </div>
  );
}

export default Example3;

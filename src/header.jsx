import './library.css';
import {Link} from "react-router-dom"
import React from 'react';

export function Header() {
  return (
    <div className="hsplit" >
      <div>
        <Link to="/example1">
          <div className="link_box" >Example1</div>
        </Link>
      </div>
      <div>
        <Link to="/example2">
          <div className="link_box" >Example2</div>
        </Link>
      </div>
      <div>
        <Link to="/example3">
          <div className="link_box" >Example3</div>
        </Link>
      </div>
    </div>
  );
}

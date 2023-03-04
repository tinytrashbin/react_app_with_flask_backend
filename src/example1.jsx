import './main.css';
import {Header} from './header';
import React from 'react';
import {api} from './library';


function Example1() {
  const [name, setName] = React.useState("A")

  React.useEffect(()=> {
    api("/my_name", {age: 60}, function(backend_output) {
      console.log(backend_output)
      setName(backend_output.name)
    })
  }, []);

  const new_name = function() {
    api("/new_name", {age: 61}, function(backend_output) {
      setName(backend_output.name)
    })
  }

  const try_signup = function() {
    api("/sign_up", {}, function(backend_output) {
      alert(JSON.stringify(backend_output))
    })
  }

  return (<>
    <Header/>
    <div className="top_box" >
      <h2>Example1</h2>
      <div>
        Name = {name}
      </div>
      <button onClick={() => new_name()} >Click for new name</button>
      <br/>
      <button onClick={() => try_signup()} >Try SignUp</button>
    </div>
  </>
  );
}

export default Example1;

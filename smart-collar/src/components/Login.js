import React, { useState } from 'react'
import axios from 'axios';
import './Login.css';

const Login = () => {

  const [usernameReg, setUsernameReg] = useState('');
  const [passwordReg, setPasswordReg] = useState('');

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

/*change localhost */
  const register = () => {
    axios.post('http://localhost3306/register', {
      username: usernameReg, 
      password: passwordReg
    }).then((response)=> {
        console.log(response);
    });
  };

/*change localhost */
  const loginFunc = () => {
    axios.post('http://localhost3306/login', {
      username: username, 
      password: password
    }).then((response)=> {
        if (response.data.message) {
          setLogInStatus(response.data.message);
        } else {
          setLogInStatus(response.data[0].username);
        }
    });
  };

  const [logInStatus, setLogInStatus] = useState('');

  return (
    <div> 
      <h4>Sign up if you dont have an account yet!</h4>
      <div className='registration'>
        <h2>Registration</h2>
        <p>
          <label>Username</label>
            <input class='input' type='text' 
                    onChange={(e)=> {setUsernameReg(e.target.value);
              }}  
            />
            <br></br>
          <label>Password</label>
          <input class='input' type='text' 
                  onChange={(e)=> {setPasswordReg(e.target.value);
              }}  
            />
            <br></br>
          <button class='button' onClick={register}> Register! </button>
        </p>
      </div>

      <br></br>
      <h4>Log in!</h4>
      <div className='Login'>
        <h2>Login</h2>
        <p>
          <label>Username</label>
            <input class='input' type='text'
                    placeholder='Username?'
                    onChange={(e) =>{
                        setUsername(e.target.value);
                    }}
            />
          <br></br>
          <label>Password</label>
          <input class='input' type='text'
                    placeholder='Password?'
                    onChange={(e) =>{
                        setPassword(e.target.value);
                    }}
            />
            <br></br>
          <button class='button' onClick={loginFunc}> Login! </button>
        </p>
      </div>
      <h3>{logInStatus}</h3>
    </div>
  );
}

export default Login;
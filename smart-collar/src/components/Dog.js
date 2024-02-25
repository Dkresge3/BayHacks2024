import React from 'react'
import './Dog.css'

function Dog() {
  return (
    <button onClick={() => (window.location.href = "http://192.168.101.225:8080/")}>
       Calculate
</button>
  )
}

export default Dog;

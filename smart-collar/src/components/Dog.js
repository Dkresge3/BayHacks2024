import React from 'react'
import './Dog.css'

function Dog() {
  return (
    <p>
        Check on your dogs and see how long they have gone without a walk
        <br></br>
        <button onClick={() => (window.location.href = "http://192.168.101.225:8080/")}>
        Calculate
        </button>
    </p>
  )
}

export default Dog;

<template>

    <router-view />


</template>

<script >
import {RouterView} from 'vue-router'

export default {
  name: 'App',

  }

</script>

<style >

#app {
  min-height: 100vh;
  min-width: 100vw;
}
.username{
  margin: 10px;
}
.content-wrapper{
    display: flex;
    align-items: center;
    padding: 20px 50px;
    width: 100%;
    left: 0px;
    top: 70px;

    background: linear-gradient(180deg, #F0F6FA 0%, #FFFFFF 100%);
  }

  .content{
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 10px;
    gap: 10px;
    background: #FFFFFF;
    border-radius: 15px;
    flex: none;
    order: 0;
    align-self: stretch;
    flex-grow: 0;
    justify-content: space-around;

  }


.blue-button {
    background-color: #005d9f;
    border: none;
    width: 300px;
    height: 40px !important;
    position: relative;
    padding: 0 2.5em;
    font-size: 15px;
    color: rgb(255, 255, 255);
    
    border-radius: 8px;
    /* box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); */
    transition: all 0.3s ease 0s;
    cursor: pointer;
    outline: none;
  }


  
    .button-label{
      text-align: center;

    }
  
  .warning{
      color: rgb(255, 0, 0);
  }
  
  .container {
    max-width: 95%;
    flex-wrap: wrap;
  }
  .form-title{
      text-align: center;
      margin-bottom: 10px;
  }
  form {
      width: 100%;
  }
  .input {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    /* align-items: center; */
   
  }
  .input > label {
    text-align: start;
    color: #005d9f;
    margin-left: 5px;
  }

  .input > input {
    width: 300px;
    background: #FFFFFF;
    box-shadow: 5px 0px 15px rgba(0, 93, 159, 0.1);
    border-radius: 8px;
    height: 40px !important;
    border: none;
    padding: 0px 10px 0px 10px;
    outline:none;
    
  }
  
  .input > input::placeholder {
    color:#0067a75d;
  }
  
  /* From uiverse.io */
  
  .blue-button:hover {
    /* background-color: #198754;
    box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4); */
    
    background-color: #0067a75d;
    color: #fff;
    /* transform: translate(-50%, -7px); */
  }
  /* .btn-pers:active {
    transform: translate(-50%, -1px);
  } */
  .alternative-option {
    text-align: center;
  }


</style>

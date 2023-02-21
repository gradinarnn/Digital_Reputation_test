<template>
    <div class="content-wrapper" >
      <div class="content" >
        <div class="container">
          <h3 class="warning" v-if="this.invalid_user_data">Неверные пользовательские данные</h3>
          <form @submit.prevent="login">
            <h2 class="form-title">Форма входа</h2>
            <div class="input">
              <label for="login">Логин</label>
              <input
                class="form-control"
                type="text"
                name="login"
                placeholder="admin"
                :value="username_email" @input="username_email = $event.target.value"
              />
            </div>
            <div class="input">
              <label for="password">Пароль</label>
              <input
                class="form-control"
                type="password"
                name="password"
                placeholder="admin123"
              :value="password" @input="password = $event.target.value"
              />
            </div>
  
            <button type="submit" class="blue-button"  @click="click_to_login">
              Вход
            </button>
            <div  class="button-label">
              <a :href="'/registration'">Регистрация</a>
            </div>
          </form>
        </div>
      </div>
    </div>
  
</template>
  
<script>
import gql from 'graphql-tag'
 
  export default {
      data(){
          return{
              username_email: '',
              password: '',
              invalid_user_data: false,
          }
      },


      methods:{
          click_to_login(){
              this.$apollo.mutate({
                  mutation: gql`
                    mutation MyMutation($username:String!, $password:String!) {             
                        login(username: $username, password: $password) {
                            id
                            email
                            username
                        }
                    }
                    `,
                  variables: {
                      username:this.username_email,
                      password: this.password,
                  }
              }).then((data) => {
                  if (data.data.login.username){
                      this.invalid_user_data = false
                      this.$router.push(`/`)
                  }
              })
              .catch(() => {
                  this.invalid_user_data = true  
              })
          },
      },
  }
</script>
  
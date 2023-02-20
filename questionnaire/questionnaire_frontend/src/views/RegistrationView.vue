<template>
    <div class="content-wrapper" >
      <div class="content" >
        <div class="container">

          <form @submit.prevent="registration">
            <h2 class="form-title">Форма регистрации</h2>

            <h3 class="warning" v-if="this.invalid_passwords">Пароли несовпадают</h3>

            <div class="input">
              <label for="login">Адрес электронной почты</label>
              <input
                class="form-control"
                type="email"
                name="login"
                placeholder="admin@admin.com"
                :value="email" @input="email = $event.target.value"
              />
            </div>

            <div class="input">
              <label for="password_again">Пароль</label>
              <input
                class="form-control"
                type="password"
                name="password"
                placeholder="admin123"
              :value="password" @input="password = $event.target.value"
              />
            </div>

            <div class="input">
              <label for="password">Пароль еще раз</label>
              <input
                class="form-control"
                type="password"
                name="password_again"
                placeholder="admin123"
              :value="password_again" @input="password_again = $event.target.value"
              />
            </div>

            <div class="input">
              <label for="password">Имя</label>
              <input
                class="form-control"
                type="text"
                name="first_name"
                placeholder="Ирина"
              :value="first_name" @input="first_name = $event.target.value"
              />
            </div>

            <div class="input">
              <label for="password">Фамилия</label>
              <input
                class="form-control"
                type="text"
                name="last_name"
                placeholder="Иванова"
              :value="last_name" @input="last_name = $event.target.value"
              />
            </div>
  
            <button type="submit" class="blue-button"  @click="click_to_registration">
              Регистрация
            </button>

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
            email: '',
            password: '',
            password_again: '',
            first_name: '',
            last_name: '',
            invalid_passwords: false,
          }
      },



      methods:{
        click_to_registration(){
            if (this.password == this.password_again){
              this.$apollo.mutate({
                  mutation: gql`mutation MyMutation($email:String!, $password:String!, $firstName: String!, $lastName: String!) {             
                    registration(input: {email: $email, password: $password, firstName:$firstName, lastName:$lastName}) 
                    }
                    `,
                  variables: {
                      email: this.email,
                      password: this.password,
                      firstName: this.first_name,
                      lastName: this.last_name,
                  }
              }).then((data) => {
                console.log('data', data);
                  if (data.data.registration == 'created'){
                    this.invalid_passwords =  false
                      this.$router.push(`/`)
                  }
              })
            }else{
                this.invalid_passwords = true
            }
          
          },
      },
  }
</script>
  
<style scoped>
</style>
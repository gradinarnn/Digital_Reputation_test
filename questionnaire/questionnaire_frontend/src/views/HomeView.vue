<template>
    <p>Вы зашли как {{ this.username }}</p>
    <p>Доступные тесты:</p>
    <div v-for="test in all_tests" :key="test.id">
      <a :href="'/test/'+test.id">{{ test.title }}</a>

    </div>
  
   
  </template>

<script >
  import gql from 'graphql-tag'

  export default {
    data(){
        return{
            username:'',
            all_tests: {}
        }
    },

    mounted(){
      this.$apollo.query({
        query: gql`query MyQuery {
          me {
            email
            id
            username
          }
        }
      `,
      }).then((data) => { 
        console.log('data', data);               
        if (!data.data.me){
          this.$router.push(`/login`)
        }else{
          this.username = data.data.me.username
        }
      })

    },



    watch:{
      username(value){
        if (value){
          this.$apollo.query({
        query: gql`query MyQuery {
            getAllTests {
              id
              title
            }
          }
      `,
      }).then((data) => {                
        if (data.data.getAllTests){
          this.all_tests = data.data.getAllTests
        }
      })
      } 
      
      },
    }
  }
</script >

<style scoped>

</style>
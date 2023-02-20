<template>
    <div v-if="this.question">
        <h3>{{ question.title }}</h3>

        <div v-for="answer in this.question.answers" :key="answer.id">
            <input type="checkbox"  :value="answer" v-model="checked_answers" />
            <label>{{answer.text}}</label>
        </div>

        <button v-if="checked_answers.length>0" @click="click_confirm">Следующий вопрос</button>
      
    </div>

  
</template>
  
<script>
import gql from 'graphql-tag'
 
  export default {
    name: "QuestionComponent",
      data(){
          return{
              checked_answers:[],
          }
        },
        emits: ['click_confirm'],


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
      })},
          
      
      props:{
        question:{
            type: Object,

        },
    },

    methods:{
        click_confirm(){
            console.log(JSON.stringify(this.checked_answers),JSON.stringify(this.question.correctAnswers));
            console.log("==", JSON.stringify(this.checked_answers)==JSON.stringify(this.question.correctAnswers));
            var result = false
            if (JSON.stringify(this.checked_answers)==JSON.stringify(this.question.correctAnswers)){
                result = true
            }
            this.checked_answers=[]
            this.$emit('click_confirm', result)
           
        }
    }
    
  }
</script>
  
<style scoped>
</style>
<template>
    <div v-if="this.result_percent" >
    Итоги теста:
    Правильных ответов {{ current_questions_count }} из {{ questions_count }}, что соответсвует {{ result_percent }}%
    <a :href="'/'">На главную</a>
    </div>
    <div v-else>
        <QuestionComponent 
            :question="question"
            @click_confirm="click_confirm_question"
            >
            
        </QuestionComponent>
    </div>

  
   
</template>

<script >
  import gql from 'graphql-tag'
  import QuestionComponent from '@/components/QuestionComponent.vue'

  export default {
    data(){
        return{
            username:'',
            all_tests: {},
            questions:{},
            question:{},
            current_questions_count: 0,
            questions_count:0,
            result_percent: null

        }
    },
    components: {
        QuestionComponent,
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
      
      this.$apollo.query({
        query: gql`query MyQuery($testId: ID!) {
          getQuestions(input: {testId: $testId}) {
            answers {
              id
              text
            }
            correctAnswers {
              id
              text
            }
            id
            title
          }
        }
      `,
      variables:{
        testId: this.$route.params.id
      }
      }).then((data) => {                
        if (data.data.getQuestions){
            console.log("data.data.getQuestions", data.data.getQuestions);
            this.questions = data.data.getQuestions.slice()
            this.questions_count = data.data.getQuestions.length 
            this.question=this.questions.pop()
        }
      })

    },

    methods:{
        click_confirm_question(value){
            if (value){
                this.current_questions_count=this.current_questions_count + 1
            }
            if (this.questions.length>0){
                this.question=this.questions.pop()
            }else{
                this.result_percent = this.current_questions_count/this.questions_count*100
            }
        }
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
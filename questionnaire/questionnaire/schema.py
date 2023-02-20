from typing import Optional

import strawberry
from django.contrib.auth.models import User
from strawberry.types import Info

from strawberry_django import auth

from testing.models import Test, Question


@strawberry.django.type(User)
class UserResult:
    id: strawberry.ID
    username: str
    email: str
    is_staff: bool

@strawberry.type
class AllTestsResult:
    id: strawberry.ID
    title: str


@strawberry.input
class RegistrationUserInput:
    password: str
    email: str
    first_name: str
    last_name: str

@strawberry.input
class GetQuestionsInput:
    test_id: strawberry.ID

@strawberry.type
class AnswerResult:
    id: strawberry.ID
    text:str

@strawberry.type
class QuestionsResult:
    id: strawberry.ID
    title: str

    @strawberry.field
    def answers(self, ) -> list[AnswerResult]:
        question = Question.objects.get(pk = self.id)
        return question.answers.all()

    @strawberry.field
    def correct_answers(self, ) -> list[AnswerResult]:
        question = Question.objects.get(pk=self.id)
        return question.correct_answers.all()


@strawberry.type
class Query:
    @strawberry.field
    def me(self, info: Info) -> Optional[UserResult]:
        if not info.context.request.user.is_authenticated:
            return None
        return info.context.request.user

    @strawberry.field
    def get_all_tests(self, ) -> list[AllTestsResult]:
        return Test.objects.all()

    @strawberry.field
    def get_questions(self, input: GetQuestionsInput ) -> list[QuestionsResult]:
        questions = Question.objects.filter(test__pk = input.test_id)
        return questions


@strawberry.type
class Mutation:
    login: UserResult = auth.login()
    logout = auth.logout()

    @strawberry.mutation
    def registration(self, input: RegistrationUserInput) -> str:
        if User.objects.filter(email=input.email):
            return 'exist'
        else:
            try:
                user = User.objects.create_user(username=input.email.split('@')[0],
                                                email=input.email,
                                                password=input.password,
                                                first_name=input.first_name,
                                                last_name=input.last_name, )

                return 'created'

            except Exception as e:
                return 'error'





schema = strawberry.Schema(query=Query, mutation=Mutation)

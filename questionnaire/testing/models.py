from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Test(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Набор тестов'
        verbose_name_plural = 'Наборы тестов'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Вопрос', unique=True)
    answers = models.ManyToManyField(Answer, related_name="all_answers", verbose_name='Варианты ответов')
    correct_answers = models.ManyToManyField(Answer, related_name="correct_answers", verbose_name='Верные ответы')

    def __str__(self):
        return f'{self.title}: {", ".join([correct_answer.__str__() for correct_answer in self.correct_answers.all()])}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'







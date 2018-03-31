from django.core.management.base import BaseCommand

from polls.models import *

from django.utils import timezone


class Command(BaseCommand):
    """
    pollsのテストデータを生成します

    example:python manage.py generate_polls_testdata
    """
    help = 'pollsのテストデータを生成します'

    def handle(self, *args, **options):

        questions = [
            {
                'text': '朝ごはん名に食べた？',
                'pub_date': timezone.now(),
                'answer': [
                    '白米',
                    'ちくわ',
                    'きゅうり',
                ]
            },
            {
                'text': 'Pだと何の言語が好き？',
                'pub_date': timezone.now(),
                'answer': [
                    'Perl',
                    'Python',
                    'PHP',
                    'Prolog',
                ]
            },
            {
                'text': '好きなバンドは何？',
                'pub_date': timezone.now(),
                'answer': [
                    'ハローハッピーワールド',
                    'ポッピンパーティー'
                    'ロゼリア',
                    'パステルパレット',
                    'アフターグロウ',
                ]
            }
        ]

        for v in questions:
            q = Question.objects.create(question_text=v['text'], pub_date=v['pub_date'])
            for ans in v['answer']:
                Choice.objects.create(question=q, choice_text=ans)

        self.stdout.write(self.style.SUCCESS('Successfully.'))



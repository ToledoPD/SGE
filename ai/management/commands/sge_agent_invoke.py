from django.core.management.base import BaseCommand
from ai.agent import SEGAgent


class Command(BaseCommand):

    def handle(self, *args, **options):
        agent = SEGAgent()
        agent.invoke()

        self.stdout.write(
            self.style.SUCCESS('SGE AGENT INVOCADO COM SUCESSO!')
        )

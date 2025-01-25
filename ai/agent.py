import json
from django.conf import settings
from django.core import serializers
from openai import OpenAI
from ai import prompts, models
from products.models import Product
from outflows.models import Outflow


class SEGAgent:

    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPEN_API_KEY,
        )

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()
        return json.dumps({
            'products': serializers.serialize('json', products),
            'outflows': serializers.serialize('json', outflows),
        })

    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": prompts.SYSTEM_PROMPT,
                },

                {
                    "role": "user",
                    "content": prompts.USER_PROMPT.replace('{{data}}', self.__get_data()),
                },
            ],
        )
        result = response.choices[0].message.content
        models.AiResult.objects.create(result=result)

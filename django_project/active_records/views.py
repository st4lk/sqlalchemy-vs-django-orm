import logging
from django.http import JsonResponse

from .models import M1

logger = logging.getLogger(__name__)


def active_record_example(request):
    one = M1.objects.get(pk=1)
    another_one = M1.objects.get(pk=1)
    another_one.value = 'new-value'

    logger.info('one.value = %s', one.value)
    logger.info('another_one.value = %s', another_one.value)

    return JsonResponse({
        'one.value': one.value,
        'another_one.value': another_one.value,
    })

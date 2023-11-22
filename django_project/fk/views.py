import logging
from django.http import JsonResponse

from .models import FkLeft, FkRight

logger = logging.getLogger(__name__)


def save_fk(request):
    right = FkRight()
    left = FkLeft(right=right)

    left.save()

    return JsonResponse({
        'right.id': right.id,
        'left.id': left.id,
        'left.right_id': left.right_id,
    })

from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('index page accessed')
    return HttpResponse('Hello world')

def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'error: {e}')
        return HttpResponse('error')
    else:
        logger.debug('about page accessed')
        return HttpResponse('about us')
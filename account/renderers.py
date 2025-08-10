import json
import logging
from rest_framework import renderers

logger = logging.getLogger(__name__)  # Get logger for this file

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'ErrorDetail' in str(data):
            logger.error(f"Validation error: {data}")  # This logs to terminal
            return json.dumps({'errors': data})
        return json.dumps(data)
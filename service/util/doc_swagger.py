from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'rotate_image', {
    'Rotação imagem': fields.String('aperte execute, e vá para: http://localhost:9000/rotate_img ')})

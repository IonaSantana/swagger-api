import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np
import cv2
import re

class ImageService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_MODEL)
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo VADER a ser usado
        """

        #self.model = SentimentIntensityAnalyzer()

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_rest(self, path):
        
        logger.debug(mensagens.INICIO_LEITURA)
        start_time = time.time()

        response_image = self.rotate_Image(path)
    
        logger.debug(mensagens.FIM_LEITURA)
        logger.debug(f"Fim de todas as leituras em {time.time()-start_time}")

        #response = {
        #             "listaImagens": json.loads(df_response.to_json(
        #                                                                    orient='records', force_ascii=False))}

        return response_image

    def rotate_Image(self, path):
        """
        Pega o modelo carregado e aplica em texts
        """
        logger.debug('Iniciando a imagem...')
        logger.debug(path)
        path_split = "service/service/Bichinho-49.jpeg"
        logger.debug(path_split + ' aaa')
        img = cv2.imread(path_split)
        
        if (img is None):
            logger.debug('Imagem Vazia')
        
        img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
       
        adress_image = 'service/service/YESTE.jpeg'
        logger.debug(adress_image)
        image = cv2.imwrite(adress_image, img_rotate_180)
        logger.debug(adress_image)
        return image

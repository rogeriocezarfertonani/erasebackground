from ast import Str
from unittest.mock import patch
import uuid
from rembg import remove
import uuid
from django.conf import settings
from django.conf.urls.static import static
import base64


#nameuuid = str(uuid.uuid4())
#print('uuuid é', nameuuid)
#input_path = 'media/caveira.jpg'
#output_path = str('media/caveira2.jpg')


# with open (input_path,'rb') as i:
#    with open (output_path,'wb') as o:
#        input = i.read()
#        output = remove(input)
#        o.write(output)

class EraseBackground ():

    def removeBacground(self, inputPath, outputPath):
        with open(inputPath, 'rb') as i:
            with open(outputPath, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)

    def removeBg(self, file_obj):
        output = 'media/' + str(uuid.uuid4()) + str(file_obj)
        saida = output
        print('A SAIDA É :',output)
        # print('URL',settings.MEDIA_ROOT)
        #static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

        with open(output, 'wb') as o:
            input = file_obj.read()
            output = remove(input)
            o.write(output)
            print('O nome de o',saida)

            return saida 
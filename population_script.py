import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD_Team4D.settings')
django.setup()
from upskill_photography.models import Picture, Category


def populate():
    picture1 = [
        {'uploading user': 'james',
         'title': 'cats',
         'image': 'static/images/',
         'likes': '10',
         'views': '120',
         }
    ]
    picture2 = [
        {'uploading user': 'james',
         'title': 'europe',
         'image': 'static/images/',
         'likes': '104',
         'views': '1205',
         }
    ]
    picture3 = [
        {'uploading user': 'oliver',
         'title': 'space',
         'image': 'static/images/',
         'likes': '130',
         'views': '1120',
         }
    ]
    picture4 = [
        {'uploading user': 'rojhat',
         'title': 'bugatti',
         'image': 'static/images/',
         'likes': '10',
         'views': '120',
         }
    ]
    picture5 = [
        {'uploading user': 'oliver',
         'title': 'cars',
         'image': 'static/images/',
         'likes': '10046',
         'views': '134456',
         }
    ]
    picture6 = [
        {'uploading user': 'rojhat',
         'title': 'dogs',
         'image': 'static/images/',
         'likes': '14',
         'views': '99',
         }
    ]
    picture7 = [
        {'uploading user': 'annie',
         'title': 'lions',
         'image': 'static/images/',
         'likes': '104',
         'views': '1204',
         }
    ]


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

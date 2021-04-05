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
         'title': 'pagani',
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
    cats = {'animals': {'Pictures': picture1, 'views': 128, 'likes': 64},
            'space ': {'Pictures': picture3, 'views': 64, 'likes': 32},
            'cars':  {'Pictures': picture5, 'views': 32, 'likes': 16}}
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pictures']:
            add_picture(c, p['title'], p['image'], p['uploading_user'], views=p['views'])

    for c in Category.objects.all():
        for p in Picture.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_cat(name, views=0, likes=0):
    c: object = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def add_picture(cat, title, image, uploading_user, views=0, likes=0):
    p = Picture.objects.get_or_create(category=cat, title=title)[0]
    p.title = Picture.title
    p.uploading_user = Picture.uploading_user
    p.image = Picture.image
    p.views = Picture.views
    p.likes = Picture.likes
    p.save()
    return p


if __name__ == '__main__':
    print('Starting upskillphotography population script...')
    populate()

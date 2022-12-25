from PIL import Image
from PIL.Image import Resampling


def resize_image(img: Image, new_width: int = None, new_height: int = None):
    width, height = img.size

    if new_width and not new_height:
        new_height = int(new_width * height / width)

    if new_height and not new_width:
        new_width = int(new_height * width / height)

    img = img.resize((new_width, new_height), Resampling.LANCZOS)

    return img


def get_collage(img_1: Image, img_2: Image, mode):
    if mode == 'vertical':
        if img_1.width < img_2.width:
            img_2 = resize_image(img_2, new_width=img_1.width)
        elif img_2.width < img_1.width:
            img_2 = resize_image(img_1, new_width=img_2.width)

        collage = Image.new('RGBA', (img_1.width, img_1.height + img_2.height))
        collage.paste(img_1)
        collage.paste(img_2, (0, img_1.height))

        return collage

    elif mode == 'horizontal':
        if img_1.height < img_2.height:
            img_2 = resize_image(img_2, new_height=img_1.height)
        elif img_2.height < img_1.height:
            img_1 = resize_image(img_1, new_height=img_2.height)

        collage = Image.new('RGBA', (img_1.width + img_2.width, img_1.height))
        collage.paste(img_1)
        collage.paste(img_2, (img_1.width, 0))

        return collage
    else:
        return None


# example
def main():
    img_1 = Image.open('1.png')
    img_2 = Image.open('3.png')
    
    collage_h = get_collage(img_1, img_2, 'horizontal')
    collage_v = get_collage(img_1, img_2, 'vertical')

    if collage_h:
        collage_h.save('collage_h.png')
    if collage_v:
        collage_v.save('collage_v.png')


if __name__ == '__main__':
    main()

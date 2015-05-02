import os
import pygame.camera
import pygame.image
import sys

counter = 0


def get_output_dir():
    out = os.path.join(os.path.expanduser("~"), 'pystop')
    if not os.path.exists(out):
        os.makedirs(out)
    return out


def get_next_image_filename(outdir):
    global counter
    filename = None
    path_exists = True
    while path_exists:
        filename = os.path.join(outdir, '{:04}.jpg'.format(counter))
        counter += 1
        path_exists = os.path.exists(filename)
    return filename


def main():
    outdir = get_output_dir()
    last_img = None
    pygame.camera.init()
    cameras = pygame.camera.list_cameras()
    print cameras
    webcam = pygame.camera.Camera()
    webcam.start()
    img = webcam.get_image()
    width = img.get_width()
    height = img.get_height()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('pystop - [spacebar] to capture')

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    filename = get_next_image_filename(outdir)
                    pygame.image.save(img, filename)
                    last_img = img
                    last_img.set_alpha(128)

        screen.blit(img, (0, 0))
        if last_img:
            screen.blit(last_img, (0, 0))
        pygame.display.flip()
        img = webcam.get_image()

if __name__ == '__main__':
    main()
#Snake_Game.py
import pygame
import Snake


_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(235, 135, 200)
_PLAYER_COLOR = pygame.Color(0, 0, 128)


class SnakeGame:
    def __init__(self):
        self._state = Snake.GameState()
        self._running = True


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            # Load our image, but we haven't got a scaled-down version
            # yet.  We'll scale it when we need it.
            self._player_image = pygame.image.load('snake.png')
            self._player_image_scaled = None


            self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))
            
            while self._running:
                clock.tick(_FRAME_RATE)
                self._handle_events()
                self._draw_frame()

        finally:
            pygame.quit()


    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

        # Throw away the scaled version of the player image.  Since the
        # size of the window has changed, we'll need to re-scale it to
        # be appropriate to the window's new size, which we'll do the
        # next time we draw a frame.
        self._player_image_scaled = None


    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._handle_event(event)

        self._handle_keys()


    def _handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._stop_running()
        elif event.type == pygame.VIDEORESIZE:
            self._create_surface(event.size)
        


    def _handle_keys(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._state.Snake().move_left()

        if keys[pygame.K_RIGHT]:
            self._state.Snake().move_right()

        if keys[pygame.K_UP]:
            self._state.Snake().move_up()

        if keys[pygame.K_DOWN]:
            self._state.Snake().move_down()
        self._state.eaten()


    


    def _stop_running(self) -> None:
        self._running = False


    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        self._draw_snake()
        self._draw_food()
        pygame.display.flip()


    def _draw_snake(self) -> None:
        top_left_frac_x = self._state.Snake().top_left_x()
        top_left_frac_y = self._state.Snake().top_left_y()
        width_frac = self._state.Snake().width()
        height_frac = self._state.Snake().height()

        top_left_pixel_x = self._frac_x_to_pixel_x(top_left_frac_x)
        top_left_pixel_y = self._frac_y_to_pixel_y(top_left_frac_y)
        width_pixel = self._frac_x_to_pixel_x(width_frac)
        height_pixel = self._frac_y_to_pixel_y(height_frac)

        player_rect = pygame.Rect(
            top_left_pixel_x, top_left_pixel_y,
            width_pixel, height_pixel)

        if self._player_image_scaled == None:
            # If we don't have a scaled version of our image, then we'll
            # need to create one.  We do that by calling the
            # pygame.transform.scale() function, which takes two arguments:
            # an image and the size you want the image to be.  The result
            # is an image that has been scaled proportionally, which we'll
            # store in self._player_image_scaled.
            self._player_image_scaled = pygame.transform.scale(
                self._player_image, (width_pixel, height_pixel))

        # Now, we'll draw our scaled image -- either the one we just created
        # or, if we had it already, the one we already had.
        self._surface.blit(
            self._player_image_scaled,
            (top_left_pixel_x, top_left_pixel_y))
    def _draw_food(self) -> None:
        top_left_frac_x = self._state.Food().top_left_x()
        top_left_frac_y = self._state.Food().top_left_y()
        width_frac = self._state.Food().width()
        height_frac = self._state.Food().height()

        top_left_pixel_x = self._frac_x_to_pixel_x(top_left_frac_x)
        top_left_pixel_y = self._frac_y_to_pixel_y(top_left_frac_y)
        width_pixel = self._frac_x_to_pixel_x(width_frac)
        height_pixel = self._frac_y_to_pixel_y(height_frac)

        player_rect = pygame.Rect(
            top_left_pixel_x, top_left_pixel_y,
            width_pixel, height_pixel)

        pygame.draw.rect(self._surface, _PLAYER_COLOR, player_rect)
            

    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        return self._frac_to_pixel(frac_x, self._surface.get_width())


    def _frac_y_to_pixel_y(self, frac_y: float) -> int:
        return self._frac_to_pixel(frac_y, self._surface.get_height())


    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac * max_pixel)



if __name__ == '__main__':
    SnakeGame().run()

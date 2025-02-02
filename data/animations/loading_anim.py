from PIL import Image, ImageDraw
import numpy as np
import math


def create_loading_animation():
    """
    Generates an animated GIF representing 'neurons' in motion to be used as a loading screen.

    This function simulates the motion of a number of 'neurons' (ellipses) across a 2D plane,
    each moving at a random speed and changing direction at random intervals. At each frame,
    lines are drawn between every pair of neurons. The resulting animation is saved as a GIF file.

    The positions of the neurons are randomly initialized and updated for each frame based on
    their speed and direction. The direction of each neuron changes every N frames, where N is
    a random number specific to each neuron. A rotation is also applied to the neurons for added
    visual effect.

    The final GIF has a black background with the neurons and connecting lines drawn in white.

    Output:
    A GIF file named 'neurons.gif' saved in the current directory.
    """
    SIZE_X = 1750  # Width of the image in pixels
    SIZE_Y = 700   # Height of the image in pixels

    frames = []
    ellipse_positions = []
    num_points = 10
    rnd_nums = np.random.randint(0, SIZE_X, num_points * 4)
    neuron_size = 5

    # Initializing directions for each point with random speeds between -2 and 2
    speeds = np.random.randint(-2, 5, (num_points, 2))

    # Introducing an array for controlling direction change frequency for each neuron.
    direction_change_freqs = np.random.randint(10, 30, num_points)

    # Initialize the rotation speed
    rotation_speed = -0.005  # In radians per frame.

    for point in range(num_points):
        start_index = point * 4
        left = rnd_nums[start_index + 0]
        upper = rnd_nums[start_index + 1]
        right = left + neuron_size
        lower = upper + neuron_size
        ellipse_pos = [left, upper, right, lower]
        ellipse_positions.append(ellipse_pos)

    for frame_num in range(300):
        img = Image.new('RGB', (SIZE_X, SIZE_Y), color='black')
        ellipse_centers = []  # Reset ellipse centers for the new frame

        for num_point, ellipse in enumerate(ellipse_positions):
            speed = speeds[num_point]
            new_left = ellipse[0] + speed[0]
            new_upper = ellipse[1] + speed[1]
            new_right = new_left + neuron_size
            new_lower = new_upper + neuron_size

            # check if the new position would be off-screen
            if new_left < 0 or new_right > SIZE_X:
                speeds[num_point][0] *= -1  # reverse direction on x-axis
            if new_upper < 0 or new_lower > SIZE_Y:
                speeds[num_point][1] *= -1  # reverse direction on y-axis

            new_pos = [new_left, new_upper, new_right, new_lower]
            ellipse_positions[num_point] = new_pos

            # Change direction slightly every Nth frame where N is the direction_change_freq for this neuron.
            if frame_num % direction_change_freqs[num_point] == 0:
                speeds[num_point] = np.random.randint(-5, 5, size=2)

            d = ImageDraw.Draw(img)
            d.ellipse(new_pos, fill='white')

        for ellipse in ellipse_positions:
            ellipse_centers.append([(ellipse[0] + ellipse[2]) / 2, (ellipse[1] + ellipse[3]) / 2])

        # Apply the rotation to all the ellipse centers
        for i in range(len(ellipse_centers)):
            x = ellipse_centers[i][0] - SIZE_X / 2
            y = ellipse_centers[i][1] - SIZE_Y / 2

            new_x = x * math.cos(rotation_speed) - y * math.sin(rotation_speed)
            new_y = x * math.sin(rotation_speed) + y * math.cos(rotation_speed)

            ellipse_centers[i][0] = new_x + SIZE_X / 2
            ellipse_centers[i][1] = new_y + SIZE_Y / 2
            ellipse_positions[i] = [new_x + SIZE_X / 2, new_y + SIZE_Y / 2, new_x + SIZE_X / 2 + neuron_size,
                                    new_y + SIZE_Y / 2 + neuron_size]

        drawn_ellipses = []
        for ellipse in ellipse_centers:
            other_ellipses = ellipse_centers.copy()
            other_ellipses.remove(ellipse)
            for other_ellipse in other_ellipses:
                ellipse_tuple = [ellipse[0], ellipse[1], other_ellipse[0], other_ellipse[1]]
                if ellipse_tuple not in drawn_ellipses:
                    drawn_ellipses.append(ellipse_tuple)
                    d.line(ellipse_tuple, fill="white", width=1)

        frames.append(img)

    frames[0].save('neurons.gif', format='GIF', append_images=frames[1:], save_all=True, duration=50, loop=0)

from os import walk

import customtkinter as ctk
from PIL import Image


class AnimatedButton(ctk.CTkButton):
    """
    A CustomTkinter button that plays an animation (forward and backward)
    using image frames loaded from specified light and dark mode directories.

    The animation can be triggered once per click, or set to loop indefinitely
    when initialized with 'loop=True'.
    """

    def __init__(
        self,
        parent: ctk.CTk | ctk.CTkFrame,
        light_path: str,
        dark_path: str,
        button_text: str,
        loop: bool = False,
    ):
        """
        Initializes the AnimatedButton, loads all frames,
        and sets up animation state.

        Parameters
        ----------
        parent : ctk.CTk or ctk.CTkFrame
            The parent widget.
        light_path : str
            Path to the folder containing light mode animation frames.
        dark_path : str
            Path to the folder containing dark mode animation frames.
        button_text : str
            The text displayed on the button.
        loop : bool, optional
            If True, the animation plays continuously forward and backward
            after initialization. If False, it requires a click to start
            each cycle. Defaults to False.
        """

        # animation logic setup
        self.frames = self.import_folders(
            light_path=light_path,
            dark_path=dark_path,
        )
        self.frames_index = 0
        self.frames_index_max = len(self.frames) - 1
        self.animation_status = ctk.StringVar(value="start")
        self.animation_status.trace(mode="w", callback=self.animate)
        self.is_loop = loop

        super().__init__(
            parent,
            text=button_text,
            image=self.frames[self.frames_index],
            command=self.trigger_animation if not self.is_loop else None,
        )
        if self.is_loop:
            self.trigger_animation()

    def import_folders(self, light_path: str, dark_path: str):
        """
        Loads, sorts, and pairs image files from light and dark folders
        into a list of `ctk.CTkImage` objects.

        Returns
        -------
        list[ctk.CTkImage]
            The compiled list of dual-mode animation frames.
        """

        image_paths = []
        for path in (light_path, dark_path):
            for _, __, data in walk(path):
                sorted_data = sorted(
                    data,
                    key=lambda item: int(item.split(".")[0][-5:]),
                )
                full_path_data = [f"{path}/{item}" for item in sorted_data]
                image_paths.append(full_path_data)
        image_paths = zip(*image_paths)

        ctk_images = []
        for image_path in image_paths:
            light_image_path, dark_image_path = image_path
            ctk_images.append(
                ctk.CTkImage(
                    light_image=Image.open(light_image_path),
                    dark_image=Image.open(dark_image_path),
                )
            )

        return ctk_images

    # state management
    def trigger_animation(self):
        """
        Starts the animation forward if at "start" or backward if at "end".

        Updates `self.animation_status` which triggers the `animate` method.
        """

        if self.animation_status.get() == "start":
            self.frames_index = 0
            self.animation_status.set("forward")

        if self.animation_status.get() == "end":
            self.frames_index = self.frames_index_max
            self.animation_status.set("backward")

    def animate(self, *args):
        """
        The core recursive function that updates the frame image every 20ms.

        The final status (`"start"/"end"` or `"forward"/"backward"`)
        is determined
        by the value of `self.is_loop`.
        """

        direction_map = {
            "forward": {
                "delta": 1,
                "is_continue": lambda index: index < self.frames_index_max,
                "new_status": "backward" if self.is_loop else "end",
            },
            "backward": {
                "delta": -1,
                "is_continue": lambda index: index > 0,
                "new_status": "forward" if self.is_loop else "start",
            },
        }

        status = self.animation_status.get()
        if status not in direction_map:
            return

        delta, is_continue, new_status = direction_map[status].values()

        self.frames_index += delta
        self.configure(image=self.frames[self.frames_index])
        if is_continue(self.frames_index):
            self.after(20, self.animate)
        else:
            self.animation_status.set(new_status)

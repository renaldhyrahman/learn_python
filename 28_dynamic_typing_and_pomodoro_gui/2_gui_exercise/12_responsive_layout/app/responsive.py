class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {k: v for k, v in sorted(size_dict.items())}
        self.current_min_size = None
        self.window.bind("<Configure>", self.check_size)

        self.window.update()

        min_height = self.window.winfo_height()
        min_width = list(self.size_dict)[0]
        self.window.minsize(min_width, min_height)

    def check_size(self, event):
        if event.widget != self.window:
            return
        window_width = event.width
        checked_size = None
        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
                checked_size = min_size
        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[self.current_min_size]()

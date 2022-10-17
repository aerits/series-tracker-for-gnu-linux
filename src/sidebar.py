class sidebar(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello World")

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

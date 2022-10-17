from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget

class Bar(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("sidebar")

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

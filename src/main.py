from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget


class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello World")

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class main(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        await self.view.dock(Hover(), edge="left", size=40)
        await self.view.dock(Hover(), Hover(), edge="top")
        
    async def on_load(self, event):
        await self.bind("q", "quit")


main.run(textual.log)

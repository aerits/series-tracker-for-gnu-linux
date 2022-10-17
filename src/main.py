from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget

# classes

from Sidebar import Bar

class main(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        await self.view.dock(Bar(), edge="left", size=40)
        await self.view.dock(Hover(), Hover(), edge="top")
        
    async def on_load(self, event):
        await self.bind("q", "quit")


main.run(log="textual.log")

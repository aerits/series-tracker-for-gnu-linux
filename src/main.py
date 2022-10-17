from rich.panel import Panel

from textual.app import App, ComposeResult
from textual.reactive import Reactive
from textual.widget import Widget

# classes

from Sidebar import Bar
from Body import body

class main(App):

    async def on_mount(self) -> None:
        await self.view.dock(Bar(), edge="left", size=40)
        await self.view.dock(body(), body(), edge="top")
        
    async def on_load(self, event):
        await self.bind("q", "quit")


main.run()

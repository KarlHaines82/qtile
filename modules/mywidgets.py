from libqtile.widget import base
import re
import subprocess
from powerline.bindings.qtile import widget as pwidget

__name__ = "mywidgets"


__all__ = [
    'CapsNumWidget',
    'MyPlWidget'
]


class MyPlWidget(pwidget.PowerlineTextBox):
    def cmd_get(self):
        return str(self.text, 'UTF-8')


class CapsNumWidget(base.ThreadPoolText):
    """Extended caps/num lock widget"""
    defaults = [("update_interval", 0.5, "Update Time in seconds.")]
    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(CapsNumWidget.defaults)
        return

    def get_indicators(self):
        """Return a list with the current state of the keys."""
        try:
            output = self.call_process(["xset", "q"])
        except subprocess.CalledProcessError as err:
            output = err.output
            return []
        if output.startswith("Keyboard"):
            indicators = re.findall(r"(Caps|Num)\s+Lock:\s*(\w*)", output)
            return indicators

    def ThreadPoolText(self):
        """Poll content for the text box."""
        indicators = self.get_indicators()
        return indicators

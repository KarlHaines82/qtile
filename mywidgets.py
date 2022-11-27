from libqtile.widget import base
import re, subprocess

__all__ = [
    'CapsNumWidget',
]

class CapsNumWidget(base.ThreadPoolText):
    """Extended caps/num lock widget"""
    defaults = [("update_interval", 0.5, "Update Time in seconds.")]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(CapsNumWidget.defaults)

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

    def poll(self):
        """Poll content for the text box."""
        indicators = self.get_indicators()
        s = "C["+indicators[0][1]+"] N["+indicators[1][1]+"]"
        return s

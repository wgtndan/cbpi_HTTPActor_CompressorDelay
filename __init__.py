from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property
import httplib2
from flask import request

@cbpi.actor
class HTTPActor(ActorBase):

    a_url = Property.Text("Controller Address", configurable=True, default_value="http://<ipaddress>:<port>", description="Address of the controller. Do not add a trailing slash (ex: http://192.168.0.10)")
    b_on = Property.Text("On Command", configurable=True, default_value="control?cmd=GPIO,<pin>,1", description="Command to turn actor on")
    c_off = Property.Text("Off Command", configurable=True, default_value="control?cmd=GPIO,<pin>,0", description="Command to turn actor off")
    d_pow = Property.Text("Power Command", configurable=True, default_value="control?cmd=PWM,<pin>,", description="Command to set actor power level. Power level will be added to the end of the command. If device does not support this, make this field blank.")
    
    power = 100
    
    def send(self, command):
        try:
            h = httplib2.Http(".cache")
            ## Sending http command ""
            (resp, content) = h.request("%s/%s" % (self.a_url, command), "GET", headers={'cache-control':'no-cache'})
        except Exception as e:
            self.api.app.logger.error("FAILED to switch HTTP actor: %s/%s" % (self.a_url, command))

    def on(self, power=None):
        self.send(self.b_on)
        if power is not None:
            self.set_power(power)

    def off(self):
        self.send(self.c_off)
        
    def set_power(self, power):
        if power is not None and self.d_pow is not None and self.d_pow:
            if power != self.power:
                self.power = int(power)
                self.send("%s%s" % (self.d_pow, power))


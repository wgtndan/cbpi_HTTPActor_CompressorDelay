from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property
import httplib2
from flask import request

@cbpi.actor
class WIFISocket(ActorBase):

    a_url = Property.Text("Server Address", configurable=True, default_value="http://<ipaddress>:<port>", description="Address of the controller")
    b_on = Property.Text("On Command", configurable=True, default_value="control?cmd=GPIO,<pin>,1", description="Command to turn actor on")
    c_off = Property.Text("Off Command", configurable=True, default_value="control?cmd=GPIO,<pin>,0", description="Command to turn actor off")
    d_pwm = Property.Text("PWM Command", configurable=True, default_value="control?cmd=PWM,<pin>,<level>", description="Command to set actor power level, if it supports PWM")
    
    def send(self, command, value=None):
        try:
            h = httplib2.Http(".cache")
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            ## Sending http command ""
            (resp_headers, content) = h.request("%s/%s" % (self.a_url, command), "GET",  body=command, headers=headers)
        except Exception as e:
            self.api.app.logger.error("FAILED to switch HTTP actor: %s/%s" % (self.a_url, command))

    def on(self, power=None):
        self.send(self.b_on)
        if power is not None:
            self.send(self.d_pwm, power)

    def off(self):
        self.send(self.c_off)

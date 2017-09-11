from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property
import httplib2
from flask import request

from datetime import datetime, timedelta

cbpi.HTTPActor_compressors = []

@cbpi.actor
class HTTPActor_Compressor(ActorBase):

    a_url = Property.Text("Controller Address", configurable=True, default_value="http://<ipaddress>:<port>", description="Address of the controller. Do not add a trailing slash (ex: http://192.168.0.10)")
    b_on = Property.Text("On Command", configurable=True, default_value="control?cmd=GPIO,<pin>,1", description="Command to turn actor on")
    c_off = Property.Text("Off Command", configurable=True, default_value="control?cmd=GPIO,<pin>,0", description="Command to turn actor off")
    d_delay = Property.Number("Compressor Delay", configurable=True, default_value=10, description="minutes")
    compressor_on = False
    compressor_wait = datetime.utcnow()
    delayed = False

    def init(self):
        super(HTTPActor_Compressor, self).init()
        cbpi.HTTPActor_compressors += [self]
    
    def send(self, command):
        try:
            h = httplib2.Http(".cache")
            ## Sending http command ""
            (resp, content) = h.request("%s/%s" % (self.a_url, command), "GET", headers={'cache-control':'no-cache'})
        except Exception as e:
            self.api.app.logger.error("FAILED to switch HTTP actor: %s/%s" % (self.a_url, command))

    def on(self, power=None):
        if datetime.utcnow() >= self.compressor_wait:
            self.compressor_on = True
            self.send(self.b_on)
            self.delayed = False
        else:
            print "Delaying Turing on Compressor"
            cbpi.app.logger.info("Delaying Turing on Compressor")
            self.delayed = True


    def off(self):
        if self.compressor_on:
            self.compressor_on = False
            self.compressor_wait = datetime.utcnow() + timedelta(minutes=int(self.d_delay))
        self.delayed = False
        self.send(self.c_off)

@cbpi.backgroundtask(key="update_HTTPActor_compressors", interval=5)
def update_HTTPActor_compressors(api):
    for compressor in cbpi.HTTPActor_compressors:
        if compressor.delayed and datetime.utcnow() >= compressor.compressor_wait:
            cbpi.app.logger.info("Compressor Off so not responding to end of delay")
            if compressor.compressor_on:
                cbpi.app.logger.info("Turing Compressor Back on After Delay")
                compressor.on()
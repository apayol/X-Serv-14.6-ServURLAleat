#!/usr/bin/python3

import webapp
import random

class aleat(webapp.webApp):


    def process(self, parsedRequest):
        num_aleat = random.randint(1,9999999)
        return ("200 OK", "<html><body><h1>Hola.</h1>" +
            "<p><a href= http://localhost:1234/" + str(num_aleat) +
            ">Dame otra</a></p></body></html>")
 
if __name__ == '__main__':
    my_webapp = aleat("localhost", 1234)

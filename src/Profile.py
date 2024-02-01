import tornado.web
import json
import base64
import os

class Handler(tornado.web.RequestHandler):
    D = {
        "alice" : {
            "name" : "Alice Smith",
            "DOB" : "1975-01-01",
            "email" : "alice@example.com",
            "image" : "/static/alice.png"
        },
        "bob" : {
            "name" : "Bob Jones",
            "DOB" : "1983-12-31",
            "email" : "bob@bob.xyz",
            "image" : "/static/bob.png"
        },
        "carol" : {
            "name" : "Carol Ling",
            "DOB" : "2000-07-17",
            "email" : "carol@example.com",
            "image" : "/static/carol.png"
        },
        "dave" : {
            "name" : "Dave N. Port",
            "DOB" : "1999-03-14",
            "email" : "dave@dave.dave",
            "image" : "/static/dave.png"
        }
    }
    
    def get(self):
        p = self.request.path.split("/")
        uname = p[2]
        info = self.D[uname]

        self.render(
            "../html/Profiles.html",
            name=info["name"],
            dob=info["DOB"],
            email=info["email"],
            image=info["image"],
            uname=uname
        )
    
    def post(self):
        p = self.request.path.split("/")
        uname = p[2]
        info = self.D[uname]

        J = json.loads(self.request.body)
        info["name"] = J["name"]
        info["dob"] = J["dob"]
        info["email"] = J["email"]

        if (J["image"] != ""):
            filename = "tornado-lab/html/" + uname + ".png"
            with open(filename, "wb") as file:
                file.write(base64.b64decode(J["image"]))
            info["image"] = "/static/" + uname + ".png"
    
        print("WE GOT:",info["name"],info["dob"],info["email"],info["image"][:20])
        resp={"ok": True}
        self.write( json.dumps(resp) )
import tornado.web

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path.split("/")
        
        uname = p[2]

        D = {
            "alice" : {
                "name" : "Alice Smith",
                "DOB" : "January 1",
                "email" : "alice@example.com",
                "image" : "/static/alice.png"
            },
            "bob" : {
                "name" : "Bob Jones",
                "DOB" : "December 31",
                "email" : "bob@bob.xyz",
                "image" : "/static/bob.png"
            },
            "carol" : {
                "name" : "Carol Ling",
                "DOB" : "July 17",
                "email" : "carol@example.com",
                "image" : "/static/carol.png"
            },
            "dave" : {
                "name" : "Dave N. Port",
                "DOB" : "March 14",
                "email" : "dave@dave.dave",
                "image" : "/static/dave.png"
            }
        }

        info = D[uname]

        self.render(
            "../html/Profiles.html",
            name=info["name"],
            dob=info["DOB"],
            email=info["email"],
            image=info["image"]
        )
        
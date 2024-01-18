import tornado.web

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path.split("/")
        
        uname = p[2]

        D = {
            "alice" : {
                "name" : "Alice Smith",
                "DOB" : "Jan 1",
                "email" : "alice@example.com"
            },
            "bob" : {
                "name" : "Bob Jones",
                "DOB" : "Dec 31",
                "email" : "bob@bob.xyz"
            },
            "carol" : {
                "name" : "Carol Ling",
                "DOB" : "Jul 17",
                "email" : "carol@example.com"
            },
            "dave" : {
                "name" : "Dave N. Port",
                "DOB" : "Mar 14",
                "email" : "dave@dave.dave"
            }
        }

        info = D[uname]

        self.render(
            "../html/Profiles.html",
            name=info["name"],
            dob=info["DOB"],
            email=info["email"]
        )
        
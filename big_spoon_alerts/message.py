import datetime

class Message:

    def __init__(self, menu_diff, current_menu):
        self.menu_diff = menu_diff
        self.current_menu = current_menu

    def getSubject(self):
        recap = ""
        if(len(self.menu_diff["new"])>0):
            recap += str(len(self.menu_diff["new"])) + " New"
        if(len(self.menu_diff["dropped"])>0):
            if(len(self.menu_diff["new"])>0):
               recap += ", "
            recap += str(len(self.menu_diff["dropped"])) + " Dropped"
        return datetime.datetime.now().strftime("%Y-%m-%d") + " | Big Spoon Menu: " + recap


    def getBody(self):
        body = ""
        if(len(self.menu_diff["new"])>0):
            body += "New Flavors:\n"
            for new_flavor in self.menu_diff["new"]:
                 body += "\t" + new_flavor['name'] + "\n"
                 body += "\t\t" + new_flavor['blurb'] + "\n"
            body += "\n"

        if(len(self.menu_diff["dropped"])>0):
            body += "Dropped Flavors:\n"
            for dropped_flavor in self.menu_diff["dropped"]:
                 body += "\t" + dropped_flavor['name'] + "\n"
                 body += "\t\t" + dropped_flavor['blurb'] + "\n"
            body += "\n"

        if(len(self.current_menu)>0):
            body += "Current Menu:\n"
            for current_flavor in self.current_menu:
                 body += "\t" + current_flavor['name'] + "\n"
                 body += "\t\t" + current_flavor['blurb'] + "\n"
        return body

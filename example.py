from errbot import BotPlugin, botcmd
from config.py import BOT_IDENTITY


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return 'It *works* !'  # This string format is markdown.
    
    @botcmd
    def hello_world(self, msg, args):
        return 'hello world'



    @botcmd
    def What_time_is_it(self, msg, args):
        import datetime
        now = datetime.datetime.now()
        return "Todays Date is: " + (now.strftime("%Y-%m-%d %H:%M:%S"))

    @botcmd
    def inc(self, msg, args):
        if 'counterb' not in self:
            self["counterb"]=0
        self["counterb"] = self["counterb"]+1
        return self["counterb"]

    @botcmd
    def mult(self, msg, args):
        if 'countera' not in self:
            self["countera"]=1
        self["countera"] = self["countera"] * 2
        return self["countera"]
    
    @botcmd
    def test(self, msg, args):
        self.send_card(title='Title + Body',
            body='text body to put in the card',
            thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
            image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            link='http://www.google.com',
            fields=(('First Key','Value1'), ('Second Key','Value2'), ('3', '3')),
            color='red',
            in_reply_to=msg
        )
        return 'test'


    @botcmd
    def Facebook(self, msg, args):
        self.send_card(title='Title + Body',
            body='text body to put in the card',
            thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
            image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            link='http://www.google.com',
            fields=(('First Key','Value1'), ('Second Key','Value2'), ('3', '3')),
            color='red',
            in_reply_to=msg
        )
        return 'test'

    @botcmd
    def DailyJoke(self, msg, args):
        return 'Ready for a funny joke? Here it goes- you might want to sit down for this one...' \
               'What did the astronauts fiancé say when he proposed in open space?

                "I can't breathe!"'
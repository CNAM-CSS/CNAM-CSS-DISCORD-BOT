import discord

class Event_manager:
    def __init__(self, bot):
        self.bot = bot
        self.event_activation()
    
    def event_activation(self):
        """
        Active les événements pour le bot.
        """
        
        @self.bot.event
        async def on_ready():
            print(f'{self.bot.user} est connecté et prêt à l\'emploi!')
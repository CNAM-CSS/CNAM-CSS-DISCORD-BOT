import discord
from discord.ext import commands

class Command_manager:
    def __init__(self, bot):
        self.bot = bot
        self.command_activation()

    def command_activation(self):
        """
        Active les commandes slash pour le bot.
        """

        @self.bot.slash_command(name="ping", description="Renvoie Pong!")
        async def ping(ctx: discord.ApplicationContext):
            """
            Commande slash qui renvoie 'Pong!' lorsqu'un utilisateur l'utilise.
            """
            print('Pong!')
            await ctx.respond('Pong!')

        @self.bot.slash_command(name="hello", description="Renvoie Salut !")
        async def hello(ctx: discord.ApplicationContext):
            """
            Commande slash qui renvoie 'Salut !' avec le nom de l'utilisateur.
            """
            await ctx.respond(f'Salut {ctx.author.name} !')
        
        @self.bot.slash_command(name="dadjoke", description="Renvoie une blague de papa aléatoire.")
        async def dadjoke(ctx: discord.ApplicationContext):
            """
            Commande slash qui renvoie une blague de papa aléatoire.
            """
            jokes = [
                "Pourquoi les plongeurs plongent toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
                "Que dit une imprimante dans l'eau ? J'ai papier !",
                "Je suis allé voir un spectacle de batteries hier soir, c’était frappant.",
                "Pourquoi les maths sont tristes ? Parce qu'elles ont trop de problèmes.",
            ]

            joke = random.choice(jokes)
            await ctx.respond(joke)
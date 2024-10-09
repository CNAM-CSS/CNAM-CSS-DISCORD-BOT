import discord
import random
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
            
        @self.bot.slash_command(name="contributors", description="Affiche la liste des contributeurs du projet.")
        async def contributors(ctx: discord.ApplicationContext):
            """
            Commande slash qui affiche la liste des contributeurs du projet de manière stylée.
            """
            embed = discord.Embed(
                title=":trophy: Contributeurs du projet :trophy:",
                description="Voici la liste des contributeurs qui ont apporté leur aide au développement du bot.",
                color=discord.Color.gold()
            )

            # Ajouter les contributeurs avec des icônes et des liens
            embed.add_field(
                name="KANTZER Jules",
                value="[GitHub](https://github.com/diezeJhon) [twitter](https://x.com/diezejhon)",
                inline=False
            )
            embed.add_field(
                name="DIGHAB Abdellah",
                value="[GitHub](https://github.com/adwge99)",
                inline=False
            )

            embed.set_footer(text="Merci à tous les contributeurs pour leur soutien !")
            await ctx.respond(embed=embed)
        
        @self.bot.slash_command(name="github", description="affiche le lien du github.")
        async def github(ctx: discord.ApplicationContext):
            """
            Commande slash qui affiche le lien du github du projet.
            """
            embed = discord.Embed(
                title=":trophy: Lien du projet GitHub :trophy:",
                description="Voici le lien du projet GitHub.",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="GitHub",
                value="[cliquez ici](https://github.com/CNAM-CSS/CNAM-CSS-DISCORD-BOT)")
            embed.set_footer(text="c'est un projet open source et collaboratif hésitez pas!")
            await ctx.respond(embed=embed)
            
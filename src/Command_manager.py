import discord
import random
from discord.ext import commands

import src.tools.api_meteo as api_meteo

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
            
        @self.bot.slash_command(name="meteo", description="La pluie et le beau temps")
        async def dadjoke(ctx: discord.ApplicationContext):
            """
            Commande slash qui renvoie les information météorologiques principales de l'Usinerie.
            """
            message_titre,message_temperature,message_lever_soleil,message_coucher_soleil,message_humidite,message_visibilite_nuages,message_vent,message_air = api_meteo.generer_message_meteo()
            embed = discord.Embed(
                title=message_titre,
                description=None,
                color=discord.Colour.from_rgb(193, 0, 42)
            )
            embed.add_field(
                name = 'Température',
                value = message_temperature,
                inline = False
            )
            embed.add_field(
                name = 'Lever et coucher de soleil',
                value = message_lever_soleil+'\n'+message_coucher_soleil,
                inline = False
            )
            embed.add_field(
                name = 'Humidité',
                value = message_humidite,
                inline = False
            )
            embed.add_field(
                name = 'Couverture et visibilité',
                value = message_visibilite_nuages,
                inline = False
            )
            embed.add_field(
                name = 'Vent',
                value = message_vent,
                inline = False
            )
            embed.add_field(
                name = 'Qualité de l\'air',
                value = message_air,
                inline = False
            )
            await ctx.respond(embed = embed)
        
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
            embed.add_field(
                name="MARTENNE Anatole",
                value="[GitHub](https://github.com/AnatMarX) [LinkedIn](https://www.linkedin.com/in/anatolemartenne/)",
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
            
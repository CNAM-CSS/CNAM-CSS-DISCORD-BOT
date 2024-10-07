import os
import discord
from discord.ext import commands
from .Event_manager import Event_manager
from .Command_manager import Command_manager

class Logger:
    def __init__(self, discord_token: str):
        self.discord_token = discord_token
        
        intents = discord.Intents.default()
        intents.members = True
        intents.messages = True
        
        # Utilisation du bot sans préfixe pour les commandes slash
        self.bot = commands.Bot(intents=intents)

        # Initialisation des événements et des commandes
        self.event_manager = Event_manager(self.bot)
        self.command_manager = Command_manager(self.bot)

    def start_bot(self) -> None:
        """
        Démarre le bot Discord, active les événements et les commandes.
        """
        self.bot.run(self.discord_token)
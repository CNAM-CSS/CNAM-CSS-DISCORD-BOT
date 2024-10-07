import os
from dotenv import load_dotenv
from src.Logger import Logger

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

def main():
    discord_token = os.getenv("DISCORD_TOKEN")
    
    if not discord_token:
        raise ValueError("Le token Discord n'est pas défini. Vérifiez votre fichier .env.")
    
    logger = Logger(discord_token)
    logger.start_bot()

if __name__ == "__main__":
    main()

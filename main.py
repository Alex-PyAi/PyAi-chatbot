# Process user data  
class Download:
    def __init__(self, user_json):
        """Initialise la classe avec l'URL de l'API."""
        self.user_data = user_json

    def download(self):
        """
        Permet de télécharger les séries déposé par l'utilisateur (excel, csv, json, ...).
        Ajouter des tests pour split ou summarize les données.
        Return JSON format
        """
        # Logique de téléchargement des données de l'utilisateur via drag and drop
        return json_data

# Load user data inside LLM
class Train:
    def __init__(self, model):
        """Initialise la classe avec le modèle."""
        self.model = model

    def train(self, json_data):
        """
        Permet d'ajouter les données dans le prompt afin d'optimiser la requête.
        """
        # Logique d'ajout des données au modèle ici
        return trained_model

# Chat with LLM about your data 
class Chat:
    def __init__(self, model):
        """Initialise la classe avec le modèle."""
        self.model = model

    def chat(self, message):
        """
        Permet d'interagir avec un LLM sur les données JSON importées.
        Output doit ressembler à une analyse de données avec contexte, évolution, graphiques, tableaux, ...
        """
        # Logique d'interaction avec le modèle et génération de la réponse
        return response

  
 

